from Sound import Sound
from PySide6.QtCore import QObject, Signal

class InstantPlayersignals(QObject):
    
    can_I_play_signal = Signal()
    finished_signal = Signal()

    show_msg_signal = Signal(str, str, int)


class InstantPlayer:

    instant_player_signals = InstantPlayersignals()
    can_I_play = instant_player_signals.can_I_play_signal
    finished_signal = instant_player_signals.finished_signal
    show_msg_signal = instant_player_signals.show_msg_signal

    def __init__(self, main_widget, player_manager, choose_file_button, delete_file_button, position_controller, play_button, pause_button, resume_button, stop_button):

        self.player_manager = player_manager

        self.main_widget = main_widget

        self.file_path = ""

        self.sound_lst = []
        
        self.choose_file_button = choose_file_button
        self.delete_file_button = delete_file_button

        self.position_controller = position_controller
        self.position = self.position_controller.value()

        self.play_button = play_button
        self.pause_button = pause_button
        self.resume_button = resume_button
        self.stop_button = stop_button

        self.choose_file_button.clicked.connect(lambda: self.choose_sound(self.main_widget))
        self.delete_file_button.clicked.connect(lambda: self.delete_sound())

        self.play_button.clicked.connect(lambda: self.ask_player_manager_to_play())
        self.pause_button.clicked.connect(lambda: self.pause())
        self.resume_button.clicked.connect(lambda: self.resume())
        self.stop_button.clicked.connect(lambda: self.stop())

        self.position_controller.sliderMoved.connect(lambda: self.handle_position_change())
        self.position_controller.sliderPressed.connect(self.stop_slider_update)
        self.position_controller.sliderReleased.connect(self.resume_slider_update)

    def choose_sound(self, widget):

        sound = Sound()
        sound.select_sound_file(widget)
        
        self.file_path = sound.get_file_path()
    
    def delete_sound(self):
        self.file_path = ""
    
    def enable(self, btn):
        btn.setEnabled(True)

    def disable(self, btn):
        btn.setEnabled(False)

    def ask_player_manager_to_play(self):
        if self.file_path == "" :
            
            msg = "لا يوجد ملف صوتي"  

            self.show_msg_signal.emit(msg, "", 3)     

        else:
            # if self.sound_lst[0].is_playing():
            #     self.stop()

            self.can_I_play.emit()

    def play(self):
        
        if len(self.sound_lst) != 0:

            sound = self.sound_lst[0]
    
            if sound.get_file_path() == self.file_path:
                sound.play()
                return
            else:
                self.stop_helper()

        sound = Sound(self.file_path)
        self.sound_lst.append(sound)
        sound.track_media_position(self.set_position_controller)
        sound.media_loaded_signal.connect(self.set_position_controller_range)
        sound.media_loaded_signal.connect(self.player_helper)
        sound.end_of_media_signal.connect(self.handle_end_of_media)  
        
        sound.set_source()

    def player_helper(self):
        sound = self.sound_lst[0]
        
        sound.media_loaded_signal.disconnect(self.player_helper)
        sound.play()

    def pause(self):
        if len(self.sound_lst) != 0:
            self.sound_lst[0].pause()

    def resume(self):    
        if len(self.sound_lst) != 0:
            self.sound_lst[0].resume()

    def stop_helper(self):
        if len(self.sound_lst) != 0:

            sound = self.sound_lst[0]

            try:
                sound.end_of_media_signal.disconnect(self.handle_end_of_media)
                sound.media_loaded_signal.disconnect(self.set_position_controller_range)
                # sound.media_loaded_signal.disconnect(self.player_helper)
            except Exception as e:
                print(e)
            
            sound.stop()
            
            sound = self.sound_lst.pop()

            self.position_controller.setValue(0)

    def stop(self):
        # if len(self.sound_lst) != 0:
        self.stop_helper()

        self.finished_signal.emit()

    def handle_end_of_media(self):
        self.stop()
        self.set_position_controller_range()

    def handle_position_change(self):
        self.position = self.position_controller.value()
        if len(self.sound_lst) != 0:
            self.sound_lst[0].set_position(self.position)

    def set_position_controller(self, value):
        self.position_controller.setValue(value)

    def set_position_controller_range(self):
        if len(self.sound_lst) == 0:
            duration = 100
        else:
            duration = self.sound_lst[0].get_duration()

        self.position_controller.setRange(0, duration)

    def stop_slider_update(self):
        if len(self.sound_lst) != 0 :
            """Stop updating the slider during manual user interaction."""
            try:
                self.sound_lst[0].disconnect_media_position(self.set_position_controller)
            except Exception as e:
                print(e)

    def resume_slider_update(self):
        if len(self.sound_lst) != 0:
            """Resume updating the slider after manual user interaction."""
            self.sound_lst[0].track_media_position(self.set_position_controller)

    def turn_off(self):
        self.stop()
        self.delete_sound()
