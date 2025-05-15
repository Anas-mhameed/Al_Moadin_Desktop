from PlayAudioCommand import PlayAudioCommand

from Sound import Sound

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QTimer
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget  # Needed to keep audio backend happy
from PySide6.QtCore import QUrl

class PlayerManagersignals(QObject):
    play_instant_player_signal = Signal()
    force_stop_instant_player_signal = Signal()

    show_msg_signal = Signal(str, str, int)


    open_mic_signal = Signal()
    close_mic_signal = Signal()

class PlayerManager:

    player_manager_signals = PlayerManagersignals()
    play_instant_player = player_manager_signals.play_instant_player_signal
    force_stop_instant_player = player_manager_signals.force_stop_instant_player_signal
    show_msg_signal = player_manager_signals.show_msg_signal
    
    open_mic_signal = player_manager_signals.open_mic_signal
    close_mic_signal = player_manager_signals.close_mic_signal

    def __init__(self, main_window, emerg_frame, emerg_label, emerg_btn):
        
        self.mediator = None
        self.is_adan_near = False
        self.main_window = main_window
        self.current_command = None
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.mediaStatusChanged.connect(lambda status : self._on_status_changed(status))
        self.player.playbackStateChanged.connect(self.on_state_changed)

        self.emerg_frame = emerg_frame
        self.emerg_label = emerg_label
        self.emerg_btn = emerg_btn
        self.emerg_btn.clicked.connect(lambda: self._emergency_stop())

        self.cleanup_timer = QTimer()
        self.cleanup_timer.setInterval(20 * 1000)  # 40 secounds
        self.cleanup_timer.setSingleShot(True)
        self.cleanup_timer.timeout.connect(self._stop_current)

        self.is_adan_playing = False
        self.is_notification_playing = False
        self.is_instant_player_playing = False

        self.msg_box = QMessageBox()

        self.sound_lst = []

    def on_state_changed(self, state):
        if state == QMediaPlayer.PausedState:
            self.cleanup_timer.start()
        elif state == QMediaPlayer.PlayingState:
            if self.cleanup_timer.isActive():
                self.cleanup_timer.stop()
        elif state == QMediaPlayer.StoppedState:
            self.cleanup_timer.stop()
            if self.current_command.requester == "AdanManager":
                self._hide_emerg_frame()
            self._clear_command()

    def _clear_command(self):
        self.current_command = None # indicates that no one is playing
        
    # def _stop_adan(self):
    #     self._stop_current()
    #     self._hide_emerg_frame()

    def _on_status_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            pass

    def _emergency_stop(self):
        if self.emerg_btn.isChecked():
            self._pause()
            self.emerg_label.setText("لاستكمال الأذان إضغط هنا ")
        else:
            self._resume()
            self.emerg_label.setText("لإيقاف الأذان إضغط هنا")

    def _show_emerg_frame(self):
        self.emerg_frame.show()

    def _hide_emerg_frame(self):
        self.emerg_frame.hide()
        self.emerg_label.setText("لإيقاف الأذان إضغط هنا")
        self.emerg_btn.setChecked(False)

    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    def request_playback(self, command: PlayAudioCommand):
        if command.requester == "AdanManager":
            self._play(command) 
            self._show_emerg_frame()
        else:
            if not self.is_adan_near:

                if command.requester == "InstantPlayer":
                    
                    if self.current_command is None or self.current_command.requester == "NotificationsManager" or self.current_command.requester == "InstantPlayer":
                        self._play(command)
                    
                    elif self.current_command.requester == "AdanManager":
                        # show an error message
                        pass

    def isPlaying(self):
        return self.player.isPlaying()
    
    def _resume(self):
        self.player.play()

    def _pause(self):
        self.player.pause()

    def _play(self, command):
        self.current_command = command
        url = QUrl.fromLocalFile(command.file_path)
        if self.player.source() == url:
            self.player.setPosition(0)
        else:
            self.player.setSource(url)
        self.player.play()

    def _stop_current(self):
        self.player.stop()

    def pause_instant_player(self):
        if self.current_command and self.current_command.requester == "InstantPlayer" and self.player.playbackState() == QMediaPlayer.PlayingState:
            self._pause()

    def resume_instant_player(self):
        if self.current_command and self.current_command.requester == "InstantPlayer" and self.player.playbackState() == QMediaPlayer.PausedState:
            self._resume()

    def stop_instant_player(self):
        if self.current_command and self.current_command.requester == "InstantPlayer" and (self.player.playbackState() == QMediaPlayer.PlayingState or self.player.playbackState() == QMediaPlayer.PausedState):
            self._stop_current()

    def prepare_for_adan(self):
        if not self.is_adan_near :
            self.is_adan_near = True
            self._stop_current()

    def  allow_playback(self):
        if self.is_adan_near:
            self.is_adan_near = False

    def current_adan_changed_to_previous(self):
        if self.current_command and self.current_command.requester == "AdanManager" and self.isPlaying():
            self._stop_current()