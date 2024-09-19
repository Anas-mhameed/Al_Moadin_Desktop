from PySide6.QtCore import QTimer

class Message:
     
    def __init__(self, info_msg_label):
        self.info_msg_label = info_msg_label
     
    def update_info_label(self, msg):
        self.info_msg_label.setText(msg)
    
class MainMessager:

    def __init__(self, messages_frame, error_msg_label, info_msg_label):

        self.messages_frame = messages_frame

        self.error_msg_label = Message(error_msg_label)
        self.info_msg_label = Message(info_msg_label)

    def update_error_label(self, msg):
        self.error_msg_label.update_info_label(msg)
    
    def update_info_label(self, msg):
        self.info_msg_label.update_info_label(msg)
    
    def show(self):
        self.messages_frame.show()
    
    def hide(self):
        self.messages_frame.hide()

class SecondaryMessager:

    def __init__(self, messages_frame, info_msg_label):

        self.messages_frame = messages_frame
        self.info_msg_label = Message(info_msg_label)

    def update_info_label(self, msg):
        self.info_msg_label.update_info_label(msg)
    
    def show(self):
        self.messages_frame.show()
    
    def hide(self):
        self.messages_frame.hide()