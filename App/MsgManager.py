from PySide6.QtCore import QObject, Signal

class MsgManagerSignals(QObject):
    hide_emergency_frame_signal = Signal()
    disable_emergency_frame_signal = Signal()

class MsgManager():

    msg_manager_signals = MsgManagerSignals()
    hide_emergency_frame_signal = msg_manager_signals.hide_emergency_frame_signal
    
    
    def __init__(self, main_page_msg_frame, main_page_error_label, main_page_info_label, noti_page_msg_frame, noti_page_info_label):
        
        self.mediator = None
        self.main_page_msg_frame = main_page_msg_frame
        self.main_page_error_label = main_page_error_label
        self.main_page_info_label = main_page_info_label
        self.noti_page_msg_frame = noti_page_msg_frame
        self.noti_page_info_label = noti_page_info_label

        self.emergency_counter = -1
        self.main_page_counter = -1
        self.noti_page_counter = -1

    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator
    
    def activate_emergency_frame_timer(self, timer):
        if timer > 0 :
            self.emergency_counter = timer
        else:
            print("ERROR: TIMER INVALID !!!")

    def disable_emergency_frame_timer(self):
        self.emergency_counter = -1
    
    def show_main_page_msg(self, error_msg, info_msg, timer):
        if timer > 0:
            
            self.main_page_error_label.setText(error_msg)
            self.main_page_info_label.setText(info_msg)
            
            self.main_page_msg_frame.show()
                
            if self.main_page_counter != -1 :
                self.main_page_counter += timer
            
            else:
                self.main_page_counter = timer

        else:
            print("ERROR: TIMER INVALID !!!")

    def hide_main_page_msg(self):
        self.main_page_msg_frame.hide()
        self.main_page_error_label.setText("")
        self.main_page_info_label.setText("")
        
        self.main_page_counter = -1

    def show_noti_page_msg(self, info_msg, timer):
        if timer > 0:
            
            self.noti_page_info_label.setText(info_msg)
            self.noti_page_msg_frame.show()
            
            if self.noti_page_counter != -1:
                self.noti_page_counter += timer
            
            else:
                self.noti_page_counter = timer
        else:
            print("ERROR: TIMER INVALID !!!")
    
    def hide_noti_page_msg(self):
        self.noti_page_msg_frame.hide()
        self.noti_page_info_label.setText("")
        
        self.noti_page_counter = -1

    def handle_time_update(self):

        if self.emergency_counter > 0:
            self.emergency_counter -= 1
            if self.emergency_counter == 0 :

                self.mediator.notify(self, "emergency_frame_timer_expired")

                self.emergency_counter = -1

        if self.main_page_counter > 0:
            self.main_page_counter -= 1
            if self.main_page_counter == 0:
                self.hide_main_page_msg()
                self.main_page_counter = -1

        if self.noti_page_counter > 0:
            self.noti_page_counter -= 1
            if self.noti_page_counter == 0:
                self.hide_noti_page_msg()
                self.noti_page_counter = -1
