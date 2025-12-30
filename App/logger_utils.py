import logging
from datetime import datetime
from functools import wraps

def log_adan_event(event_type):
    """Decorator to log adan-related events"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger('AdanApp')
            start_time = datetime.now()
            
            try:
                logger.info(f"[{event_type}] Starting: {func.__name__}")
                result = func(*args, **kwargs)
                duration = (datetime.now() - start_time).total_seconds()
                logger.info(f"[{event_type}] Completed: {func.__name__} (took {duration:.2f}s)")
                return result
            except Exception as e:
                logger.error(f"[{event_type}] Failed: {func.__name__} - {str(e)}", exc_info=True)
                raise
        return wrapper
    return decorator

class AdanLogger:
    def __init__(self):
        self.logger = logging.getLogger('AdanApp')
    
    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    def log_time_update(self, current_time, next_adan_time, next_adan_name):
        self.logger.info(f"[TIME_UPDATE] Current: {current_time}, Next Adan: {next_adan_name} at {next_adan_time}")
    
    def log_adan_times(self, adan_times_dict):
        self.logger.info(f"[ADAN_TIMES] Daily schedule: {adan_times_dict}")
    
    def log_adan_play(self, adan_name, audio_file, volume):
        self.logger.info(f"[ADAN_PLAY] Playing {adan_name} - File: {audio_file}, Volume: {volume}%")
    
    def log_adan_stop(self, adan_name, reason="completed"):
        self.logger.info(f"[ADAN_STOP] Stopped {adan_name} - Reason: {reason}")
    
    def log_notification_play(self, notification_type, file_path):
        self.logger.info(f"[NOTIFICATION] Playing {notification_type} - File: {file_path}")
    
    def log_adan_state_change(self, old_state, new_state, adan_name=None):
        self.logger.info(f"[ADAN_STATE] Changed from '{old_state}' to '{new_state}'" + 
                        (f" for {adan_name}" if adan_name else ""))
    
    def log_volume_change(self, device, old_volume, new_volume):
        self.logger.info(f"[VOLUME] {device} volume changed: {old_volume}% -> {new_volume}%")
    
    def log_zigbee_device(self, device_id, status, signal_strength=None):
        signal_info = f", Signal: {signal_strength}" if signal_strength else ""
        self.logger.info(f"[ZIGBEE] Device {device_id}: {status}{signal_info}")
    
    def log_error(self, component, error_msg, exception=None):
        if exception:
            self.logger.error(f"[ERROR] {component}: {error_msg}", exc_info=True)
        else:
            self.logger.error(f"[ERROR] {component}: {error_msg}")
    
    def log_warning(self, component, warning_msg):
        self.logger.warning(f"[WARNING] {component}: {warning_msg}")

    def log_adan_completion(self, adan_name, duration_played, total_duration):
        self.logger.info(f"[ADAN_COMPLETE] {adan_name} finished - Played: {duration_played:.1f}s / Total: {total_duration:.1f}s")

    def log_adan_time_reached(self, adan_name, scheduled_time, actual_time):
        self.logger.info(f"[ADAN_TIME] {adan_name} time reached - Scheduled: {scheduled_time}, Actual: {actual_time}")

    def log_adan_skipped(self, adan_name, reason):
        self.logger.info(f"[ADAN_SKIP] {adan_name} skipped - Reason: {reason}")
