from PySide6.QtWidgets import QWidget
from PySide6.QtCore import  QObject, Signal, QTimer
from Time import Time
from AdanTimePrepare import AdanTimePrepare
from GeneralSettings import GeneralSettings
import time


class TimeManager():

    def __init__(self, mediator, am_pm_label, seconds_label, am_pm_frame, time_lower_widget, time_label, day_label, date_label):
        
        self.mediator = None
        
        mediator.register("TimeManager", self)

        self.time = Time(mediator, am_pm_label, seconds_label, am_pm_frame, time_lower_widget, time_label, day_label, date_label)
    
    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    # def connect_to_next_day_signal(self, func):
    #     self.time.new_day_signal.connect(func)

    def connect_to_time_updated_signal(self, func):
        self.time.time_updated.connect(func)

    # def connect_to_new_jomoaa_signal(self, func):
    #     self.time.new_jomoaa.connect(func)

    def connect_to_get_formate_signal(self, func):
        self.time.get_formate_signal.connect(func)

    def connect_to_check_version_update(self, func):
        self.time.check_for_new_release.connect(func)

    def update_time_formate(self, new_time_formate):
        
        self.time.update_time_formate(new_time_formate)
    
    def get_time_formate(self):
        if self.mediator:
            return self.mediator.notify(self, "request_time_formate")
        
        # self.time.get_formate()

    def run(self):
        # Get the current time
        start_time = time.time()
        
        # Run the time update
        self.time.run()
        
        # Calculate how long the update took
        elapsed = time.time() - start_time
        
        # Adjust the next timer interval to maintain 1-second precision
        # If the update took 0.1 seconds, wait 0.9 seconds for the next update
        next_interval = max(0, 1.0 - elapsed)
        
        # Schedule the next update with the adjusted interval
        QTimer.singleShot(int(next_interval * 1000), self.run)
