from PySide6.QtCore import QTimer
from Time import Time
import time

class TimeManager():

    def __init__(self, mediator, am_pm_label, seconds_label, am_pm_frame, time_lower_widget, time_label, day_label, date_label):
        
        self.mediator = None
        
        mediator.register("TimeManager", self)

        self.time = Time(mediator, am_pm_label, seconds_label, am_pm_frame, time_lower_widget, time_label, day_label, date_label)
    
    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    def connect_to_time_updated_signal(self, func):
        self.time.time_updated.connect(func)

    def update_time_formate(self, new_time_formate):
        self.time.update_time_formate(new_time_formate)
    
    def get_time_formate(self):
        if self.mediator:
            return self.mediator.notify(self, "request_time_formate")

    def run(self):
        # Get the current time
        start_time = time.time()
        
        # Run the time update
        self.time.run()
        
        # Calculate how long the update took
        elapsed = time.time() - start_time
        
        # Adjust the next timer interval to maintain 1-second precision
        # If the update took 0.1 seconds, wait 0.9 seconds for the next update
        next_interval = max(0, 0.3 - elapsed)
        
        # Schedule the next update with the adjusted interval
        QTimer.singleShot(int(next_interval * 1000), self.run)
