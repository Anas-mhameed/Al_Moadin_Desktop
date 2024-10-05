import os
from PySide6.QtUiTools import QUiLoader
import resources_rc
from PySide6.QtWidgets import (
    QMainWindow, 
    QStackedWidget, 
    QWidget, 
    QSpinBox, 
    QLabel, 
    QLineEdit, 
    QPushButton,
    QFrame,
    QSlider,
    QTimeEdit,
    QComboBox,
    QDateEdit,
    QCalendarWidget,
    QScrollArea,
    QMessageBox, 
    )
from ResourceFile import resource_path
from PySide6.QtGui import QFontDatabase, QFont
from functools import partial
from PySide6.QtCore import QFile, QDate, QEvent
from PySide6.QtCore import QTimer, Qt
from AdanManager import AdanManager
from GeneralSettings import GeneralSettings
from TimeManager import TimeManager
from InstantPlayer import InstantPlayer
from PlayerManager import PlayerManager
from PlayerManagerHelper import PlayerManagerHelper
from Messager import MainMessager, SecondaryMessager
from Runnable import RunnableManager, Runnable
from DatabaseManager import DatabaseManager
from NotificationManager import NotificationManager
from SpinBoxTrack import SpinBoxTrack
from time import sleep

class AppManager(QMainWindow):

    def __init__(self, ui_file):
        super(AppManager, self).__init__()

        if not os.path.exists(ui_file):
            raise FileNotFoundError(f"The UI file '{ui_file}' does not exist.")

        loader = QUiLoader()
        ui_file = QFile(ui_file)

        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError(f"Unable to open/read the UI file '{ui_file}'.")

        self.ui = loader.load(ui_file)
        ui_file.close()

        self.setWindowTitle("برنامج المؤذن")
        self.setCentralWidget(self.ui)
        # self.ui.closeEvent = self.closeEvent
        # self.ui.close = self.close
      
        self.setup_ui()

        self.database_manager = DatabaseManager()
        self.runnable_manager = RunnableManager()

        self.intiate_adans_state_button()

        self.messager = MainMessager(self.client_info_msg_frame, self.error_msg_label, self.info_msg_label)

        self.secondary_messager = SecondaryMessager(self.noti_msg_frame, self.noti_msg_label)

        self.player_manager = PlayerManager(self, self.messager, self.runnable_manager)

        self.general_settings = GeneralSettings(self.get_masjed_name_label(), self.get_masjed_name_input(), self.get_city_input(), self.get_quds_time_diff_input(), self.get_winter_summer_buttons(), self.get_time_formate_buttons(), self.database_manager, self.runnable_manager)
        

        self.time_manager = TimeManager(self.am_pm_label, self.seconds_label, self.am_pm_frame, self.time_lower_widget, self.main_time_label, self.day_label, self.gregorian_date_label, self.hijri_date_label)

        self.general_settings.time_formate_changed.connect(self.time_manager.update_time_formate)
        self.time_manager.connect_to_get_formate_signal(self.general_settings.set_time_formate)
        self.time_manager.get_time_formate()
        
        self.adan_manager = AdanManager(self, self.database_manager, self.runnable_manager, self.player_manager, self.five_prayers, self.shorok,  self.jomoaa_prayer, self.adansSoundButtons, self.next_adan_label, self.remaining_time_label, self.general_settings, self.emergency_frame, self.emergency_label, self.emergency_stop_button)
        self.adan_manager.possible_not_adan_time_signal.connect(self.player_manager.possible_fake_prepare_emitted)
        self.player_manager.hide_emergency_frame_signal.connect(self.adan_manager.emerg_frame_hide)
        # self.adan_manager.stop_adan_signal.connect(self.player_manager.force_stop_adan)
        self.adan_manager.pause_adan_signal.connect(self.player_manager.pause_adan)
        self.adan_manager.resume_adan_signal.connect(self.player_manager.resume_adan)
        self.adan_manager.play_adan_signal.connect(self.player_manager.play_adan)
        self.adan_manager.force_stop_adan_signal.connect(self.player_manager.force_stop_adan)

        self.time_manager.connect_to_time_updated_signal(self.adan_manager.next_adan.handle_time_updated)
        
        self.general_settings.summer_timing_changed.connect(self.adan_manager.handle_summer_winter_change)
        self.general_settings.quds_diff_changed.connect(self.adan_manager.handle_quds_diff_change)
        self.general_settings.adan_time_formate_changed.connect(self.adan_manager.handle_new_time_formate)
        
        self.adan_manager.get_settings_signal.connect(self.general_settings.send_all_settings_to_adan_manager)
        self.adan_manager.get_settings()

        self.time_manager.connect_to_next_day_signal(self.adan_manager.handle_new_day)
        self.time_manager.connect_to_new_jomoaa_signal(self.adan_manager.handle_new_jomoaa)
        self.time_manager.connect_to_next_day_signal(self.adan_manager.next_adan.update_curr_day)

        self.adan_manager.prepare_for_adan_signal.connect(self.player_manager.prepare_for_adan)

        self.instant_player = InstantPlayer(self.runnable_manager, self, self.player_manager, self.instant_player_choose_file_button, self.instant_player_delete_file_button, self.volume_controller, self.instant_player_play_button, self.instant_player_pause_button, self.instant_player_resume_button, self.instant_player_stop_button)
        self.player_manager.force_stop_instant_player.connect(self.instant_player.stop)
        self.instant_player.finished_signal.connect(self.player_manager.handle_instant_finished_signal)
        self.player_manager.play_instant_player.connect(self.instant_player.play)
        self.instant_player.can_I_play.connect(self.player_manager.can_instant_player_play)


        self.notification_manager = NotificationManager(self.adan_manager.get_adans_for_notification_manager(), [0,0], self, self.scrollAreaContainer, self.player_manager, self.secondary_messager, self.runnable_manager,  self.total_notification_label, self.noti_sort_box, self.database_manager)

        self.adan_manager.fajer_duartion_signal.connect(self.notification_manager.handle_fajer_duration_changed)
        self.adan_manager.basic_duartion_signal.connect(self.notification_manager.handle_basic_duration_changed)
        self.adan_manager.set_sounds_source()

        self.time_manager.connect_to_time_updated_signal(self.notification_manager.handel_time_changed)

        self.notification_manager.can_noti_play.connect(self.player_manager.can_noti_play)
        
        self.adan_manager.adan_time_changed.connect(self.notification_manager.update_notis_and_intiate_index)
        
        # self.player_manager_helper = PlayerManagerHelper(self.adan_manager, self.notification_manager, self.instant_player )
        
        # self.player_manager.set_player_manager_helper(self.player_manager_helper
        


        self.noti_sort_box.currentIndexChanged.connect(self.notification_manager.show_notifications)
        
        # load from db
        # self.notification_manager.get_notification_from_db()

        def temp():
            self.player_manager.turn_off_notification()
            self.player_manager.set_is_notification_playing(False)

        self.stop_notification_button.clicked.connect(temp)

        self.start()

    def setup_ui(self):

        self.am_pm_frame = self.ui.findChild(QFrame, "am_pm_frame")
        self.am_pm_label = self.ui.findChild(QLabel, "am_pm_label")
        self.seconds_label = self.ui.findChild(QLabel, "seconds_label")

        self.stop_notification_button = self.ui.findChild(QPushButton, "stop_notification")

        self.noti_scrollArea = self.ui.findChild(QScrollArea, "noti_scrollArea")
        self.scrollAreaContainer = self.ui.findChild(QWidget, "scrollAreaContainer")

        self.total_notification_label = self.ui.findChild(QLabel, "total_noti_label")
        self.noti_sort_box = self.ui.findChild(QComboBox, "noti_sort_box")
        self.noti_sort_box.currentIndexChanged.connect(self.sort_noti_index_changed)        

        self.noti_msg_label = self.ui.findChild(QLabel, "noti_msg_label")
        self.noti_msg_frame = self.ui.findChild(QFrame, "noti_msg_frame")

        self.create_noti_button = self.ui.findChild(QPushButton, "new_notification_buttton")
        self.create_noti_button.clicked.connect(lambda: self.change_page(4))

        self.cancel_noti_button = self.ui.findChild(QPushButton, "cancel_noti_create")
        self.cancel_noti_button.clicked.connect(self.cancel_noti_handle)

        self.noti_date_frame = self.ui.findChild(QFrame, "noti_date_frame")
        self.noti_date_frame.hide()

        self.permenante_noti_button = self.ui.findChild(QPushButton, "permenante_noti")
        self.once_noti_button = self.ui.findChild(QPushButton, "once_noti")
        self.permenante_noti_button.clicked.connect(lambda: self.noti_btn_clicked(self.permenante_noti_button, self.once_noti_button))
        self.once_noti_button.clicked.connect(lambda:  self.noti_btn_clicked(self.once_noti_button, self.permenante_noti_button))

        self.before_adan_type_button = self.ui.findChild(QPushButton, "before_adan_type_button")
        self.after_adan_type_button = self.ui.findChild(QPushButton, "after_adan_type_button")
        
        self.before_adan_frame = self.ui.findChild(QFrame, "before_adan_frame")
        self.after_adan_frame = self.ui.findChild(QFrame, "after_adan_frame")

        self.after_adan_frame.setStyleSheet(""" 
            QFrame{
                background-color: rgb(240, 240, 240);                               
                text-decoration: line-through;
                }
            """)

        self.before_adan_minutes_spin = self.ui.findChild(QSpinBox, "before_adan_minutes_spin")
        self.before_adan_minutes_spin.valueChanged.connect(self.minutes_changes)
        self.before_adan_box = self.ui.findChild(QComboBox, "before_adan_box")
        self.before_adan_box.currentIndexChanged.connect(self.change_datetime_data)

        self.after_adan_minutes_spin = self.ui.findChild(QSpinBox, "after_adan_minutes_spin") 
        self.after_adan_minutes_spin.setFocusPolicy(Qt.NoFocus)
        self.spinbox_tracker = SpinBoxTrack(self.after_adan_minutes_spin)
        self.after_adan_box = self.ui.findChild(QComboBox, "after_adan_box")
        self.after_adan_box.currentIndexChanged.connect(self.change_datetime_data)

        self.after_adan_box.setDisabled(True)
        self.after_adan_minutes_spin.setDisabled(True)

        self.duration_spinbox = self.ui.findChild(QSpinBox, "duration_spinbox")
        self.duration_spinbox.valueChanged.connect(self.minutes_changes)

        self.before_adan_type_button.clicked.connect(lambda: self.noti_clac_type(self.before_adan_type_button, self.after_adan_type_button))
        self.after_adan_type_button.clicked.connect(lambda: self.noti_clac_type(self.after_adan_type_button, self.before_adan_type_button))
        self.noti_date = self.ui.findChild(QCalendarWidget, "noti_date")


        self.choose_notification_sound = self.ui.findChild(QPushButton, "notification_sound_button")
        self.save_notification = self.ui.findChild(QPushButton, "save_notification_button")

        self.choose_notification_sound.clicked.connect(lambda : self.notification_manager.choose_sound(self))
        self.save_notification.clicked.connect(lambda: self.save_notification_handler())

        self.client_info_msg_frame = self.ui.findChild(QFrame, "client_info_msg_frame")
        self.client_info_msg_frame.hide()
        self.error_msg_label = self.ui.findChild(QLabel, "error_msg_label")
        self.info_msg_label = self.ui.findChild(QLabel, "info_msg_label")

        self.instant_player_play_button = self.ui.findChild(QPushButton,"instant_player_play_button")
        self.instant_player_pause_button = self.ui.findChild(QPushButton,"instant_player_pause_button")
        self.instant_player_resume_button = self.ui.findChild(QPushButton,"instant_player_resume_button")
        self.instant_player_stop_button = self.ui.findChild(QPushButton,"instant_player_stop_button")
        self.volume_controller = self.ui.findChild(QSlider,"instant_play_volume_controller")
        self.instant_player_choose_file_button = self.ui.findChild(QPushButton,"instant_player_choose_file_button")
        self.instant_player_delete_file_button = self.ui.findChild(QPushButton,"instant_player_delete_file_button")

        self.emergency_frame = self.ui.findChild(QWidget, "emergency_stop_widget")
        self.emergency_frame.hide()
        self.emergency_label = self.ui.findChild(QLabel, "emergency_label")
        self.emergency_stop_button = self.ui.findChild(QPushButton, "emergency_stop_button")

        self.stacked_widget = self.ui.findChild(QStackedWidget, "stackedWidget")
        self.stacked_widget.setCurrentIndex(0)

        self.menu = self.ui.findChild(QWidget,"expandedMenu")
        self.menu.setHidden(True)

        if self.menu:
            self.menu_buttons = self.menu.findChildren(QPushButton)
            for i in range(len(self.menu_buttons) - 1):
                self.menu_buttons[i].clicked.connect(partial(self.change_page,i))


        # preparing the AdanManager components
        self.adansSoundButtons = []
        self.adansSoundButtons.append(self.ui.findChild(QPushButton, "adansSoundButton"))
        self.adansSoundButtons.append(self.ui.findChild(QPushButton, "fajerSoundButton"))


        adans_widget = self.ui.findChild(QWidget,"adansWidget") 
        if adans_widget:
            self.five_prayers = []
            for i in ["fajerWidget", "dohorWidget", "aserWidget", "magrebWidget", "ishaaWidget"]:
                self.five_prayers.append(adans_widget.findChild(QWidget, i))
        
        self.shorok = self.ui.findChild(QWidget, "shorokWidget")

        self.jomoaa_prayer = self.ui.findChild(QWidget, "jomoaaWidget")

        self.next_adan_label = self.ui.findChild(QLabel, "nextAdanNameLabel")
        
        self.remaining_time_label = self.ui.findChild(QLabel, "remainingTimeLabel")


        # preparing the general settings components
        self.masjed_name_label = self.ui.findChild(QLabel, "masgedNameLabel")
        
        self.masjed_name_input = self.ui.findChild(QLineEdit, "masjedNameInput")

        self.city_input = self.ui.findChild(QLineEdit, "cityInput")

        self.time_diff_from_quds = self.ui.findChild(QSpinBox, "qudsTimeDiff")

        self.win_sum_frame = self.ui.findChild(QFrame, "win_sum_frame")
        self.win_sum_buttons = self.win_sum_frame.findChildren(QPushButton)

        self.time_formate_frame = self.ui.findChild(QFrame, "time_formate_frame")
        self.time_formate_buttons = self.time_formate_frame.findChildren(QPushButton)


        #  preparing the TimeManager components
        self.main_time_label = self.ui.findChild(QLabel, "clockLabel")
        
        font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Chivo_Mono/ChivoMono-VariableFont_wght.ttf"))
        
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, 80)
        font.setWeight(QFont.Bold)
        self.main_time_label.setFont(font)

        self.gregorian_date_label = self.ui.findChild(QLabel, "dateLabel")
 
        self.hijri_date_label = self.ui.findChild(QLabel, "hijriLabel")
        
        self.time_lower_widget = self.ui.findChild(QWidget, "timeLowerWidget")

        self.day_label = self.ui.findChild(QLabel, "dayLabel")

    def intiate_adans_state_button(self):
        data = self.database_manager.get_adans_state()
        buttons_names = ["fajer_activate_button", "dohor_activate_button", "aser_activate_button", "magreb_activate_button", "ishaa_activate_button"]

        buttons = []
        for adan_data in data:
            adan_button = self.ui.findChild(QPushButton, buttons_names[adan_data[0] - 1])
            buttons.append(adan_button)

            if adan_data[1] == 1:
                adan_button.setChecked(True)
        
        buttons[0].toggled.connect(lambda checked : self.update_adan_state(1, checked))
        buttons[1].toggled.connect(lambda checked : self.update_adan_state(2, checked))
        buttons[2].toggled.connect(lambda checked : self.update_adan_state(3, checked))
        buttons[3].toggled.connect(lambda checked : self.update_adan_state(4, checked))
        buttons[4].toggled.connect(lambda checked : self.update_adan_state(5, checked))

    def update_adan_state(self, adan_index, checked):
        def temp(func):
            if func():
                self.database_manager.update_adan_state(adan_index, checked)
        runnable = Runnable(temp)
        self.runnable_manager.runTask(runnable)

    def change_page(self, index):
        # Change the index of the stacked widget
        self.stacked_widget.setCurrentIndex(index)
        
        for i in range(len(self.menu_buttons)):
            if i != index:
                self.menu_buttons[i].setChecked(False)
            else:
                self.menu_buttons[i].setChecked(True)
        
        if index > len(self.menu_buttons):
            self.reset_all_noti_data()

    def sort_noti_index_changed(self):
        self.notification_manager.clear_layout()
        self.notification_manager.show_notifications()

    def set_curr_date_time(self, date):
        self.noti_date.setSelectedDate(date)

    def set_minimum_date(self, date):
        self.noti_date.setMinimumDate(date)

    def set_up_date(self):
        current_date = QDate.currentDate()
        self.set_minimum_date(current_date)
        self.set_curr_date_time(current_date)
    
    def reset_before_adanBox_minuteSpinBox(self):
        self.before_adan_minutes_spin.setValue(1)
        self.before_adan_box.setCurrentIndex(0)
    
    def reset_after_adanBox_minuteSpinBox(self):
        self.after_adan_minutes_spin.setRange(10,60)
        self.after_adan_minutes_spin.setValue(10)
        self.after_adan_minutes_spin.setSuffix(" ثواني")
        self.after_adan_minutes_spin.setSingleStep(10)
        self.spinbox_tracker.reset_values()
        self.after_adan_box.setCurrentIndex(0)

    def change_datetime_data(self):
        if self.before_adan_box.currentIndex() == 5 or self.after_adan_box.currentIndex() == 5:
            jomoaa_datetime = self.adan_manager.get_current_adan_time(6)
            jomoaa_date = jomoaa_datetime.date()
            
            jomoaa_qdate = QDate(jomoaa_date.year, jomoaa_date.month, jomoaa_date.day)

            self.set_minimum_date(jomoaa_qdate)

        else :
            self.set_minimum_date(QDate().currentDate())

    def reset_all_noti_data(self):
        self.reset_before_adanBox_minuteSpinBox()
        self.reset_after_adanBox_minuteSpinBox()
        self.duration_spinbox.setValue(0)
        self.set_curr_date_time(QDate.currentDate())

    def cancel_noti_handle(self):
        self.change_page(1)
        self.reset_all_noti_data()

    def noti_clac_type(self, primary_btn, secondary_btn):

        if secondary_btn.isChecked():
            secondary_btn.setChecked(False)
        else:
            primary_btn.setChecked(True)

        if primary_btn.objectName() == "after_adan_type_button":

            self.after_adan_box.setDisabled(False)
            self.after_adan_minutes_spin.setDisabled(False)

            self.before_adan_minutes_spin.setDisabled(True)
            self.before_adan_box.setDisabled(True)

            self.reset_before_adanBox_minuteSpinBox()

            self.after_adan_frame.setStyleSheet(""" 
            QFrame{                               
                background-color: rgb(255, 255, 255);
                text-decoration: none;
                }
            """)
            self.before_adan_frame.setStyleSheet(""" 
            QFrame{
                background-color: rgb(240, 240, 240);
                text-decoration: line-through;                            
                }
            """)
        else:
            self.before_adan_minutes_spin.setDisabled(False)
            self.before_adan_box.setDisabled(False)

            self.after_adan_box.setDisabled(True)
            self.after_adan_minutes_spin.setDisabled(True)

            self.reset_after_adanBox_minuteSpinBox()

            self.before_adan_frame.setStyleSheet(""" 
            QFrame{
                background-color: rgb(255, 255, 255);
                text-decoration: none;                               
                }
            """)
            self.after_adan_frame.setStyleSheet(""" 
            QFrame{
                background-color: rgb(240, 240, 240);                               
                text-decoration: line-through;
                }
            """)

    def minutes_changes(self, value):
        spinbox = self.sender()
        if value < 11:
            spinbox.setSuffix(" دقائق")
        else:
            spinbox.setSuffix(" دقيقة")

    def save_notification_handler(self):
        is_permenant = self.permenante_noti_button.isChecked()
        
        duration = self.duration_spinbox.value()
        date = None
        
        def temp(func):
                time_to_sleep = 5
                while func() and time_to_sleep != 0:
                    time_to_sleep -= 1
                    sleep(1)
                self.secondary_messager.hide()

        if self.notification_manager.is_empty_sound():
            self.secondary_messager.update_info_label("الرجاء ادخال ملف صوتي")
            self.secondary_messager.show()

            runnable = Runnable(temp)
            self.runnable_manager.runTask(runnable)               
        else:
            if not is_permenant:
                # date of type QDate
                date = self.noti_date.selectedDate()
                day_of_week = date.dayOfWeek()
        
                if (self.before_adan_box.currentIndex() == 5 and day_of_week != 5 and self.before_adan_type_button.isChecked()) or (self.after_adan_box.currentIndex() == 5 and day_of_week != 5 and self.after_adan_type_button.isChecked()):
                    self.secondary_messager.update_info_label("عليك اختيار تاريخ يوافق يوم الجمعة")
                    self.secondary_messager.show()
                        
                    runnable = Runnable(temp)
                    self.runnable_manager.runTask(runnable)
                    return

            if self.before_adan_type_button.isChecked():
                # before adan notification
                res = self.notification_manager.create_notification(True, is_permenant, self.before_adan_box.currentIndex() + 1, (self.before_adan_minutes_spin.value() * 60), date, duration)
            else:
                # after adan notification
                seconds = self.after_adan_minutes_spin.value()
                if self.after_adan_minutes_spin.suffix() != " ثواني":
                    seconds *= 60
                
                res = self.notification_manager.create_notification(False, is_permenant, self.after_adan_box.currentIndex() + 1, seconds, date, duration)
            
            if res :
                self.cancel_noti_handle()

    def noti_btn_clicked(self, primary_btn, secondary_btn):
        if secondary_btn.isChecked():
            secondary_btn.setChecked(False)
            obj_name = secondary_btn.objectName()
            if obj_name == "once_noti":
                self.noti_date_frame.hide()

            elif obj_name == "permenante_noti" :
                self.noti_date_frame.show()
                self.set_up_date()
        else:
            primary_btn.setChecked(True)
    # for AdansManager
    def get_five_prayers(self):
        return self.five_prayers

    def get_adans_sound_buttons(self):
        return self.adansSoundButtons

    def get_next_adan_label(self):
        return self.next_adan_label
    
    def get_remaining_time_label(self):
        return self.remaining_time_label

    def get_shorok_widget(self):
        return self.shorok
    
    def get_jomoaa_prayer(self):
        return self.jomoaa_prayer
    
    # for general settings
    def get_masjed_name_label(self):
        return self.masjed_name_label
    
    def get_masjed_name_input(self):
        return self.masjed_name_input
    
    def get_city_input(self):
        return self.city_input
    
    def get_quds_time_diff_input(self):
        return self.time_diff_from_quds
    
    def get_winter_summer_buttons(self):
        return self.win_sum_buttons
    
    def get_time_formate_buttons(self):
        return self.time_formate_buttons

    # start function
    def start(self):
        timer = QTimer(self)
        timer.timeout.connect(lambda: self.run())
        timer.start(1000)
    
    def run(self):

        self.time_manager.run()
        
        self.player_manager.run()
        # self.adan_manager.run()

        # self.notification_manager.run()

    def closeEvent(self, event: QEvent):
        self.runnable_manager.terminate_all_workers()
        self.runnable_manager.wait_for_done()
        event.accept()
        