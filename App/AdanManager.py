from Sound import Sound
from NextAdan import NextAdan
from AdanTimePrepare import AdanTimePrepare
from Adan import Adan
from PySide6.QtWidgets import QLabel, QPushButton
from PySide6.QtCore import QObject, Signal, Slot
from Runnable import Runnable, RunnableManager
from datetime import time
from ResourceFile import resource_path
from time import sleep
from datetime import datetime as dt


class AdanManagerSignals(QObject):
    
    adan_time_changed = Signal(object)
    prepare_for_adan = Signal()

    def __init__(self):
        super().__init__()
        

class AdanManager():

    adan_manager_signals = AdanManagerSignals()
    adan_time_changed = adan_manager_signals.adan_time_changed 
    prepare_for_adan_signal = adan_manager_signals.prepare_for_adan

    def __init__(self, main_widget, database_manager, runnable_manager, player_manager, five_prayers, shorok, jomoaa, adans_sound_buttons, next_adan_label, remaining_time_label, general_settings, emerg_frame, emerg_label, emerg_btn):

        self.database_manager = database_manager
        self.runnable_manager = runnable_manager 

        self.adan_time_prepare = AdanTimePrepare()
        self.general_settings = general_settings
        
        self.time_formate = ""
        self.is_summer = True
        self.quds_differ = 0

        self.wich_is_playing = None

        self.player_manager = player_manager

        self.emerg_frame = emerg_frame
        self.emerg_label = emerg_label
        self.emerg_btn = emerg_btn
        self.emerg_btn.clicked.connect(lambda: self.emergency_stop())

        # initiate defaulte sounds 
        self.fajer_sound = Sound(sound_file=resource_path("resources/sounds/azan9.mp3"))
        self.basic_sound = Sound(sound_file=resource_path("resources/sounds/azan2.mp3"))

        for button in adans_sound_buttons:
            if button.objectName() == "fajerSoundButton" :
                button.clicked.connect(lambda: self.change_fajer_sound(main_widget))
            else:
                button.clicked.connect(lambda: self.change_basic_sound(main_widget))

        self.adans = []
        self.initiate_adans(five_prayers, shorok)

        self.intiate_adans_state()

        self.jomoaa = self.intiate_jomoaa(jomoaa)
        # self.handle_summer_winter_change(True)

        self.next_adan = NextAdan(self.adans, self.set_not_adan_time, dt.now(), next_adan_label, remaining_time_label, self.start_adan, self.prepare_for_adan)
        
        self.next_adan.adan_time_signal.connect(self.start_adan)
        self.next_adan.prepare_for_adan_signal.connect(self.prepare_for_adan)

        self.update_ui()
        self.update_jomoaa_ui()

    def update_curr_time(self, updated_time):
        self.curr_time = updated_time

    def intiate_adans_state(self):
        adan_state_data = self.database_manager.get_adans_state()
        for i in range(len(self.adans)):
            self.adans[i].change_state(True if adan_state_data[i][1] else False)

    def get_current_adan_time(self, index):
        if index == 6:
            return self.jomoaa.get_adan_time()
        return self.adans[index - 1].get_adan_time()
        
    def intiate_jomoaa(self, ui_object):
        jomoaa_time = self.adan_time_prepare.get_jomoaa()
        # need completion
        # if jomoaa_time < self.curr_time.get_curr_time() :
        #     jomoaa_time = self.adan_time_prepare.get_next_jomoaa()

        jomoaa_adan = self.adan_creator(ui_object,"jomoaa",jomoaa_time)

        return jomoaa_adan

    def get_new_jomoaa(self):
        jomoaa_time = self.adan_time_prepare.get_jomoaa()
        self.jomoaa.update_original_time(jomoaa_time)

    def initiate_adans(self, five_prayers, shorok):
        adans_labels = ["fajer", "dohor", "aser", "magreb", "ishaa"]
        self.adan_time_prepare.get_current_day_adans()
        all_adans_time = self.adan_time_prepare.convert_to_dt()

        for i in range(len(five_prayers)):
            adan = self.adan_creator(five_prayers[i], adans_labels[i], all_adans_time[2][i])

            self.adans.append(adan)
            adan_button = five_prayers[i].findChild(QPushButton,f"{adans_labels[i]}_activate_button")
            adan_button.toggled.connect(adan.change_state)
        self.shorok = self.adan_creator(shorok, "shorok", all_adans_time[1])

    def adan_creator(self, ui_object, label_name, adan_time):
        adan_name_label = ui_object.findChild(QLabel, f"{label_name}_label")
        adan_time = adan_time
        adan_time_label = ui_object.findChild(QLabel, f"{label_name}_adan_time")

        return Adan(adan_name_label, adan_time, adan_time_label)

    def emergency_stop(self):
        
        if self.wich_is_playing.is_playing():
            self.wich_is_playing.pause()
            self.emerg_label.setText("لاستكمال الاذان اضغط هنا")
        else:
            self.wich_is_playing.resume()
            self.emerg_label.setText("لايقاف الاذان اضغط هنا")

    def time_to_hide_emerg_frame(self):
        def temp(func):
            sound = self.get_next_adan_sound()
            sleep(1)
            time_to_sleep = (sound.get_duration() // 1000) + 1

            while func() and time_to_sleep != 0:
                time_to_sleep -= 1
                sleep(1)
                
            self.emerg_frame_hide_helper()

        self.runnable = Runnable(temp)
        self.runnable_manager.runTask(self.runnable)
    
    def emerg_frame_hide_helper(self):
        self.emerg_frame.hide()
        self.emerg_label.setText("لايقاف الاذان اضغط هنا")

        if self.emerg_btn.isChecked():
            self.wich_is_playing.stop()
            try:
                self.runnable2.stop()
            except:
                pass
            self.player_manager.set_is_adan_playing(False)

        self.emerg_btn.setChecked(False)

    def set_not_adan_time(self):
        self.player_manager.set_is_adan_playing(False)
        self.next_adan.set_praper_for_adan_call(False)

    def start_adan(self, adan):
        if adan.get_adan_name() == "الفجر":
            self.wich_is_playing = self.fajer_sound
        else:
            self.wich_is_playing = self.basic_sound
        
        if adan.check_state():
            self.wich_is_playing.play()
            self.emerg_frame.show()
            self.time_to_hide_emerg_frame()

        def temp(func):
            sound = self.get_next_adan_sound()
            while func() and not sound.end_of_media():
                sleep(1)
            self.set_not_adan_time()

        self.runnable2 = Runnable(temp)
        self.runnable_manager.runTask(self.runnable2)

    def get_next_adan_sound(self):
        name = self.next_adan.get_next_adan_name()
        return self.fajer_sound if name == "الفجر" else self.basic_sound

    def prepare_for_adan(self):
        self.prepare_for_adan_signal.emit()

    def change_fajer_sound(self, widget):
        self.fajer_sound.select_sound_file(widget)

    def change_basic_sound(self, widget):
        self.basic_sound.select_sound_file(widget)
            
    def helper(self, adans):

        temp = self.quds_differ

        for adan in adans:
            
            
            adan_time = adan.get_original_time()
            
            hour = adan_time.hour
            minute = adan_time.minute

            temp_summer = 0
            if self.is_summer:
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

            adan.update_time(adan.get_adan_time().replace(hour=new_hour, minute=new_minute))

    def update_is_summer_time(self, is_summer):
        self.is_summer = is_summer

    def handle_summer_winter_helper(self, adan):
        
        new_hour = adan.get_adan_time().hour

        if self.is_summer :
                new_hour += 1
        else:
                new_hour -= 1

        adan_time = adan.get_adan_time()
        
        if new_hour < 0:
            new_hour += 24

        new_adan_time = adan_time.replace(hour= (new_hour) % 24)

        adan.update_time(new_adan_time)

    def handle_summer_winter_change(self, is_summer_time):
        
        self.update_is_summer_time(is_summer_time)

        for adan in self.adans:
            
            self.handle_summer_winter_helper(adan)
        
        self.handle_summer_winter_helper(self.shorok)
        self.handle_summer_winter_helper(self.jomoaa)

        self.adan_time_changed.emit(None)

        self.update_ui()
        self.update_jomoaa_ui()
    
    def update_quds_differ(self, new_quds_diff):
        self.quds_differ = new_quds_diff

    def handle_quds_diff_change(self, new_quds_differ):

        self.update_quds_differ(new_quds_differ)

        # make function
        all_adans = self.adans.copy()
        all_adans.append(self.shorok)
        all_adans.append(self.jomoaa)
   
        self.helper(all_adans)
        
        self.adan_time_changed.emit(None)

        self.update_ui()
        self.update_jomoaa_ui()

    # def check_if_jomoaa_passed(self):
    #     if self.curr_time.day == "السبت" :
    #         if self.curr_time.curr_dt.time() > time(0,0,0) and self.curr_time.curr_dt.time() < time(0,0,1):
    #             return True
    #     return False

    def get_new_adans_time(self):

        self.adan_time_prepare.get_current_day_adans()
        all_adans_time = self.adan_time_prepare.convert_to_dt()

        self.shorok.update_original_time(all_adans_time[1])

        for i in range(len(self.adans)):
            self.adans[i].update_original_time(all_adans_time[2][i])


        # activate quds differ and summer ... => wich also trigger notification update 
        
        #  check this #############################                 !!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!! ###############
        
        # is_summer_time = self.general_settings.is_summer_time
        # self.handle_quds_diff_change(self.general_settings.quds_time_diff, is_summer_time)

    def update_ui(self):
        for adan in self.adans:
            adan.update_ui(self.time_formate)

        self.shorok.update_ui(self.time_formate)

    def update_jomoaa_ui(self):
        self.jomoaa.update_ui(self.time_formate)

    def handle_new_day(self):
        
        self.get_new_adans_time()

        # update the ui 
        self.update_ui()

        # send the new prayers to next adan
        self.next_adan.update_five_prayers(self.adans)
        
        # emit a signal to update notificatins
        self.adan_time_changed.emit()

    def handle_new_jomoaa(self):
        
        self.get_new_jomoaa()

        #  update jomoaa ui
        self.update_jomoaa_ui()
        
        # emit a signal to update notificatins
        self.adan_time_changed.emit()
    
    def update_time_formate(self, new_formate):
        self.time_formate = new_formate
    
    def handle_new_time_formate(self, new_time_formate):
        self.update_time_formate(new_time_formate)
        self.update_ui()
        self.update_jomoaa_ui()
