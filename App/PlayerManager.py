from PlayAudioCommand import PlayAudioCommand
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QTimer
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon

class PlayerManagersignals(QObject):
    position_signal = Signal(int)
    duration_signal = Signal(int)

class PlayerManager:

    player_manager_signals = PlayerManagersignals()
    position_signal = player_manager_signals.position_signal
    duration_signal = player_manager_signals.duration_signal

    def __init__(self, volume_off_on_btn, main_window):

        self.mediator = None
        self.is_adan_near = False
        self.main_window = main_window
        self.current_command = None
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.playbackStateChanged.connect(self.on_state_changed)

        self.volume_off_on_btn = volume_off_on_btn
        self.volume_off_on_btn.setChecked(False)
        self.volume_off_on_btn.toggled.connect(self.toggle_volume)

        self.is_player_muted = False

        self.pre_adan_sound_path = "./resources/pre_adan_sound/notification-smooth-modern-stereo.mp3"

        self.is_pre_adan_sound_activated = False
        
        self.position_timer = QTimer()
        self.position_timer.timeout.connect(self._emit_position)

        self.player.durationChanged.connect(self._emit_duration)

        self.pending_command = None
        self.waiting_to_set_source = False

        self.msg_box = QMessageBox()

        self.sound_lst = []
    
    def set_position(self, position_ms: int):
        if self.current_command and self.current_command.requester == "InstantPlayer":
            self.player.setPosition(position_ms)

    def _emit_position(self):
        if self.current_command and self.current_command.requester == "InstantPlayer" and self.isPlaying():
            pos = self.player.position() # in ms
            self.position_signal.emit(pos)

    def _emit_duration(self, duartion):
        if self.current_command and self.current_command.requester == "InstantPlayer":
            self.duration_signal.emit(duartion) # in ms

    def toggle_volume(self, checked):
        if checked:
            self.audio_output.setVolume(0.0)
            self.is_player_muted = True
            self.volume_off_on_btn.setIcon(QIcon("resources/images/mute.png"))
        else:
            if self.current_command:
                self.audio_output.setVolume(self.current_command.volume / 100.0)
            else:
                self.audio_output.setVolume(1.0)
            self.is_player_muted = False
            self.volume_off_on_btn.setIcon(QIcon("resources/images/volume.png"))

    def on_state_changed(self, state):
        if state == QMediaPlayer.StoppedState:
            if self.current_command.requester == "QuraanPageManager":
                self.mediator.notify(self, "quraan_audio_finished", self.current_command.index, self.current_command.adan_name)
            elif self.current_command.requester == "NotificationManager":
                if hasattr(self, 'duration_timer') and self.duration_timer.isActive():
                    self.duration_timer.stop()
            elif self.current_command.requester == "InstantPlayer":
                self.position_timer.stop()
                self.position_signal.emit(0)

            if self.waiting_to_set_source and self.pending_command:
                command = self.pending_command
                self.pending_command = None
                self.waiting_to_set_source = False

                # Delay playback slightly to avoid FFmpeg/Qt bug
                QTimer.singleShot(0, lambda: QTimer.singleShot(100, lambda: self._play(command)))
            else:
                id = self.current_command.adan_name if self.current_command.adan_name else None
                self.mediator.notify(self, "audio_finished", self.current_command.requester, id)
                self._clear_command()

    def _clear_command(self):
        self.current_command = None # indicates that no one is playing
 
    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    def set_pre_adan_sound_state(self, state):
        self.is_pre_adan_sound_activated = state

    def start_pre_adan_sound(self):
        if self.is_pre_adan_sound_activated:
            self.request_playback(PlayAudioCommand("NextAdan", self.pre_adan_sound_path, 50))

    def request_playback(self, command: PlayAudioCommand):
        if command.requester == "AdanManager":
            self.mediator.notify(self, "open_mic")
            self._play(command)
    
        elif command.requester == "NextAdan" and self.is_adan_near:
            self._play(command)

        else:
            if self.is_adan_near or (self.current_command is not None and self.current_command.requester == "AdanManager"):
                self.mediator.notify(self, "cant_play_audio", "لا يمكن تشغيل الصوت", "انتظر حتى الإنتهاء من الأذان" )
                if command.requester == "QuraanPageManager":
                    self.mediator.notify(self, "failed_to_play")
                elif command.requester == "FirebaseVoiceRecord":
                    # Send can't play status for Firebase audio task since it can't be played
                    if command.adan_name:  # adan_name contains the command_id for Firebase tasks
                        self.mediator.notify(self, "firebase_audio_task_cant_play", command.adan_name)
            else:
                if self.isPlaying() or self.isPaused():
                    self.pending_command = command
                    self.waiting_to_set_source = True
                    self._stop_current()
                else:
                    self.mediator.notify(self, "open_mic")
                    self._play(command)
                
                if command.requester == "QuraanPageManager":
                    self.mediator.notify(self, "successfully_played")
                
                elif command.requester == "InstantPlayer":
                    self.position_timer.start(200)
                
    def isPlaying(self):
        return self.player.isPlaying()
    
    def isPaused(self):
        return self.player.playbackState() == QMediaPlayer.PausedState

    def _resume(self):
        self.player.play()

    def _pause(self):
        self.player.pause()

    def _play(self, command):

        if hasattr(self, 'duration_timer') and self.duration_timer.isActive():
            self.duration_timer.stop()

        self.current_command = command
        url = QUrl.fromLocalFile(command.file_path)
        # Set the volume from the command
        volume = 0.0 if self.is_player_muted else command.volume / 100.0  # Convert percentage to 0-1 range
        self.audio_output.setVolume(volume)
        
        if self.player.source() == url:
            self.player.setPosition(0)
        else:
            self.player.setSource(url)

        self.player.play()

        if self.current_command.duration and self.current_command.duration > 0:
            if not hasattr(self, 'duration_timer'):
                self.duration_timer = QTimer(self.main_window)
                self.duration_timer.setSingleShot(True)
                self.duration_timer.timeout.connect(self.stop_notification)

            self.duration_timer.start(self.current_command.duration * 1000) 

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

    def stop_notification(self):
        if self.current_command and self.current_command.requester == "NotificationManager" and self.isPlaying():
            self._stop_current()

    def handle_adan_volume_change(self, adan_name, volume):
        """Handle volume change for a specific adan"""
        # Check if an adan is currently playing and if it's the one being changed
        if (self.current_command is not None and 
            self.current_command.requester == "AdanManager" and 
            self.player.playbackState() in [QMediaPlayer.PlayingState, QMediaPlayer.PausedState] and
            self.current_command.adan_name == adan_name):
            
            # Update the volume
            volume_value = volume / 100.0
            self.audio_output.setVolume(volume_value)
            
            # Also update the volume in the current command
            self.current_command.volume = volume

    def stop_quraan_audio(self, index, category):
        if self.current_command and self.current_command.requester == "QuraanPageManager" and self.current_command.index == index and self.current_command.adan_name == category and self.isPlaying():
            self._stop_current()
