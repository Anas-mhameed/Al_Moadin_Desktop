from AudioPriority import AudioPriority
from PlayAudioCommand import PlayAudioCommand
from helper_functions import select_sound_file
from PySide6.QtCore import QObject, Signal

class InstantPlayer:

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
        self.pause_button.clicked.connect(lambda: self.ask_to_pause())
        self.resume_button.clicked.connect(lambda: self.ask_to_resume())
        self.stop_button.clicked.connect(lambda: self.ask_to_stop())

        self.position_controller.sliderMoved.connect(lambda: self.handle_position_change())
        self.position_controller.sliderPressed.connect(self.stop_slider_update)
        self.position_controller.sliderReleased.connect(self.resume_slider_update)

    def choose_sound(self, widget):
        self.file_path = select_sound_file(widget)
    
    def delete_sound(self):
        self.file_path = ""
    
    def enable(self, btn):
        btn.setEnabled(True)

    def disable(self, btn):
        btn.setEnabled(False)

    def ask_player_manager_to_play(self):
        self.player_manager.request_playback(PlayAudioCommand("InstantPlayer", self.file_path))

    def ask_to_pause(self):
        self.player_manager.pause_instant_player()

    def ask_to_resume(self):    
        self.player_manager.resume_instant_player()

    def ask_to_stop(self):
        self.player_manager.stop_instant_player()

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
