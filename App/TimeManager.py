from PySide6.QtWidgets import QWidget
from PySide6.QtCore import  QObject, Signal
from Time import Time
from AdanTimePrepare import AdanTimePrepare
from GeneralSettings import GeneralSettings

class NextDaySignal(QObject):
    
    next_day = Signal()

    def __init__(self):
        super().__init__()

class TimeManager():

    def __init__(self, am_pm_label, seconds_label, am_pm_frame, time_lower_widget, time_label, day_label, date_label, higri_date_label):
        
        self.time = Time(am_pm_label, seconds_label, am_pm_frame, time_lower_widget, time_label, day_label, date_label, higri_date_label)
    
    def connect_to_next_day_signal(self, func):
        self.time.new_day_signal.connect(func)

    def connect_to_time_updated_signal(self, func):
        self.time.time_updated.connect(func)

    def connect_to_new_jomoaa_signal(self, func):
        self.time.new_jomoaa.connect(func)

    def update_time_formate(self, new_time_formate):
        self.time.update_time_formate(new_time_formate)

    def run(self):
        #  should run in different thread!!!
        self.time.run()
