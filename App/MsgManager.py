from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox

class MsgManager():

    def __init__(self):
        
        self.active_boxes = []
        self.mediator = None

    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    def show_auto_close_error(self, title, message, parent=None, timeout=4000):

        msg_box = QMessageBox(parent)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setModal(False)
        
        try :
            msg_box.show()
        except Exception as e:
            pass

        # Store reference
        self.active_boxes.append(msg_box)

        def close_and_cleanup():
            msg_box.close()
            self.active_boxes.remove(msg_box)

        QTimer.singleShot(timeout, close_and_cleanup)

    def show_auto_close_info(self, title, message, parent=None, timeout=4000):
        msg_box = QMessageBox(parent)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setModal(False)
        msg_box.show()

        # Store reference
        self.active_boxes.append(msg_box)

        def close_and_cleanup():
            msg_box.close()
            self.active_boxes.remove(msg_box)

        QTimer.singleShot(timeout, close_and_cleanup)
