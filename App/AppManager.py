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
    QComboBox,
    QCalendarWidget,
    QScrollArea,
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
from MsgManager import MsgManager
from Runnable import RunnableManager, Runnable
from NotificationManager import NotificationManager
from SpinBoxTrack import SpinBoxTrack
from ZigbeeController import ZigbeeController
from ProgramUpdater import ProgramUpdater
from DatabaseManager import DatabaseManager
from Mediator import Mediator


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
      
        self.setup_ui()

        # Initialize the mediator
        self.mediator = Mediator()

        # Initialize DatabaseManager as a singleton
        self.database_manager = DatabaseManager()
        self.runnable_manager = RunnableManager()

        # self.program_updater = ProgramUpdater()

        self.database_manager.initialize_app_version()

        # Check if token exists
        if not self.database_manager.check_token():
            token = self.database_manager.get_token()
        else:
            # Else ask for token
            token = "123"
            # Save token in database
            self.database_manager.save_token(token)

        self.zigbee_controller = ZigbeeController(token, self.runnable_manager)

        def temp():
            def helper(func):
                if func():
                    self.zigbee_controller.connect_to_zigbee_btn_clicked()
            runnable = Runnable(helper)
            self.runnable_manager.runTask(runnable)
            
        self.connect_to_zigbee_btn.clicked.connect(temp)
        
        self.intiate_adans_state_button()

        self.msg_manager = MsgManager()
        self.mediator.register("MsgManager", self.msg_manager)

        self.player_manager = PlayerManager(self, self.emergency_frame, self.emergency_label, self.emergency_stop_button)
        self.mediator.register("PlayerManager", self.player_manager)
  

        #  NEED TO BE CHECKED ------ TO BE COMPLETED ------
        self.player_manager.open_mic_signal.connect(lambda: self.zigbee_controller.run(True))
        self.player_manager.close_mic_signal.connect(lambda: self.zigbee_controller.run(False))
        #  TILL HERE ||||||||||||||||||||| ------ TO BE COMPLETED ------

        self.adan_manager = AdanManager(self, self.five_prayers, self.shorok,  self.jomoaa_widget, self.adansSoundButtons, self.next_adan_label, self.remaining_time_label)
        self.mediator.register("AdanManager", self.adan_manager)

        self.general_settings = GeneralSettings(self.get_masjed_name_label(), self.get_masjed_name_input(), self.get_city_input(), self.get_quds_time_diff_input(), self.get_winter_summer_buttons(), self.get_time_formate_buttons(), self.runnable_manager)
        self.mediator.register("GeneralSettings", self.general_settings)

        self.time_manager = TimeManager(self.mediator, self.am_pm_label, self.seconds_label, self.am_pm_frame, self.time_lower_widget, self.main_time_label, self.day_label, self.gregorian_date_label)

        self.time_manager.get_time_formate()
        
        self.time_manager.connect_to_time_updated_signal(self.adan_manager.next_adan.handle_time_updated)

        self.instant_player = InstantPlayer(self, self.player_manager, self.instant_player_choose_file_button, self.instant_player_delete_file_button, self.volume_controller, self.instant_player_play_button, self.instant_player_pause_button, self.instant_player_resume_button, self.instant_player_stop_button)

        self.notification_manager = NotificationManager(self.adan_manager.get_adans_for_notification_manager(), self, self.scrollAreaContainer, self.runnable_manager,  self.total_notification_label, self.noti_sort_box)
        self.mediator.register("NotificationManager", self.notification_manager)

        self.adan_manager.request_settings()
        self.notification_manager.request_adans_duration()

        self.time_manager.connect_to_time_updated_signal(self.notification_manager.handel_time_changed)


        # Here -----------------------------------------

        # self.adan_manager.fajer_duartion_signal.connect(self.notification_manager.handle_fajer_duration_changed)
        # self.adan_manager.basic_duartion_signal.connect(self.notification_manager.handle_basic_duration_changed)

        # self.adan_manager.set_sounds_source()

        # self.adan_manager.adan_time_changed.connect(self.notification_manager.update_notis_and_intiate_index)

        #  ---------------------------------------------

        self.noti_sort_box.currentIndexChanged.connect(self.notification_manager.show_notifications)
        self.notification_manager.cancel_noti_signal.connect(self.cancel_noti_handle)
        self.stop_notification_button.clicked.connect(lambda: self.player_manager.stop_notification())

        self.start()

    def setup_ui(self):
        
        Rubik_font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Rubik/static/Rubik-SemiBold.ttf"))
        Rubik_SemiBold_font_family = QFontDatabase.applicationFontFamilies(Rubik_font_id)[0]
        Rubik_SemiBold_font_38 = QFont(Rubik_SemiBold_font_family, 38)
        Rubik_SemiBold_font_34 = QFont(Rubik_SemiBold_font_family, 34)
        Rubik_SemiBold_font_32 = QFont(Rubik_SemiBold_font_family, 32)

        Tajawal_font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Tajawal/Tajawal-Bold.ttf"))
        tajawal_bold_font_family = QFontDatabase.applicationFontFamilies(Tajawal_font_id)[0]
        tajawal_bold_font_16 = QFont(tajawal_bold_font_family, 16)
        tajawal_bold_font_18 = QFont(tajawal_bold_font_family, 18)
        tajawal_bold_font_20 = QFont(tajawal_bold_font_family, 20)

        Noto_Kufi_Arabic_font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Noto_Kufi_Arabic/static/NotoKufiArabic-SemiBold.ttf"))
        kufi_font_family = QFontDatabase.applicationFontFamilies(Noto_Kufi_Arabic_font_id)[0]
        kufi_font_24 = QFont(kufi_font_family, 24)
        kufi_font_24.setBold(True)

        kufi_font_18 = QFont(kufi_font_family, 18)
        kufi_bold_font_18 = QFont(kufi_font_family, 18)
        kufi_bold_font_18.setBold(True)

        Marhey_font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Marhey/static/Marhey-Regular.ttf"))
        merhay_font_family = QFontDatabase.applicationFontFamilies(Marhey_font_id)[0]
        merhay_font_14 = QFont(merhay_font_family, 14)

        Vazirmatn_font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Vazirmatn/static/Vazirmatn-Bold.ttf"))
        Vazirmatn_Bold_font_family = QFontDatabase.applicationFontFamilies(Vazirmatn_font_id)[0]
        Vazirmatn_Bold_font_34 = QFont(Vazirmatn_Bold_font_family, 34)

        Readex_Pro_font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Readex_Pro/static/ReadexPro-Regular.ttf"))
        ReadexPro_font_family = QFontDatabase.applicationFontFamilies(Readex_Pro_font_id)[0]
        ReadexPro_font_28 = QFont(ReadexPro_font_family, 28)

        Chivo_Mono_font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Chivo_Mono/ChivoMono-VariableFont_wght.ttf"))       
        ChivoMono_VariableFont_wght_font_family = QFontDatabase.applicationFontFamilies(Chivo_Mono_font_id)[0]
        ChivoMono_VariableFont_wght_font_80 = QFont(ChivoMono_VariableFont_wght_font_family, 80)
        ChivoMono_VariableFont_wght_font_80.setWeight(QFont.Bold)

        self.menu_title_label = self.ui.findChild(QLabel, "menuTitleLabel")
        self.menu_title_label.setFont(tajawal_bold_font_20)

        self.main_page_button = self.ui.findChild(QPushButton, "mainPageButton")
        self.main_page_button.setFont(tajawal_bold_font_16)

        self.notification_page_button = self.ui.findChild(QPushButton, "notificationsPageButton")
        self.notification_page_button.setFont(tajawal_bold_font_16)
        
        self.quraan_page_button = self.ui.findChild(QPushButton, "quraanPageButton")
        self.quraan_page_button.setFont(tajawal_bold_font_16)
        
        self.settings_page_button = self.ui.findChild(QPushButton, "settingsPageButton")
        self.settings_page_button.setFont(tajawal_bold_font_16)

        self.connect_to_zigbee_btn = self.ui.findChild(QPushButton, "connect_to_zigbee_btn")
        
        self.am_pm_frame = self.ui.findChild(QFrame, "am_pm_frame")
        self.am_pm_label = self.ui.findChild(QLabel, "am_pm_label")
        self.seconds_label = self.ui.findChild(QLabel, "seconds_label")

        self.stop_notification_button = self.ui.findChild(QPushButton, "stop_notification")
        self.stop_notification_button.setFont(tajawal_bold_font_16)

        self.noti_scrollArea = self.ui.findChild(QScrollArea, "noti_scrollArea")
        self.scrollAreaContainer = self.ui.findChild(QWidget, "scrollAreaContainer")

        self.total_notification_label = self.ui.findChild(QLabel, "total_noti_label")
        self.total_notification_label.setFont(Rubik_SemiBold_font_32)

        self.total_noti_text_label = self.ui.findChild(QLabel, "total_noti_text_label")
        self.total_noti_text_label.setFont(Rubik_SemiBold_font_32)

        self.notis_text_label = self.ui.findChild(QLabel, "notis_text_label")
        self.notis_text_label.setFont(kufi_font_24)

        self.noti_sort_box = self.ui.findChild(QComboBox, "noti_sort_box")
        self.noti_sort_box.currentIndexChanged.connect(self.sort_noti_index_changed)        

        self.noti_sort_box.setFont(kufi_font_18)
        self.noti_sort_box.view().setFont(kufi_font_18)

        # self.noti_msg_label = self.ui.findChild(QLabel, "noti_msg_label")
        # self.noti_msg_frame = self.ui.findChild(QFrame, "noti_msg_frame")

        self.create_noti_button = self.ui.findChild(QPushButton, "new_notification_buttton")
        self.create_noti_button.setFont(tajawal_bold_font_16)
        self.create_noti_button.clicked.connect(lambda: self.change_page(4))

        self.cancel_noti_button = self.ui.findChild(QPushButton, "cancel_noti_create")
        self.cancel_noti_button.setFont(tajawal_bold_font_16)
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
        self.before_adan_minutes_spin.setFont(kufi_font_18)

        self.before_adan_minutes_spin.valueChanged.connect(self.minutes_changes)
        self.before_adan_box = self.ui.findChild(QComboBox, "before_adan_box")
        self.before_adan_box.setFont(kufi_font_18)
        self.before_adan_box.view().setFont(kufi_font_18)

        self.before_adan_box.currentIndexChanged.connect(self.change_datetime_data)

        self.after_adan_minutes_spin = self.ui.findChild(QSpinBox, "after_adan_minutes_spin") 
        self.after_adan_minutes_spin.setFont(kufi_font_18)

        self.after_adan_minutes_spin.setFocusPolicy(Qt.NoFocus)

        self.spinbox_tracker = SpinBoxTrack(self.after_adan_minutes_spin)
        self.after_adan_box = self.ui.findChild(QComboBox, "after_adan_box")
        self.after_adan_box.setFont(kufi_font_18)
        self.after_adan_box.view().setFont(kufi_font_18)

        self.after_adan_box.currentIndexChanged.connect(self.change_datetime_data)

        self.after_adan_box.setDisabled(True)
        self.after_adan_minutes_spin.setDisabled(True)

        self.duration_spinbox = self.ui.findChild(QSpinBox, "duration_spinbox")
        self.duration_spinbox.setFont(kufi_font_18)

        self.duration_spinbox.valueChanged.connect(self.minutes_changes)

        self.before_adan_type_button.clicked.connect(lambda: self.noti_clac_type(self.before_adan_type_button, self.after_adan_type_button))
        self.after_adan_type_button.clicked.connect(lambda: self.noti_clac_type(self.after_adan_type_button, self.before_adan_type_button))
        self.noti_date = self.ui.findChild(QCalendarWidget, "noti_date")


        self.choose_notification_sound = self.ui.findChild(QPushButton, "notification_sound_button")
        self.choose_notification_sound.setFont(tajawal_bold_font_16)

        self.save_notification = self.ui.findChild(QPushButton, "save_notification_button")
        self.save_notification.setFont(tajawal_bold_font_16)

        self.choose_notification_sound.clicked.connect(lambda : self.notification_manager.choose_sound(self))
        self.save_notification.clicked.connect(lambda: self.save_notification_handler())

        # self.client_info_msg_frame = self.ui.findChild(QFrame, "client_info_msg_frame")
        # self.client_info_msg_frame.hide()

        # self.error_msg_label = self.ui.findChild(QLabel, "error_msg_label")
        # self.info_msg_label = self.ui.findChild(QLabel, "info_msg_label")

        # self.error_msg_label.setFont(merhay_font_14)
        # self.info_msg_label.setFont(merhay_font_14)


        self.instant_player_play_button = self.ui.findChild(QPushButton,"instant_player_play_button")
        self.instant_player_pause_button = self.ui.findChild(QPushButton,"instant_player_pause_button")
        self.instant_player_resume_button = self.ui.findChild(QPushButton,"instant_player_resume_button")
        self.instant_player_stop_button = self.ui.findChild(QPushButton,"instant_player_stop_button")
        self.volume_controller = self.ui.findChild(QSlider,"instant_play_volume_controller")

        tajawal_bold_font_14 = QFont(tajawal_bold_font_family, 14)
        tajawal_bold_font_14.setBold(True)

        self.instant_player_choose_file_button = self.ui.findChild(QPushButton,"instant_player_choose_file_button")
        self.instant_player_delete_file_button = self.ui.findChild(QPushButton,"instant_player_delete_file_button")

        self.instant_player_choose_file_button.setFont(tajawal_bold_font_14)
        self.instant_player_delete_file_button.setFont(tajawal_bold_font_14)        

        self.emergency_frame = self.ui.findChild(QWidget, "emergency_stop_widget")
        self.emergency_frame.hide()

        self.emergency_label = self.ui.findChild(QLabel, "emergency_label")
        self.emergency_label.setFont(kufi_bold_font_18)

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

        # adans_sound_button = self.ui.findChild(QPushButton, "adansSoundButton")
        fajer_sound_button = self.ui.findChild(QPushButton, "fajerSoundButton")
        dohor_sound_button = self.ui.findChild(QPushButton, "dohorSoundButton")
        aser_sound_button = self.ui.findChild(QPushButton, "aserSoundButton")
        magreb_sound_button = self.ui.findChild(QPushButton, "magrebSoundButton")
        ishaa_sound_button = self.ui.findChild(QPushButton, "ishaaSoundButton")
        
        
        # adans_sound_button.setFont(tajawal_bold_font_18)
        fajer_sound_button.setFont(tajawal_bold_font_18)
        dohor_sound_button.setFont(tajawal_bold_font_18)
        aser_sound_button.setFont(tajawal_bold_font_18)
        magreb_sound_button.setFont(tajawal_bold_font_18)
        ishaa_sound_button.setFont(tajawal_bold_font_18)


        # self.adansSoundButtons.append(adans_sound_button)
        self.adansSoundButtons.append(fajer_sound_button)
        self.adansSoundButtons.append(dohor_sound_button)
        self.adansSoundButtons.append(aser_sound_button)
        self.adansSoundButtons.append(magreb_sound_button)
        self.adansSoundButtons.append(ishaa_sound_button)
        

        adans_widget = self.ui.findChild(QWidget,"adansWidget") 
        if adans_widget:
            self.five_prayers = []
            for i in ["fajerWidget", "dohorWidget", "aserWidget", "magrebWidget", "ishaaWidget"]:
                self.five_prayers.append(adans_widget.findChild(QWidget, i))
        
        self.shorok = self.ui.findChild(QWidget, "shorokWidget")

        self.jomoaa_widget = self.ui.findChild(QWidget, "jomoaaWidget")

        self.next_adan_label = self.ui.findChild(QLabel, "nextAdanNameLabel")

        self.next_adan_label.setFont(Vazirmatn_Bold_font_34)

        self.remaining_text_label = self.ui.findChild(QLabel, "remaining_text_label")

        self.remaining_text_label.setFont(ReadexPro_font_28)


        self.remaining_time_label = self.ui.findChild(QLabel, "remainingTimeLabel")

        # preparing the general settings components
        self.advanced_settings_label = self.ui.findChild(QLabel, "advanced_settings_label")
        self.advanced_settings_label.setFont(Rubik_SemiBold_font_34)

        self.masjed_time_settings_label = self.ui.findChild(QLabel,"masjed_time_settings_label")
        self.masjed_time_settings_label.setFont(Rubik_SemiBold_font_34)

        self.masjed_name_label = self.ui.findChild(QLabel, "masgedNameLabel")

        self.masjed_name_label.setFont(Rubik_SemiBold_font_38)

        self.masjed_name_text_label = self.ui.findChild(QLabel, "masjed_name_text_label")
        self.masjed_name_text_label.setFont(kufi_font_24)

        self.city_text_label = self.ui.findChild(QLabel, "city_text_label")
        self.city_text_label.setFont(kufi_font_24)

        self.quds_diff_text_label = self.ui.findChild(QLabel, "quds_diff_text_label")
        self.quds_diff_text_label.setFont(kufi_font_24)

        self.sum_win_timing_label = self.ui.findChild(QLabel, "sum_win_timing_label") 
        self.sum_win_timing_label.setFont(kufi_font_24)

        self.time_format_text_label = self.ui.findChild(QLabel, "time_format_text_label")
        self.time_format_text_label.setFont(kufi_font_24)

        self.winter_settings_label = self.ui.findChild(QLabel, "winter_settings_label")
        self.winter_settings_label.setFont(kufi_font_18)

        self.summer_settings_label = self.ui.findChild(QLabel, "summer_settings_label")
        self.summer_settings_label.setFont(kufi_font_18)
        
        self.time_formate_24_label = self.ui.findChild(QLabel, "time_formate_24_label")
        self.time_formate_24_label.setFont(kufi_font_18)
        
        self.time_formate_12_label = self.ui.findChild(QLabel, "time_formate_12_label")
        self.time_formate_12_label.setFont(kufi_font_18)
        
        self.zigbee_connect_text_label = self.ui.findChild(QLabel, "zigbee_connect_text_label")
        self.zigbee_connect_text_label.setFont(kufi_font_18)

        self.connect_to_zigbee_btn = self.ui.findChild(QPushButton, "connect_to_zigbee_btn")
        self.connect_to_zigbee_btn.setFont(tajawal_bold_font_16)


        self.masjed_name_input = self.ui.findChild(QLineEdit, "masjedNameInput")
        self.masjed_name_input.setFont(kufi_font_18)

        self.city_input = self.ui.findChild(QLineEdit, "cityInput")
        self.city_input.setFont(kufi_font_18)
        
        self.time_diff_from_quds = self.ui.findChild(QSpinBox, "qudsTimeDiff")
        self.time_diff_from_quds.setFont(kufi_font_24)

        self.win_sum_frame = self.ui.findChild(QFrame, "win_sum_frame")
        self.win_sum_buttons = self.win_sum_frame.findChildren(QPushButton)

        self.time_formate_frame = self.ui.findChild(QFrame, "time_formate_frame")
        self.time_formate_buttons = self.time_formate_frame.findChildren(QPushButton)


        #  preparing the TimeManager components
        self.main_time_label = self.ui.findChild(QLabel, "clockLabel")

        self.main_time_label.setFont(ChivoMono_VariableFont_wght_font_80)

        self.gregorian_date_label = self.ui.findChild(QLabel, "dateLabel")
        self.gregorian_date_label.setFont(kufi_font_24)
        
        self.time_lower_widget = self.ui.findChild(QWidget, "timeLowerWidget")

        self.day_label = self.ui.findChild(QLabel, "dayLabel")
        self.day_label.setFont(kufi_font_24)

        self.noti_type_text_label = self.ui.findChild(QLabel, "noti_type_text_label")
        self.noti_type_text_label.setFont(kufi_font_24)

        self.before_adan_noti_label = self.ui.findChild(QLabel, "before_adan_noti_label")
        self.before_adan_noti_label.setFont(kufi_font_24)

        self.after_adan_noti_label = self.ui.findChild(QLabel, "after_adan_noti_label")
        self.after_adan_noti_label.setFont(kufi_font_24)

        self.duration_label = self.ui.findChild(QLabel, "duration_label")
        self.duration_label.setFont(kufi_font_24)

        self.date_noti_label = self.ui.findChild(QLabel, "date_noti_label")
        self.date_noti_label.setFont(kufi_font_24)

        self.permenant_noti_label = self.ui.findChild(QLabel, "permenant_noti_label")
        self.permenant_noti_label.setFont(kufi_font_18)

        self.once_noti_label = self.ui.findChild(QLabel, "once_noti_label")
        self.once_noti_label.setFont(kufi_font_18)

        self.quraan_coming_soon_label = self.ui.findChild(QLabel, "quraan_coming_soon_label")
        self.quraan_coming_soon_label.setFont(Vazirmatn_Bold_font_34)

    def intiate_adans_state_button(self):
        data = self.database_manager.get_adans_state()
        buttons_names = ["fajer_activate_button", "dohor_activate_button", "aser_activate_button", "magreb_activate_button", "ishaa_activate_button"]

        buttons = []

        tajawal_bold_font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Tajawal/Tajawal-Bold.ttf"))
        tajawal_bold_font_family = QFontDatabase.applicationFontFamilies(tajawal_bold_font_id)[0]
        tajawal_bold_font_18_temp = QFont(tajawal_bold_font_family, 18)

        for adan_data in data:
            adan_button = self.ui.findChild(QPushButton, buttons_names[adan_data[0] - 1])
            adan_button.setFont(tajawal_bold_font_18_temp)

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
            #after_adan_frame{                               
                background-color: rgb(255, 255, 255);
                }
            """)
            self.after_adan_noti_label.setStyleSheet("""
            text-decoration: none;
            color:black;
            """)
            self.before_adan_frame.setStyleSheet(""" 
            #before_adan_frame{
                background-color: rgb(240, 240, 240);                           
                }
            """)
            self.before_adan_noti_label.setStyleSheet("""
            text-decoration: line-through;
            color:black;
            """)
        else:
            self.before_adan_minutes_spin.setDisabled(False)
            self.before_adan_box.setDisabled(False)

            self.after_adan_box.setDisabled(True)
            self.after_adan_minutes_spin.setDisabled(True)

            self.reset_after_adanBox_minuteSpinBox()

            self.before_adan_frame.setStyleSheet(""" 
            #before_adan_frame{
                background-color: rgb(255, 255, 255);                              
                }
            """)
            self.before_adan_noti_label.setStyleSheet(""" 
            text-decoration: none;
            color:black;
            """)
            self.after_adan_frame.setStyleSheet(""" 
            #after_adan_frame{
                background-color: rgb(240, 240, 240);                               
                }
            """)
            self.after_adan_noti_label.setStyleSheet("""
            text-decoration: line-through;
            color:black;
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

        day_of_week = 0

        if not is_permenant:
            # date of type QDate
            date = self.noti_date.selectedDate()
            day_of_week = date.dayOfWeek()

        if self.before_adan_type_button.isChecked():
            # before adan notification
            is_before_adan = True
            adan_index = self.before_adan_box.currentIndex()
            seconds = (self.before_adan_minutes_spin.value() * 60)
        
        else:
            # after adan notification
            seconds = self.after_adan_minutes_spin.value()
            if self.after_adan_minutes_spin.suffix() != " ثواني":
                seconds *= 60
            
            is_before_adan = False
            adan_index = self.after_adan_box.currentIndex()

        self.notification_manager.handel_save_noti_button_clicked(day_of_week, is_before_adan, is_permenant, adan_index, seconds, date, duration)

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
        return self.jomoaa_widget
    
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

    def closeEvent(self, event: QEvent):
        self.runnable_manager.terminate_all_workers()
        self.runnable_manager.wait_for_done()
        event.accept()

