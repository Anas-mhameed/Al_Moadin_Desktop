from PySide6.QtCore import QTimer
from Time import Time
import time

class TimeManager():

    def __init__(self, mediator, am_pm_label, seconds_label, am_pm_frame, time_lower_widget, time_label, day_label, date_label):
        
        self.mediator = None
        
        mediator.register("TimeManager", self)

        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("time_manager", "initialization", "starting", "TimeManager initializing")

        self.time = Time(mediator, am_pm_label, seconds_label, am_pm_frame, time_lower_widget, time_label, day_label, date_label)

        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("time_manager", "initialization", "completed", "TimeManager ready with Time component")
    
    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    def connect_to_time_updated_signal(self, func):
        if hasattr(self, 'mediator') and self.mediator:
            func_name = getattr(func, '__name__', str(func))
            self.mediator.log("time_manager", "signal_connection", "connected", 
                            f"time_updated signal connected to: {func_name}")
        
        self.time.time_updated.connect(func)

    def update_time_formate(self, new_time_formate):
        if hasattr(self, 'mediator') and self.mediator:
            old_format = getattr(self.time, 'time_formate', 'unknown')
            self.mediator.log("time_manager", "format_update", "delegating", 
                            f"Updating Time format: '{old_format}' -> '{new_time_formate}'")
        
        self.time.update_time_formate(new_time_formate)
    
    def get_time_formate(self):
        if self.mediator:
            if hasattr(self, 'mediator') and self.mediator:
                self.mediator.log("time_manager", "format_request", "requesting", 
                                "Requesting time format from GeneralSettings via mediator")
            
            result = self.mediator.notify(self, "request_time_formate")
            return result

    def run(self):
        # Get the current time
        start_time = time.time()
        
        # Run the time update
        self.time.run()
        
        # Calculate how long the update took
        elapsed = time.time() - start_time
        
        # Adjust the next timer interval to maintain 1-second precision
        next_interval = max(0, 0.3 - elapsed)
        
        # Log every single run to see all activity
        if hasattr(self, 'mediator') and self.mediator:
            self.mediator.log("time_manager", "performance", "run_cycle", 
                            f"Update took {elapsed:.3f}s, next interval: {next_interval:.3f}s")
        
        # Schedule the next update with the adjusted interval
        QTimer.singleShot(int(next_interval * 1000), self.run)
