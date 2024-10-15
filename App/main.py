from AppManager import AppManager
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from ResourceFile import resource_path
import uuid

def get_mac_address():
    mac = uuid.getnode()
    return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

def validate_license():
    current_mac = get_mac_address()
    return (current_mac == '18:C0:4D:9F:E6:76') or True

if __name__ == "__main__":

    app = QApplication(sys.argv)

    if validate_license():
        main_ui_file = resource_path("resources/ui/main_adan_window_ui.ui")
        window = AppManager(main_ui_file)
        window.show()
        sys.exit(app.exec())

    else:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Access Denied")
        msg_box.setText("Your device is not authorized to run this application.")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec() 
        sys.exit()
    