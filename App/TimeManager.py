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

    def __init__(self, am_pm_label, seconds_label, am_pm_frame, time_lower_widget, time_label, day_label, date_label, higri_date_label, general_settings) :

        self.next_day_signal = NextDaySignal()

        self.curr_time = Time(am_pm_label, seconds_label, am_pm_frame, time_lower_widget, time_label, day_label, date_label, higri_date_label)

        self.general_settings = general_settings

    def run(self):
        self.curr_time.update_time()
        
        is_new_day = self.curr_time.check_if_new_day()
        if is_new_day:
            self.next_day_signal.next_day.emit()

        self.curr_time.update_ui(self.general_settings.get_time_formate()[0], is_new_day)
