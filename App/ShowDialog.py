from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QDialog
from ResourceFile import resource_path
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class ShowDialog(QDialog):

    def __init__(self, noti_time, noti_info, handle_sound, handle_save, handle_delete, parent=None):
        super().__init__(parent)

        ui_file = QFile(resource_path("resources/ui/show_notification_dialog.ui"))
        ui_file.open(QFile.ReadOnly)
        
        # Load the .ui file
        loader = QUiLoader()
        
        # Load the UI into the QDialog
        self.dialog = loader.load(ui_file, self)
        self.setFixedSize(450, 400)  # Set a fixed size of 400x300 for the dialog
        self.setStyleSheet("background-color: white;")
        ui_file.close()

        self.destroy_and_remove_from_db = handle_delete
        self.new_file_path = ""
        self.setupUI()

        self.noti_time_label.setText(f"{noti_time.time().strftime("%H:%M")}")
        self.noti_info_label.setText(noti_info)
        self.noti_date_label.setText(f"{noti_time.date()}")

        self.edit_sound_noti_button.clicked.connect(lambda: self.edit_sound(handle_sound))
        self.save_noti_button.clicked.connect(lambda: self.save(handle_save))
        self.delete_noti_button.clicked.connect(lambda: self.delete())

        self.setLayout(self.dialog.layout())

    def setupUI(self):
        self.noti_time_label = self.dialog.findChild(QLabel, "noti_time_label")
        self.noti_info_label = self.dialog.findChild(QLabel, "noti_info_label")
        self.noti_date_label = self.dialog.findChild(QLabel, "noti_date_label")

        self.edit_sound_noti_button = self.dialog.findChild(QPushButton, "edit_sound_noti_button")
        self.save_noti_button = self.dialog.findChild(QPushButton, "save_noti_button")
        self.delete_noti_button = self.dialog.findChild(QPushButton, "delete_noti_button")
    
    def edit_sound(self, handle_sound):
        self.new_file_path = handle_sound()
    
    def delete(self):
        self.destroy_and_remove_from_db()
        self.reject()

    def save(self, handle_save):
        handle_save(self.new_file_path)
        self.accept()