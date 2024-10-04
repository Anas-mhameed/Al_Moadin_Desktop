from Runnable import Runnable
from CustomDialog import CustomDialog
from PySide6.QtWidgets import QDialog
from time import sleep
from Sound import Sound
from PySide6.QtCore import QObject, Signal


class PlayerManagersignals(QObject):
    play_instant_player_signal = Signal()

class PlayerManager:

    player_manager_signals = PlayerManagersignals()
    play_instant_player = player_manager_signals.play_instant_player_signal

    def __init__(self, main_window, messager, runnable_manager):
        
        self.main_window = main_window

        self.is_adan_playing = False
        self.is_notification_playing = False
        self.is_instant_player_playing = False
        self.messager = messager
        self.runnable_manager = runnable_manager

        self.noti_runnable = ""
        self.sound = Sound()
    
    def play_adan(self, file_path):
        # play adan !!!!!!!!
        self.sound.update_file_path(file_path)
        self.sound.play()

    def get_is_adan_playing(self):
        return self.is_adan_playing

    def handle_instant_finished_signal(self):
        self.set_is_instant_player_playing(False)

    def get_is_instant_player_playing(self):
        return self.is_instant_player_playing

    def get_is_notification_playing(self):
        return self.is_notification_playing
     
    def set_player_manager_helper(self, player_manager_helper):
        self.player_manager_helper = player_manager_helper

    def turn_off_notification(self):
        self.player_manager_helper.turn_off_notification()

    def turn_off_instant_player(self):
        self.player_manager_helper.turn_off_instant_player()

    def can_instant_player_play(self):
        if self.is_adan_playing:
            return False

        elif self.is_notification_playing:
            #  close notification
            self.turn_off_notification()
            self.set_is_notification_playing(False)

        self.set_is_instant_player_playing(True)

        return self.play_instant_player.emit()

    def can_noti_play(self):
        pass

    def prepare_for_adan(self):
        self.set_is_adan_playing(True)
        self.set_is_instant_player_playing(False)
        self.set_is_notification_playing(False)
        self.turn_off_instant_player()
        self.turn_off_notification()

    def set_is_adan_playing(self, bool):
        self.is_adan_playing = bool

    def set_is_notification_playing(self, bool):
        self.is_notification_playing = bool

    def set_is_instant_player_playing(self, bool):
        self.is_instant_player_playing = bool
    
    def get_adan_time_from_manager(self, adan_index):
        return self.player_manager_helper.get_adan_time_from_manager(adan_index)
        
    def hide_msg(self, sleep_time, secondary_list = None):
        def temp_func(func):
            time_to_sleep = sleep_time
            while func() and time_to_sleep != 0:
                time_to_sleep -= 1
                sleep(1)
            if secondary_list != None :
                func = secondary_list.pop(0)
                func(*secondary_list)
            self.messager.hide()
        runnable = Runnable(temp_func)
        self.runnable_manager.runTask(runnable)
    
    def send_msg(self, error_msg, info_msg):
        self.messager.update_error_label(error_msg)
        self.messager.update_info_label(info_msg)
        self.messager.show()

    def force_stop_adan(self):
        pass

    def run(self):
        print()
        print(f"adan: {self.is_adan_playing}")
        print(f"instnat: {self.is_instant_player_playing}")
        print(f"notifiaction: {self.is_notification_playing}")