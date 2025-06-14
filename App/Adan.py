from AppManager import resource_path
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtCore import QUrl


class Adan:

    def __init__(self, adan_name_label, adan_time, time_label_ui, active=False, sound_path=None):
        
        self.name_label = adan_name_label
        self.name = adan_name_label.text()
        self.original_time = adan_time
        self.time = adan_time
        self.time_label_ui = time_label_ui
        self.is_active = active
        
        # Sound properties
        self.sound_path = sound_path if sound_path else ""
        self.volume = 50  # Default volume 50%

        font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Noto_Kufi_Arabic/static/NotoKufiArabic-SemiBold.ttf"))
        self.kufi_semiBold_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(self.kufi_semiBold_font_family, 28)
        font.setBold(True)

        self.name_label.setFont(font)

        font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Noto_Kufi_Arabic/static/NotoKufiArabic-Regular.ttf"))
        self.kufi_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(self.kufi_font_family, 24)
        self.time_label_ui.setFont(font)

    def set_sound_path(self, path):
        self.sound_path = path
        
    def get_sound_path(self):
        return self.sound_path
        
    def set_volume(self, volume):
        self.volume = volume
        
    def get_volume(self):
        return self.volume

    def get_adan_time(self):
        return self.time
    
    def get_adan_name(self):
        return self.name

    def get_original_time(self):
        return self.original_time

    def update_original_time(self, new_original_time):
        self.original_time = new_original_time

    def update_time(self, new_time):
        self.time = new_time
    
    def check_state(self):
        return self.is_active

    def change_state(self, is_checked):
        self.is_active = is_checked
    
    def update_ui(self, formate):
        #update adan time label
        self.time_label_ui.setText(self.time.strftime(formate))

    def set_next_adan_ui(self):
        # self.name_label.setText("blabla")
        self.name_label.setStyleSheet("color: rgb(8, 148, 108);")

    def remove_next_adan_ui(self):
        self.name_label.setStyleSheet("color: black;")
