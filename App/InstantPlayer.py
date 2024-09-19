from Sound import Sound
from Runnable import Runnable
from time import sleep

class InstantPlayer:

    def __init__(self, runnable_manager, main_widget, player_manager, choose_file_button, delete_file_button, position_controller, play_button, pause_button, resume_button, stop_button):
        
        self.runnable_manager = runnable_manager
        self.player_manager = player_manager

        self.main_widget = main_widget

        self.sound = Sound()
        
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

        self.play_button.clicked.connect(lambda: self.play())
        self.pause_button.clicked.connect(lambda: self.pause())
        self.resume_button.clicked.connect(lambda: self.resume())
        self.stop_button.clicked.connect(lambda: self.stop())

        # self.position_controller.valueChanged.connect(lambda: self.handle_position_change())
        self.sound.track_media_duration(self.set_position_controller_range)
        self.sound.track_media_position(self.set_position_controller)
        self.position_controller.sliderMoved.connect(lambda: self.handle_position_change())
        self.position_controller.sliderPressed.connect(self.stop_slider_update)
        self.position_controller.sliderReleased.connect(self.resume_slider_update)

    def choose_sound(self, widget):
        self.sound.select_sound_file(widget)
    
    def delete_sound(self):
        self.stop()
        self.sound.removeSound()
    
    def enable(self, btn):
        btn.setEnabled(True)

    def disable(self, btn):
        btn.setEnabled(False)

    def play(self):

        if self.sound.check_path_is_empty():
            msg = "لا يوجد ملف صوتي" 
            self.player_manager.send_msg(msg, "")
            self.disable(self.play_button)

            self.player_manager.hide_msg(3, [self.enable , self.play_button])

        else:
            if self.player_manager.can_instant_player_play():
                # if self.sound.is_playing():
                #     self.stop()
                try:
                    self.stop()
                except:
                    pass

                def temp(func):
                    sleep(1)
                    self.sound.set_volume(100)
                    self.set_position_controller(0)
                    self.player_manager.set_is_instant_player_playing(True)
                    self.sound.play()
                self.runnable_manager.runTask(Runnable(temp))
                # self.sound.play()
                
                def temp(func):
                    while func() and not self.sound.end_of_media():
                        sleep(0.5)
                    self.sound.stop()
                    self.player_manager.set_is_instant_player_playing(False)

                self.runnable = Runnable(temp)
                self.runnable_manager.runTask(self.runnable)

            else:
                self.player_manager.send_msg("لا يمكن تشغيل ملف الصوت الفوري الان ", "الرجاء الانتظار حتى الانتهاء من الاذان")
                self.disable(self.play_button)
                self.player_manager.hide_msg(5, [self.enable , self.play_button])

    def pause(self):
        self.sound.pause()

    def resume(self):
        self.sound.resume()
    
    def stop(self):
        try:
            self.runnable.stop()
        except:
            pass
        self.sound.stop()
        self.sound.set_position(0)
        self.position_controller.setValue(0)
        self.player_manager.set_is_instant_player_playing(False)
    
    def handle_position_change(self):
        self.position = self.position_controller.value()
        self.sound.set_position(self.position)

    def set_position_controller(self, value):
        self.position_controller.setValue(value)

    def set_position_controller_range(self):
        self.position_controller.setRange(0, self.sound.get_duration())
    
    def stop_slider_update(self):
        """Stop updating the slider during manual user interaction."""
        self.sound.disconnect_media_position(self.set_position_controller)

    def resume_slider_update(self):
        """Resume updating the slider after manual user interaction."""
        self.sound.track_media_position(self.set_position_controller)

    def turn_off(self):
        self.stop()
        self.delete_sound()
