import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from ResourceFile import resource_path

class CustomDialog(QDialog):
    def __init__(self, accept_func, reject_func, label_text=None, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("نافذة اشعار")

        self.accept_func = accept_func
        self.reject_func = reject_func

        ui_file = QFile(resource_path("resources/ui/customDialog.ui"))
        ui_file.open(QFile.ReadOnly)
        
        # Load the .ui file
        loader = QUiLoader()
        
        # Load the UI into the QDialog
        self.dialog = loader.load(ui_file)
        ui_file.close()

        self.setupUI()

        if label_text:
            self.dialog_label.setText(label_text)

        self.setLayout(self.dialog.layout())

    def setupUI(self):
        
        self.dialog_label = self.dialog.findChild(QLabel, "dialog_label")

        self.ok_button = self.dialog.findChild(QPushButton, "ok_button")
        self.cancel_button = self.dialog.findChild(QPushButton, "cancel_button")
        # Connect buttons to their respective slots
        self.ok_button.clicked.connect(self.ok)
        self.cancel_button.clicked.connect(self.cancel)
    
    def ok(self):
        self.accept_func()
        self.accept()

    def cancel(self):
        self.reject_func()
        self.reject()
