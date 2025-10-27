from helper_functions import select_sound_file

from PlayAudioCommand import PlayAudioCommand

from NextAdan import NextAdan
from AdanTimePrepare import AdanTimePrepare
from Adan import Adan
from PySide6.QtWidgets import QLabel, QPushButton, QSlider
from PySide6.QtCore import QObject, Signal
import datetime as dt
from ResourceFile import resource_path
from DatabaseManager import DatabaseManager  # Import DatabaseManager directly
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtCore import QUrl

adan_db_names = [
            "fajer_adan",
            "dohor_adan",
            "aser_adan",
            "magreb_adan",
            "ishaa_adan"
        ]

class AdanManagerSignals(QObject):
    
    prepare_for_adan = Signal()
    get_settings_signal = Signal()
    adan_sound_changed = Signal()
    find_next_adan_signal = Signal()
    force_stop_adan_signal = Signal()
    play_adan_signal = Signal(str)
    fajer_duartion_signal = Signal(int)
    basic_duartion_signal = Signal(int)
    # stop_adan_signal = Signal()
    pause_adan_signal = Signal()
    resume_adan_signal = Signal()


    possible_not_adan_time_signal = Signal()

    def __init__(self):
        super().__init__()
        

class AdanManager():

    adan_manager_signals = AdanManagerSignals()
    prepare_for_adan_signal = adan_manager_signals.prepare_for_adan
    get_settings_signal = adan_manager_signals.get_settings_signal
    
    adan_sound_changed = adan_manager_signals.adan_sound_changed

    find_next_adan_signal = adan_manager_signals.find_next_adan_signal
    force_stop_adan_signal = adan_manager_signals.force_stop_adan_signal
    play_adan_signal = adan_manager_signals.play_adan_signal
    fajer_duartion_signal = adan_manager_signals.fajer_duartion_signal
    basic_duartion_signal = adan_manager_signals.basic_duartion_signal

    # stop_adan_signal = adan_manager_signals.stop_adan_signal
    pause_adan_signal = adan_manager_signals.pause_adan_signal
    resume_adan_signal = adan_manager_signals.resume_adan_signal

    possible_not_adan_time_signal = adan_manager_signals.possible_not_adan_time_signal

    def __init__(self, main_widget, five_prayers, shorok, jomoaa, adans_sound_buttons, next_adan_label, remaining_time_label):

        self.database_manager = DatabaseManager()  # Initialize DatabaseManager directly

        self.curr_time = dt.datetime.now()

        self.adan_time_prepare = AdanTimePrepare()
        
        self.mediator = None

        self.time_formate = "%H:%M"

        self.main_widget = main_widget

        for button in adans_sound_buttons:
            button_name = button.objectName()
            button.clicked.connect(lambda checked=False, btn_name=button_name: self.change_adan_sound(btn_name))


        self.adans = []
        self.adans_buttons = []
        self.adans_volume_sliders = []

        self.initiate_adans(five_prayers, shorok)

        self.intiate_adans_state()

        self.jomoaa = self.intiate_jomoaa(jomoaa)

        self.next_adan = NextAdan(self.adans, next_adan_label, remaining_time_label)
        self.next_adan.update_adan_times_signal.connect(self.handle_new_day)
        self.find_next_adan_signal.connect(self.next_adan.intiate_next_adan)

        self.next_adan.adan_time_signal.connect(self.start_adan)
        self.next_adan.force_stop_adan.connect(self.force_stop_adan)

        self.update_ui()
        self.update_jomoaa_ui()

    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator
        self.next_adan.set_mediator(mediator)

    def get_adans_duration(self):
        for adan in self.adans:
            self.calc_audio_duration(adan.get_sound_path(), self.adans.index(adan) + 1)
        
        # #  should send jomoaa sound file
        # self.calc_audio_duration(self.adans[1].get_sound_path(), 6)

    def calc_audio_duration(self, file_path, adan_index):
        temp_player = QMediaPlayer()
        audio_output = QAudioOutput()
        temp_player.setAudioOutput(audio_output)

        def on_duration_changed(duration):
            if duration > 0:
                temp_player.durationChanged.disconnect(on_duration_changed)
                temp_player.deleteLater()
                audio_output.deleteLater()

                # Now adan_index is already an integer (1-5)
                self.mediator.notify(self, "audio_duration_changed", duration, adan_index)

                # this should be remove when jomoaa sound file is added to ui
                # if adan_index == 2:
                #     self.mediator.notify(self, "audio_duration_changed", duration, 6)
                

        temp_player.durationChanged.connect(on_duration_changed)
        temp_player.setSource(QUrl.fromLocalFile(file_path))

    def force_stop_adan(self):
        self.force_stop_adan_signal.emit()

    def request_settings(self):
        if self.mediator:
            self.mediator.notify(self, "request_general_settings")

    def update_curr_time(self, updated_time):
        self.curr_time = updated_time

    def intiate_adans_state(self):
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("adan_state_change", "loading", "retrieving_states", "Loading adan states from database")

        adan_state_data = self.database_manager.get_adans_state()
        
        for i in range(len(self.adans)):
            old_state = self.adans[i].check_state()
            new_state = True if adan_state_data[i][1] else False
            self.adans[i].change_state(new_state)
            
            if hasattr(self, 'mediator') and self.mediator:
                old_state_text = "enabled" if old_state else "disabled"
                new_state_text = "enabled" if new_state else "disabled"
                self.mediator.log("adan_state_change", old_state_text, new_state_text, 
                                f"{self.adans[i].get_adan_name()} loaded from DB")

    def get_current_adan_time(self, index):
        if index == 6:
            return self.jomoaa.get_adan_time()
        return self.adans[index - 1].get_adan_time()
        
    def intiate_jomoaa(self, ui_object):
        jomoaa_time = self.adan_time_prepare.get_jomoaa()
        jomoaa_adan = self.adan_creator(ui_object,"jomoaa",jomoaa_time)
        return jomoaa_adan

    def get_new_jomoaa(self):
        jomoaa_time = self.adan_time_prepare.get_jomoaa()
        self.jomoaa.update_original_time(jomoaa_time)

        if self.mediator:
            self.mediator.notify(self, "request_general_settings")

    def initiate_adans(self, five_prayers, shorok):
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("adan_state_change", "uninitialized", "initializing_adans", "Loading 5 daily prayers")

        adans_labels = ["fajer", "dohor", "aser", "magreb", "ishaa"]
        self.adan_time_prepare.get_current_day_adans()
        all_adans_time = self.adan_time_prepare.convert_to_dt()
        
        sound_data = self.database_manager.get_adans_sound()
        
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("adan_state_change", "loading", "sound_data_retrieved", 
                            f"Loaded {len(sound_data)} adan sound configurations")
        
        for i in range(len(five_prayers)):
            adan = self.adan_creator(five_prayers[i], adans_labels[i], all_adans_time[2][i])
            sound_path = resource_path(sound_data[i][1])
            adan.set_sound_path(sound_path)
            volume = sound_data[i][2] if len(sound_data[i]) > 2 else 50
            adan.set_volume(volume)
            
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("adan_state_change", "created", "adan_configured", 
                                f"{adans_labels[i]} - Time: {all_adans_time[2][i].strftime('%H:%M')}, Volume: {volume}%, Sound: {sound_path}")
            
            self.adans.append(adan)
            self.connect_adan_to_activate_button(five_prayers[i], adan, adans_labels[i])
            self.connect_adan_to_slider(adan, adans_labels[i], i)

        self.shorok = self.adan_creator(shorok, "shorok", all_adans_time[1])
        
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("adan_state_change", "initializing", "adans_initialized", 
                            f"All 5 prayers + Shorok configured successfully")

    def connect_adan_to_activate_button(self, prayer, adan, adan_label):
        adan_button = prayer.findChild(QPushButton, f"{adan_label}_activate_button")
        adan_button.toggled.connect(adan.change_state)
        self.adans_buttons.append(adan_button)

    def connect_adan_to_slider(self, adan, adan_label, adan_index):
        # Find and connect volume slider if it exists
        volume_slider = self.main_widget.findChild(QSlider, f"{adan_label}_volume_slider")
        self.adans_volume_sliders.append(volume_slider)
        if volume_slider:
            # Set the slider value to the adan's volume
            volume_slider.setValue(adan.get_volume())
            volume_slider.valueChanged.connect(lambda value, a=adan, idx=adan_index: self.handle_volume_change(value, a, idx))

    def handle_volume_change(self, value, adan, adan_index):
        old_volume = adan.get_volume()
        adan.set_volume(value)
        
        # Log volume change
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("volume_change", 
                             adan.get_adan_name(), 
                             old_volume, 
                             value)
        
        if 0 <= adan_index < len(adan_db_names):
            self.database_manager.update_adans_sound(adan_db_names[adan_index], new_volume=value)
            
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("adan_state_change", "volume_updated", "database_saved", 
                                f"{adan.get_adan_name()} volume saved to DB")
        
        if self.mediator:
            self.mediator.notify(self, "adan_volume_changed", adan.get_adan_name(), value)

    def adan_creator(self, ui_object, label_name, adan_time):
        adan_name_label = ui_object.findChild(QLabel, f"{label_name}_label")
        adan_time = adan_time
        adan_time_label = ui_object.findChild(QLabel, f"{label_name}_adan_time")

        return Adan(adan_name_label, adan_time, adan_time_label)

    def start_adan(self, adan):
        # Log adan start attempt with all details
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("adan_play", 
                             adan.get_adan_name(), 
                             adan.get_sound_path(), 
                             adan.get_volume())
            self.mediator.log("adan_state_change", 
                             "waiting", 
                             "adan_triggered", 
                             f"{adan.get_adan_name()} - State: {adan.check_state()}")

        if adan.check_state():
            command = PlayAudioCommand("AdanManager", adan.get_sound_path(), adan.get_volume(), adan.get_adan_name())
            self.mediator.notify(self, "request_playback", command)
            
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("adan_play", adan.get_adan_name(), "playback_requested", "Command sent to PlayerManager")
        else:
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("adan_state_change", "enabled", "disabled", 
                                f"{adan.get_adan_name()} - Adan is turned off")
            self.mediator.notify(self, "close_mic")

    def change_adan_sound(self, adan_name):
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("adan_state_change", "current_sound", "changing_sound", f"User changing {adan_name}")

        try:
            file_path = select_sound_file(self.main_widget)
            if not file_path:
                if hasattr(self, 'mediator') and self.mediator:
                    self.mediator.log("adan_state_change", "changing_sound", "cancelled", f"{adan_name} - No file selected")
                return

            path = resource_path(file_path)
            
            adan_index_map = {
                "fajerSoundButton": 0,
                "dohorSoundButton": 1, 
                "aserSoundButton": 2,
                "magrebSoundButton": 3,
                "ishaaSoundButton": 4
            }

            if adan_name in adan_index_map:
                adan_index = adan_index_map[adan_name]
                old_path = self.adans[adan_index].get_sound_path()
                
                self.update_sound(adan_index, path)
                
                if hasattr(self, 'mediator') and self.mediator:
                    self.mediator.log("adan_state_change", "sound_changed", "updated_successfully", 
                                    f"{self.adans[adan_index].get_adan_name()} - New file: {path}")
                
                self.calc_audio_duration(path, adan_index + 1)

            if self.mediator:
                adan_display_names = {
                    "fajerSoundButton": "الفجر",
                    "dohorSoundButton": "الظهر", 
                    "aserSoundButton": "العصر",
                    "magrebSoundButton": "المغرب",
                    "ishaaSoundButton": "العشاء"
                }
                display_name = adan_display_names.get(adan_name, adan_name)
                self.mediator.notify(self, "sound_updated_successfully", f"تم تحديث صوت أذان {display_name} بنجاح")

        except Exception as e:
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("error", "AdanManager", f"Failed to change adan sound for {adan_name}: {str(e)}")

    def update_sound(self, adan_index, file_path):
        self.adans[adan_index].set_sound_path(file_path)
        self.database_manager.update_adans_sound(adan_db_names[adan_index], file_path)

    def change_pre_adan_sound(self):
        """Allow user to select a pre-adhan sound file"""

        try:
            file_path = select_sound_file(self.main_widget)

            if not file_path:  # Check if a file was selected
                return

            path = resource_path(file_path)

            # Update pre-adhan sound in database
            self.database_manager.update_pre_adan_sound(file_path=path)

            # Show success message
            if self.mediator:
                self.mediator.notify(self, "sound_updated_successfully", "تم تحديث صوت ما قبل الأذان بنجاح")

        except Exception as e:
            import traceback
            traceback.print_exc()

    def test_pre_adan_mediator(self):
        """Test method to verify mediator notification works"""

        if self.mediator:
            self.mediator.notify(self, "sound_updated_successfully", "اختبار إشعار صوت ما قبل الأذان")

    def set_pre_adan_sound_direct(self, file_path):
        """Set pre-adhan sound directly without file dialog (for testing)"""

        try:
            if not file_path:
                return

            path = resource_path(file_path)

            # Update pre-adhan sound in database
            self.database_manager.update_pre_adan_sound(file_path=path)

            # Show success message
            if self.mediator:
                self.mediator.notify(self, "sound_updated_successfully", "تم تحديث صوت ما قبل الأذان بنجاح")

        except Exception as e:
            import traceback
            traceback.print_exc()

    def toggle_pre_adan_sound(self, enabled):
        """Enable or disable pre-adhan sound"""
        self.database_manager.update_pre_adan_sound(is_enabled=enabled)

        status = "تم تفعيل" if enabled else "تم إلغاء"
        if self.mediator:
            self.mediator.notify(self, "sound_updated_successfully", f"{status} صوت ما قبل الأذان")

    def set_pre_adan_volume(self, volume):
        """Set pre-adhan sound volume"""
        self.database_manager.update_pre_adan_sound(volume=volume)

        if self.mediator:
            self.mediator.notify(self, "sound_updated_successfully", f"تم تحديث مستوى صوت ما قبل الأذان إلى {volume}%")

    def helper(self, adans, new_quds_diff, is_summer):

        temp = new_quds_diff

        for adan in adans:
            
            adan_time = adan.get_original_time()
            
            hour = adan_time.hour
            minute = adan_time.minute

            temp_summer = 0
            if is_summer:
                temp_summer = 1

            if temp < 0:
                temp_hour = (temp * (-1)) // 60
                temp_minute = (temp * (-1)) % 60

                new_hour = hour - temp_hour + temp_summer
                if new_hour < 0:
                    new_hour += 24

                new_minute = minute - temp_minute
                if new_minute < 0:
                    new_hour -= 1
                    new_minute += 60 
                if new_hour < 0:
                    new_hour += 24
            else :

                temp_hour = temp // 60

                temp_minute = temp % 60

                total_minute = temp_minute + minute

                new_hour = (hour + temp_hour + (total_minute // 60) + temp_summer) % 24
                new_minute = total_minute % 60

            adan.update_time(adan.get_original_time().replace(hour=new_hour, minute=new_minute, ))

    def handle_summer_winter_helper(self, adan, is_summer):
        
        new_hour = adan.get_adan_time().hour

        if is_summer :
                new_hour += 1
        else:
                new_hour -= 1

        adan_time = adan.get_adan_time()
        
        if new_hour < 0:
            new_hour += 24

        new_adan_time = adan_time.replace(hour= (new_hour) % 24)

        adan.update_time(new_adan_time)

    def handle_summer_winter_change(self, is_summer_time):
        if hasattr(self, 'mediator') and self.mediator:
            season = "summer" if is_summer_time else "winter"
            self.mediator.log("adan_state_change", "season_change", f"switched_to_{season}", "Time adjustment applied")

        for adan in self.adans:
            self.handle_summer_winter_helper(adan, is_summer_time)
        
        self.handle_summer_winter_helper(self.shorok, is_summer_time)
        self.handle_summer_winter_helper(self.jomoaa, is_summer_time)

        self.mediator.notify(self, "adan_time_changed", self.get_adans_for_notification_manager())
        self.find_next_adan_signal.emit()
        self.update_ui()
        self.update_jomoaa_ui()
    
    def group_adans(self):
        temp = self.adans.copy()
        temp.append(self.shorok)
        temp.append(self.jomoaa)

        return temp

    def handle_quds_diff_change(self, new_quds_differ, is_summer_time):
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("adan_state_change", "time_adjustment", "quds_diff_changed", 
                            f"New difference: {new_quds_differ} min, Summer time: {is_summer_time}")

        all_adans = self.group_adans()
        self.helper(all_adans, new_quds_differ, is_summer_time)
        
        # Log updated times
        if hasattr(self, 'mediator') and self.mediator:
            updated_times = {}
            for adan in self.adans:
                updated_times[adan.get_adan_name()] = adan.get_adan_time().strftime('%H:%M')
            self.mediator.log("adan_times", updated_times)

        self.mediator.notify(self, "adan_time_changed", self.get_adans_for_notification_manager())
        self.find_next_adan_signal.emit()
        self.update_ui()
        self.update_jomoaa_ui()

    def get_new_adans_time(self):

        self.adan_time_prepare.get_current_day_adans()
        all_adans_time = self.adan_time_prepare.convert_to_dt()

        self.shorok.update_original_time(all_adans_time[1])

        for i in range(len(self.adans)):
            self.adans[i].update_original_time(all_adans_time[2][i])

        if self.mediator:
            self.mediator.notify(self, "request_general_settings")

    def update_ui(self):
        for adan in self.adans:
            adan.update_ui(self.time_formate)

        self.shorok.update_ui(self.time_formate)

    def update_jomoaa_ui(self):
        self.jomoaa.update_ui(self.time_formate)

    def handle_new_day(self, new_day):
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("adan_state_change", "previous_day", "new_day", f"Day changed to: {new_day}")

        self.get_new_adans_time()
        self.update_ui()
        self.next_adan.update_five_prayers(self.adans)
        
        if hasattr(self, 'mediator') and self.mediator:
            # Log new adan times
            adan_times_dict = {}
            for adan in self.adans:
                adan_times_dict[adan.get_adan_name()] = adan.get_adan_time().strftime('%H:%M')
            self.mediator.log("adan_times", adan_times_dict)

        self.mediator.notify(self, "adan_time_changed", self.get_adans_for_notification_manager())
        self.next_adan.update_curr_day(new_day)

    def handle_new_jomoaa(self):
        
        self.get_new_jomoaa()

        #  update jomoaa ui
        self.update_jomoaa_ui()
        
        # notify mediator to update notificatins
        self.mediator.notify(self, "adan_time_changed", self.get_adans_for_notification_manager())
    
    def update_time_formate(self, new_formate):
        self.time_formate = new_formate

    def handle_new_time_formate(self, new_time_formate):
        self.update_time_formate(new_time_formate)
        self.update_ui()
        self.update_jomoaa_ui()

    def get_adans_for_notification_manager(self):
        lst = []
        for i in range(1,7):
            lst.append(self.get_current_adan_time(i))
        return lst

    # HERE FIRESTORE UPDATES
    def set_adan_state(self, adans_data):
        labels = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
        for i in range(5):
            adan_info = adans_data[labels[i]]
            self.adans_buttons[i].setChecked(adan_info["state"])
            self.adans_volume_sliders[i].setValue(adan_info["volume"])
            
            
