from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QCheckBox, QPushButton, QSpacerItem
from ResourceFile import resource_path
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy


class AdanAssignmentDialog(QDialog):
    def __init__(self, audio_name, callback, is_fajer_adan = False, parent=None):
        super().__init__(parent)
        self.setWindowTitle("تعديل صوت الاذان")
        self.setFixedSize(300, 200)
        self.audio_name = audio_name
        self.callback = callback
        self.is_fajer_adan = is_fajer_adan
        self.checkboxes = {}

        layout = QVBoxLayout(self)
        
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        Tajawal_font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Tajawal/Tajawal-Bold.ttf"))
        tajawal_bold_font_family = QFontDatabase.applicationFontFamilies(Tajawal_font_id)[0]
        tajawal_bold_font_16 = QFont(tajawal_bold_font_family, 16)

        self.label = QLabel(f"  قم باختيار الاذان :")
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.label.setFont(tajawal_bold_font_16)

        layout.addWidget(self.label)

        adan_names = ["الفجر"] if is_fajer_adan else ["الظهر", "العصر", "المغرب", "العشاء"]
        for name in adan_names:
            checkbox = QCheckBox(name)
            checkbox.setStyleSheet(
                """
                QCheckBox::indicator {
                        width: 20px;
                        height: 20px;
                    }
            
            """
            )
            checkbox.setFont(tajawal_bold_font_16)

            layout.addWidget(checkbox, alignment=Qt.AlignmentFlag.AlignHCenter)

            # layout.addWidget(checkbox)
            self.checkboxes[name] = checkbox

        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        confirm_btn = QPushButton("تأكيد")
        confirm_btn.clicked.connect(self.assign)
        layout.addWidget(confirm_btn)

    def assign(self):

        checked_indexes = [i if self.is_fajer_adan else i + 1 for i, cb in enumerate(self.checkboxes.values()) if cb.isChecked() ]
        
        if len(checked_indexes) != 0:
            self.callback(self.audio_name, checked_indexes)

        self.accept()
