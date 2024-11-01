from Sound import Sound
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QTimer


class PlayerManagersignals(QObject):
    play_instant_player_signal = Signal()
    force_stop_instant_player_signal = Signal()
    hide_emergency_frame_signal = Signal()

    show_msg_signal = Signal(str, str, int)
    open_mic_signal = Signal()
    close_mic_signal = Signal()

class PlayerManager:

    player_manager_signals = PlayerManagersignals()
    play_instant_player = player_manager_signals.play_instant_player_signal
    force_stop_instant_player = player_manager_signals.force_stop_instant_player_signal
    hide_emergency_frame_signal = player_manager_signals.hide_emergency_frame_signal
    show_msg_signal = player_manager_signals.show_msg_signal

    open_mic_signal = player_manager_signals.open_mic_signal
    close_mic_signal = player_manager_signals.close_mic_signal

    def __init__(self, main_window):
        
        self.main_window = main_window

        self.is_adan_playing = False
        self.is_notification_playing = False
        self.is_instant_player_playing = False

        self.msg_box = QMessageBox()

        self.sound_lst = []
        

    def play_adan(self, file_path):

        self.close_msgbox()

        if len(self.sound_lst) != 0:
            self.sound_lst[0].stop()

        sound = Sound(file_path)

        sound.end_of_media_signal.connect(self.sound_finished)
        sound.media_loaded_signal.connect(sound.play)
        
        self.stop()
        
        self.sound_lst.append(sound)

        self.open_mic_signal.emit()
        sound.set_source()

    def get_is_adan_playing(self):
        return self.is_adan_playing

    def handle_instant_finished_signal(self):
        self.set_is_instant_player_playing(False)
        self.close_mic_signal.emit()

    def get_is_instant_player_playing(self):
        return self.is_instant_player_playing

    def get_is_notification_playing(self):
        return self.is_notification_playing

    def can_noti_play(self, file_path):

        self.close_msgbox()

        if not self.get_is_adan_playing():

            if self.get_is_instant_player_playing() or self.get_is_notification_playing():
                # show a msg box
                self.show_msg_box(file_path)
            else:
                self.set_is_notification_playing(True)
                sound = Sound(file_path)

                sound.end_of_media_signal.connect(self.sound_finished)
                sound.media_loaded_signal.connect(sound.play)
                
                self.stop()
                
                self.sound_lst.append(sound)
                
                self.open_mic_signal.emit()

                sound.set_source()

    def show_msg_box(self, file_path):
        self.msg_box.setWindowTitle("Confirmation")
        self.msg_box.setText("هنالك ملف صوتي قيد التشغيل,\n هل تريد تشغيل الملف الجديد ؟")
        self.msg_box.setIcon(QMessageBox.Question)

        # Add OK and Cancel buttons
        self.msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        self.msg_box.buttonClicked.connect(lambda x: self.handle_message_box_response(x, file_path))
        
        # Show the message box and wait for a user response
        self.msg_box.show()
        self.auto_close_messagebox(40000)

    def auto_close_messagebox(self, timeout):
        """Auto-close the message box after `timeout` milliseconds."""
        self.timer = QTimer()
        self.timer.timeout.connect(self.close_msgbox)  # or use message_box.close()
        self.timer.setSingleShot(True)
        self.timer.start(timeout)

    def close_msgbox(self):
        try:
            self.msg_box.button(QMessageBox.Cancel).click()
        except Exception as e:
            print(e)

    def handle_message_box_response(self, button, file_path):
        # Handle the response based on which button was clicked
        if button == self.msg_box.button(QMessageBox.Ok):

            if self.get_is_instant_player_playing():
                self.force_stop_instant_player.emit()
                self.set_is_instant_player_playing(False)

            self.set_is_notification_playing(True)
            sound = Sound(file_path)

            sound.end_of_media_signal.connect(self.sound_finished)
            sound.media_loaded_signal.connect(sound.play)

            self.stop()

            self.sound_lst.append(sound)

            self.open_mic_signal.emit()

            sound.set_source()

    def can_instant_player_play(self):

        self.close_msgbox()

        if self.get_is_adan_playing():
            self.show_msg_signal.emit("لا يمكن تشغيل ملف الصوت الفوري الان ", "الرجاء الانتظار حتى الانتهاء من الاذان", 3)
            return False

        elif self.get_is_notification_playing():
            #  close notification
            self.stop()
            self.set_is_notification_playing(False)

        self.set_is_instant_player_playing(True)
        self.open_mic_signal.emit()

        return self.play_instant_player.emit()

    def prepare_for_adan(self):
        self.set_is_adan_playing(True)
        # closing instant player if is playing
        self.set_is_instant_player_playing(False)
        self.force_stop_instant_player.emit()
        # closing noti if is playing
        if self.get_is_notification_playing():
            self.stop()

        self.set_is_notification_playing(False)
        
        self.close_mic_signal.emit()
        
        self.close_msgbox()

    def set_is_adan_playing(self, bool):
        self.is_adan_playing = bool

    def set_is_notification_playing(self, bool):
        self.is_notification_playing = bool

    def set_is_instant_player_playing(self, bool):
        self.is_instant_player_playing = bool

    def possible_fake_prepare_emitted(self):
        # if self.get_is_adan_playing() and (not self.sound_lst[0].is_playing() and not self.sound_lst[0].is_paused()):
        #     self.set_is_adan_playing(False)
        if self.get_is_adan_playing():
            self.set_is_adan_playing(False)

    def force_stop_adan(self):
        if self.get_is_adan_playing():
            self.stop()
            self.set_is_adan_playing(False)

            # emit a signal to hide emergency frame
            self.hide_emergency_frame_signal.emit()
            self.close_mic_signal.emit()

    def force_stop_notification(self):
        if self.get_is_notification_playing():
            self.stop()
            self.set_is_notification_playing(False)
            self.close_mic_signal.emit()

    def stop(self):
        if len(self.sound_lst) != 0:
            sound = self.sound_lst.pop()
            try:
                try:  
                    sound.end_of_media_signal.disconnect(self.sound_finished)
                except Exception as e:
                    print(e)
                
                sound.media_loaded_signal.disconnect(sound.play)

            except Exception as e:
                print(e)
      
            finally:
                sound.stop()

    def pause_adan(self):
        if self.get_is_adan_playing():
            if self.sound_lst[0].is_playing():
                self.sound_lst[0].pause()

    def resume_adan(self):
        if self.get_is_adan_playing():
            if self.sound_lst[0].is_paused():
                self.sound_lst[0].resume()

    def sound_finished(self):
        print("finished emitted !!!")
        if self.get_is_adan_playing():
            self.set_is_adan_playing(False)
        
        elif self.get_is_notification_playing():
            self.set_is_notification_playing(False)
        
        self.close_mic_signal.emit()
