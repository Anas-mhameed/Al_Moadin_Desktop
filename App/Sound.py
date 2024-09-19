from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QFileDialog 
from PySide6.QtCore import QTimer
from PySide6.QtCore import QFile, QUrl

class Sound:

    def __init__(self, sound_file = "", volume = 50, duration = -1):

        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)

        self.file_path = sound_file
        # from second to millisecond
        self.play_period = duration * 1000 
        
        self.set_volume(volume)

        self.media_player.durationChanged.connect(lambda: self.get_duration())

    def track_media_position(self, func):
        self.media_player.positionChanged.connect(func)

    def track_media_duration(self, func):
        self.media_player.durationChanged.connect(func)
    
    def disconnect_media_position(self, func):
        self.media_player.positionChanged.disconnect(func)

    def set_position(self, ms):
        self.media_player.setPosition(ms)
    
    def set_file_path_manual(self, new_file_path):
        self.file_path = new_file_path

    def set_volume(self, volume):
        self.volume = volume / 100.0
        self.set_audio_volume()
        
    def set_audio_volume(self):
        self.audio_output.setVolume(self.volume)
    
    def get_duration(self):
        return self.media_player.duration()

    def is_playing(self):
        return self.media_player.isPlaying()
    
    def is_paused(self):
        if not self.is_playing() :
            # if self.media_player.mediaStatus() == QMediaPlayer.BufferingMedia :
            #     return True
            # elif self.media_player.mediaStatus() == QMediaPlayer.StalledMedia :
            #     return True
            if self.status() == QMediaPlayer.BufferedMedia:
                return True
        return False
    
    def status(self):
        return self.media_player.mediaStatus()

    def end_of_media(self):
        return self.status() == QMediaPlayer.EndOfMedia

    def update_file_path(self, new_path):
        self.file_path = new_path

    def play(self):
        self.stop()
        self.set_audio_volume()
        try :
            self.media_player.setSource(QUrl().fromLocalFile(self.file_path))
            self.media_player.setPosition(0)
            self.media_player.play()
        except Exception as e:
            print(e)
            print("الرجاء التحقق من ادخال ملف صوتي")

    def resume(self):
        if not self.check_path_is_empty():
            if self.is_paused():
                try:
                    self.media_player.play()
                except:
                    pass

    def select_sound_file(self, widget):
        file_dialog = QFileDialog(widget)
        file_dialog.setNameFilter("Sound Files (*.wav *.mp3 *.ogg)")
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                self.file_path = file_paths[0]

    def get_file_path(self):
        return self.file_path

    def removeSound(self):
        self.file_path = ""

    def stop(self):
        try:
            self.media_player.stop()
        except:
            pass

    def pause(self):
        if not self.check_path_is_empty():
            if self.is_playing():
                try:
                    self.media_player.pause()    
                except:
                    pass
    
    def check_path_is_empty(self):
        return True if self.file_path == "" else False

    # def play_for_duration(self):
    #     # Set the media source (example: "audio.mp3")
    #     self.play()

    #     # Set a timer to stop the playback after the specified duration
    #     QTimer.singleShot(self.duration, self.stop)