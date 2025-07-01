from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QSizePolicy
from PySide6.QtCore import QSize 
from PySide6.QtGui import QFontDatabase, QFont, QIcon
from ResourceFile import resource_path
import os

class AudioItemWidget(QWidget):
    def __init__(self, filename, play_callback, stop_callback):
        super().__init__()
        self.filename = filename
        self.play_callback = play_callback
        self.stop_callback = stop_callback

        Tajawal_font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Tajawal/Tajawal-Bold.ttf"))
        tajawal_bold_font_family = QFontDatabase.applicationFontFamilies(Tajawal_font_id)[0]
        tajawal_bold_font_18 = QFont(tajawal_bold_font_family, 18)
        
        self.setStyleSheet("background-color: blue;")

        self.label = QLabel(self.remove_extension(filename))
        self.label.setFont(tajawal_bold_font_18)
        self.label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)

        self.play_button = QPushButton()
        self.play_button.setIcon(QIcon("resources/images/play_14441317.png"))  # path to your image
        self.play_button.setIconSize(QSize(24, 24))  
        self.remove_bg_color_from_qpush_btn(self.play_button)

        self.stop_button = QPushButton()
        self.stop_button.setIcon(QIcon("resources/images/square_13738097.png"))  # path to your image
        self.stop_button.setIconSize(QSize(24, 24)) 
        self.remove_bg_color_from_qpush_btn(self.stop_button)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0) 

        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.play_button)
        layout.addWidget(self.stop_button)

        self.play_button.clicked.connect(self.play)
        self.stop_button.clicked.connect(self.stop)

        self.set_inactive_style()

    def play(self):
        self.play_callback(self.filename, self)

    def stop(self):
        self.stop_callback(self)

    def sizeHint(self):
        return QSize(350, 80)
    
    def remove_bg_color_from_qpush_btn(self, button):
        button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;  /* Optional: remove button border */
            }
        """)

    def set_active_style(self):
        self.setStyleSheet("""
            background-color: #d0f0d0;
            border: 1px solid #5cb85c;
            border-radius: 6px;
        """)
        self.label.setStyleSheet("font-weight: bold; color: #2e7d32;")

    def set_inactive_style(self):
        self.setStyleSheet("""
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 6px;
        """)
        self.label.setStyleSheet("font-weight: normal; color: black;")

    def remove_extension(self, filename: str) -> str:
        """
        Remove the extension from a filename, including those with spaces.
        
        Example:
            "Surah Al-Fatiha 001.mp3" → "Surah Al-Fatiha 001"
        """
        return os.path.splitext(filename)[0]