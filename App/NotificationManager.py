from helper_functions import select_sound_file
from notificationUI import Ui_notification_widget
from Notification import AdanNotification
from Runnable import Runnable
from DatabaseManager import DatabaseManager  # Import DatabaseManager directly
from PySide6.QtWidgets import (
    QWidget,
)
import datetime as dt
from PySide6.QtCore import QDate
from PySide6.QtCore import QObject, Signal

from PlayAudioCommand import PlayAudioCommand


class NotificationSignal(QObject):
    cancel_noti_signal = Signal()
    show_msg_signal = Signal(str, int)

    
class NotificationManager:

    notification_signal = NotificationSignal()
    cancel_noti_signal = notification_signal.cancel_noti_signal
    show_msg_signal = notification_signal.show_msg_signal

    def __init__(self, prayers_times, main_window, scrollArea_container, runnable_manager, total_noti_label, noti_sort_box, *args, **kwargs):

        self.mediator = None

        self.next_noti = None
        self.curr_noti_type = -1

        self.prayers_times = prayers_times

        # Initialize adans_duration with 5 elements (0-4 indices)
        # Index 0: Fajer, 1: Dohor, 2: Aser, 3: Magreb, 4: Ishaa
        # Note: Jomoaa (index 6 in notifications) uses the same duration as Dohor (index 1)
        self.adans_duration = [0, 0, 0, 0, 0]

        self.file_path = None

        self.main_window = main_window
        self.curr_time = dt.datetime.now()

        self.scrollArea_container = scrollArea_container

        self.database_manager = DatabaseManager()  # Initialize DatabaseManager directly

        self.runnable_manager = runnable_manager
        self.sort_box = noti_sort_box

        self.total_noti_label = total_noti_label
        self.total_notifications = 0

        self.permenant_notifications = []
        self.permenant_noti_index = 0
        self.once_notifications = []

        self.pre_adan_preparation_emitted = False

        self.get_notification_from_db()

        self.clear_layout()
        self.show_notifications()

    def request_adans_duration(self):
            self.mediator.notify(self, "request_adans_duration")

    def handel_save_noti_button_clicked(self, day_of_week, adan_type, is_permenant, adan_index, seconds, date, duration):
            if self.file_path == None:
                self.mediator.notify(self, "error_saving_notification", "لم يتم حفظ الاشعار", "الرجاء اختيار ملف صوتي")
                return

            if (not is_permenant and adan_index == 5 and day_of_week != 5) :
                self.mediator.notify(self, "error_saving_notification", "لم يتم حفظ الاشعار", "عليك اختيار تاريخ يوافق يوم الجمعة")
                return
            
            res = self.create_notification(adan_type, is_permenant, adan_index + 1, seconds, date, duration)

            if res:
                self.cancel_noti_signal.emit()
        
    def update_curr_time(self, updated_time):
        self.curr_time = updated_time
    
    def update_adan_duration(self, index, new_duration):
        """
        Update the duration of an Adan sound.
        
        Args:
            index (int): The index of the Adan (0-4)
            new_duration (int): The new duration in milliseconds
        """
        if 0 <= index < len(self.adans_duration):
            self.adans_duration[index] = new_duration

    def get_adan_duration(self, index):
        """
        Get the duration of an Adan sound.
        
        Args:
            index (int): The index of the Adan (1-6 for notifications)
            
        Returns:
            int: The duration in seconds
        """
        # Convert notification index (1-6) to duration index (0-5)
        duration_index = index - 1
        
        # Special case: Jomoaa (index 6) uses the same duration as Dohor (index 1)
        if index == 6:
            duration_index = 1  # Dohor's index in adans_duration
        
        if 0 <= duration_index < len(self.adans_duration):
            duration_in_seconds = self.adans_duration[duration_index] // 1000
            total_seconds = duration_in_seconds + 1
            return total_seconds
        else:
            return 0

    def get_notification_from_db(self):
            # dan_index Integer, minutes REAL, date TEXT, duartion Integer, file_path TEXT, is_permanant Integer, noti_type Integer
            records = self.database_manager.get_notifications()
            for record in records:
                file_path = record[4]
                date = record[2]
                if date != None:
                    date = QDate.fromString(date, "yyyy-MM-dd")
                is_permenant = bool(record[5])
                noti_type = bool(record[6])
                
                adan_index = record[0]

                minutes = int(record[1]) if record[1] >= 1 else record[1] 
                duration = record[3]
                is_active = bool(record[7])

                self.intialize_notification(is_permenant, noti_type, adan_index, minutes, date, duration, file_path, is_active)
        
    def create_notification(self, is_before_adan, is_permenant, *args):
        
        date = None

        if not is_permenant:
            date = args[2]
        
        # args[0] is the adan_index (1-6)
        adan_index = args[0]
        time = self.get_adan_time(adan_index)

        minutes = args[1]
        duration = args[3] * 60 # from minutes to seconds

        duration_in_seconds = 0

        if not is_before_adan:
            # Get duration based on notification index (1-6)
            duration_in_seconds = self.get_adan_duration(adan_index)

        file_path = self.file_path
        new_notification = AdanNotification(is_before_adan, time, adan_index, minutes, file_path, date, duration, duration_in_seconds)

        # prevent conflict between notifications
        validation_res = self.validate_noti_time(new_notification, is_permenant)
        if validation_res[0]:
            self.position_notification(new_notification, is_permenant)
        else:
            self.show_msg_signal.emit(validation_res[1], 4)
            return False
        
        date_in_db = date.toString("yyyy-MM-dd") if date else None

        self.save_notification_in_db((adan_index, minutes, date_in_db, duration, file_path, is_permenant, is_before_adan, 1, duration_in_seconds))

        self.file_path = None

        self.connect_noti_to_ui(new_notification)

        self.clear_layout()

        self.show_notifications()

        if is_permenant:
            self.intiate_index()

        self.find_next_noti()

        self.increase_total_noti_num()

        return True

    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    def change_noti_state_in_db(self, notification, new_state):
        def temp(func):
            if func():
                self.database_manager.change_noti_state(notification.get_index(), notification.get_seconds(), new_state)
        runnable = Runnable(temp)
        self.runnable_manager.runTask(runnable)

    def update_notification_path_in_db(self, notification, new_val):
        def temp(func):
            if func():
                self.database_manager.update_notification(notification.get_index(), notification.get_seconds(), "file_path", new_val)
        runnable = Runnable(temp)
        self.runnable_manager.runTask(runnable)

    def update_notification_in_db(self, notification, row, new_val):
        def temp(func):
            if func():
                self.database_manager.update_notification(notification.get_index(), notification.get_seconds(), row, new_val)
        runnable = Runnable(temp)
        self.runnable_manager.runTask(runnable)
    
    def delete_notification_from_db(self, notification):
        def temp(func):
            if func():
                self.database_manager.delete_notification(notification)
        runnable = Runnable(temp)
        self.runnable_manager.runTask(runnable)

    def save_notification_in_db(self, noit_data):
        def temp(func):
            if func():
                self.database_manager.save_notification_in_db(noit_data)
        runnable = Runnable(temp)
        self.runnable_manager.runTask(runnable)

    def increase_total_noti_num(self):
        self.total_notifications += 1
        self.update_total_label() 

    def decrease_total_noti_num(self):
        self.total_notifications -= 1
        if self.total_notifications < 0 :
            self.total_notifications = 0
        self.update_total_label()

    def update_total_label(self):
        self.total_noti_label.setText(str(self.total_notifications))

    def validate_noti_time(self, notification, is_permenant):
        if not is_permenant:
            curr_time = dt.datetime.now()

            if curr_time > notification.get_adjusted_datetime():
                return (False, "الرجاء تعديل الوقت\n هذا الاشعار قد فات اوانه")
        for noti in self.permenant_notifications:
            if notification.get_adjusted_datetime().time() == noti.get_adjusted_datetime().time():
                return (False, "هذا الاشعار يتعارض مع اشعار اخر\n يرجى تغيير التوقيت")
        for noti in self.once_notifications:
            if notification.get_adjusted_datetime().time() == noti.get_adjusted_datetime().time():
                return (False, "هذا الاشعار يتعارض مع اشعار اخر\n يرجى تغيير التوقيت")
        return (True, "")

    def show_notifications(self):
        index = self.sort_box.currentIndex() + 1

        i = 0
        j = 0
        while i < len(self.permenant_notifications) and j < len(self.once_notifications):

            if self.permenant_notifications[i].get_index() != index and index != 7:
                # self.permenant_notifications[i].hide()
                i += 1
                continue
            elif self.once_notifications[j].get_index() != index and index != 7:
                # self.once_notifications[j].hide()
                j += 1
                continue
            else:
                if self.permenant_notifications[i].get_adjusted_datetime() > self.once_notifications[j].get_adjusted_datetime():
                    self.show_noti(self.once_notifications[j])
                    j += 1
                else:
                    self.show_noti(self.permenant_notifications[i])
                    i += 1

        while i < len(self.permenant_notifications):
            if self.permenant_notifications[i].get_index() == index or index == 7:
                self.show_noti(self.permenant_notifications[i])
            i += 1

        while j < len(self.once_notifications):
            if self.once_notifications[j].get_index() == index or index == 7:
                self.show_noti(self.once_notifications[j])
            j += 1

    def connect_noti_to_ui(self, new_notification):
        ui_obj = Ui_notification_widget(QWidget())
        new_notification.attach_ui(ui_obj, self.update_notification_path_in_db, self.destroy_notification, self.change_noti_state_in_db, self.main_window)

    def show_noti(self, noti):
        try:
            layout = self.scrollArea_container.layout()
            noti.show(layout)
        except:
            pass

    def destroy_notification(self, notification):

        self.find_item_and_hide_it(notification.ui_obj.widget)
        
        self.delete_notification_from_db(notification)

        if notification in self.permenant_notifications:
            self.permenant_notifications.remove(notification)
        else:
            self.once_notifications.remove(notification)
        
        self.next_noti = None

        self.intiate_index()

        self.find_next_noti()

        self.decrease_total_noti_num()

    def find_item_and_hide_it(self, widget):
        layout = self.scrollArea_container.layout()
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item is not None and item.widget() is not None:
                if item.widget() == widget:
                    item.widget().hide()
                    item.widget().deleteLater()
                    item.widget().setParent(None)
                    break

    def clear_layout(self):
        layout = self.scrollArea_container.layout()
        while layout.count() != 0:
                item = layout.itemAt(0)
                layout.takeAt(0)
                item.widget().hide()

    def intialize_notification(self, is_permenant, is_before_adan, adan_index, seconds, date, duration, file_path, is_active):
        
        # adan_index is 1-6 (1-based)
        time = self.get_adan_time(adan_index)

        duration_in_seconds = 0

        if not is_before_adan:
            # Get duration based on notification index (1-6)
            duration_in_seconds = self.get_adan_duration(adan_index)

        new_notification = AdanNotification(is_before_adan, time, adan_index, seconds, file_path, date, duration, duration_in_seconds)

        self.position_notification(new_notification, is_permenant)

        self.connect_noti_to_ui(new_notification)

        if not is_active:
            new_notification.change_state(is_active)
            # set noti to be inactive
            new_notification.handle_button_click()

        self.increase_total_noti_num()

    def position_notification(self, notification, is_permenant):
        
        if is_permenant:
            target_lst = self.permenant_notifications
        else:
            target_lst = self.once_notifications
        
        i = 0
        while(i < len(target_lst)):
            if target_lst[i].get_adjusted_datetime() < notification.get_adjusted_datetime():
                i += 1
            else:
                break
        target_lst.insert(i, notification)

    def update_notis_and_intiate_index(self, new_adan_times):
        # update adans times
        self.update_adan_time(new_adan_times)
        # update notification
        self.update_notifications()
        # find next noti index in permenant
        self.intiate_index()
        # find next noti
        self.find_next_noti()

    def update_notifications(self):
        for noti in self.permenant_notifications:
            self.update_notification_time(noti)
            if noti.get_index() != 6:
                self.update_notification_date(noti)
        for noti in self.once_notifications:
            self.update_notification_time(noti)

    def update_notification_time(self, notification):
            updated_adan_time = self.get_adan_time(notification.get_index())
            notification.update_time(updated_adan_time)
    
    def update_notification_date(self, notification):
            curr_date = dt.datetime.now().date()
            notification.update_date(curr_date)
    
    def intiate_index(self):
            self.permenant_noti_index = 0
            for noti in self.permenant_notifications:
                # if dt.get_curr_time() > noti.get_adjusted_datetime():
                if self.curr_time > noti.get_adjusted_datetime():
                    self.permenant_noti_index += 1

            noti_num = len(self.permenant_notifications)
            if noti_num != 0 :
                self.permenant_noti_index = (self.permenant_noti_index % noti_num)
    
    def update_adan_time(self, new_adan_times):
            self.prayers_times = new_adan_times
    
    def get_adan_time(self, adan_index):
        """
        Get the time of an Adan.
        
        Args:
            adan_index (int): The index of the Adan (1-6)
            
        Returns:
            datetime: The time of the Adan
        """
        # Handle special case for Jomoaa (index 6)
        prayers_index = adan_index - 1
        # if adan_index == 6:
        #     prayers_index = 1  # Dohor's index in prayers_times
        
        if 0 <= prayers_index < len(self.prayers_times):
            return self.prayers_times[prayers_index]
        else:
            return None
    
    def choose_sound(self, widget):
            self.file_path = select_sound_file(widget)
 
    def wich_noti_next(self, curr_time):
            #  0 indicates self.permenant turn
            #  1 indicates self.once turn
            #  2 no notification 
            per_count = len(self.permenant_notifications)
            once_count = len(self.once_notifications)

            if once_count == per_count and per_count == 0:
                return 2
            elif once_count == 0 and per_count != 0:
                return 0
            elif once_count != 0 and per_count == 0:
                return 1

            compare_with_permenant = self.compare_datetimes(curr_time, self.permenant_notifications[self.permenant_noti_index])
            if not self.finished_all_per_noti_today(compare_with_permenant):
                if self.compare_datetimes(curr_time, self.once_notifications[0]) > compare_with_permenant :
                    return 0
            return 1
    
    def finished_all_per_noti_today(self, compared_noti_time):
            return compared_noti_time < dt.timedelta(days = 0, hours = 0, minutes = 0, seconds = 0)
    
    def compare_datetimes(self, curr_time, noti):
            return noti.get_adjusted_datetime() - curr_time
    
    def check_if_time_to_prepare(self, curr_time, notification):
            res = self.compare_datetimes(curr_time, notification)
            return True if (res < dt.timedelta(days = 0, hours = 0, minutes = 0, seconds = 7)) and (res > dt.timedelta(days = 0, hours = 0, minutes = 0, seconds = 0)) else False
    
    def check_if_time_to_play(self, curr_time, notification):
            res = self.compare_datetimes(curr_time, notification)
            return True if (res < dt.timedelta(days = 0, hours = 0, minutes = 0, seconds = 1)) and (res > dt.timedelta(days = 0, hours = 0, minutes = 0, seconds = 0)) else False
    
    def find_next_noti(self):
            res = self.wich_noti_next(self.curr_time)
            if res != 2:
                if res == 0:
                    self.curr_noti_type = 0
                    self.next_noti = self.permenant_notifications[self.permenant_noti_index]
                else:
                    self.curr_noti_type = 1
                    self.next_noti = self.once_notifications[0]
            else:
                self.curr_noti_type = -1
                self.next_noti = None
    
    def handel_time_changed(self, curr_time):
        
        # update self.curr_time
        self.update_curr_time(curr_time)

        # find next noti if not exist 
        if not self.next_noti:
            self.intiate_index()
            self.find_next_noti()

        if self.next_noti:  
            if self.check_if_time_to_play(curr_time, self.next_noti):
                if self.next_noti.activated():
                    # Create command with duration
                    command = PlayAudioCommand(
                        "NotificationManager", 
                        self.next_noti.get_file_path(),
                        duration=self.next_noti.get_duration()
                    )
                    
                    # ask player manager to play
                    self.mediator.notify(self, "request_playback", command)

                # find next notification
                if self.curr_noti_type:
                    # remove noti from once lst
                    self.once_notifications.pop(0)
                    self.decrease_total_noti_num()
                    self.delete_notification_from_db(self.next_noti)
                    self.clear_layout()
                    self.show_notifications()

                else:
                    # increase the permenant index by 1
                    self.permenant_noti_index += 1 
                    if self.permenant_noti_index == len(self.permenant_notifications):
                        self.permenant_noti_index = 0

                self.pre_adan_preparation_emitted = False
                self.find_next_noti()
            
            elif self.check_if_time_to_prepare(curr_time, self.next_noti) and not self.pre_adan_preparation_emitted:
                if self.next_noti.activated():
                    self.mediator.notify(self, "pre_adan_preparation")
                    self.pre_adan_preparation_emitted = True
    
    def handle_adan_duration_changed(self, new_duration, adan_index):
        """
        Handle when an Adan duration has changed.
        
        Args:
            new_duration (int): The new duration in milliseconds
            adan_index (int): The index of the Adan (0-4)

            act like jomoaa and dohor is the same
        """

        self.update_adan_duration(adan_index, new_duration)

        # Update all notifications that use this Adan
        # Convert from duration index (0-4) to notification index (1-5)
        notification_index = adan_index + 1
        
        # Also update Jomoaa notifications if Dohor duration changed
        jomoaa_needs_update = (adan_index == 1)  # Dohor's index in adans_duration
        
        for noti in self.permenant_notifications:
            if noti.get_index() == notification_index or (jomoaa_needs_update and noti.get_index() == 6):
                if not noti.is_before_adan:
                    # Get the appropriate duration based on notification index
                    new_duration_seconds = self.get_adan_duration(noti.get_index())
                    
                    # update noti obj
                    noti.update_adan_duration(new_duration_seconds)
                    # update noti in db
                    self.update_notification_in_db(noti, "adan_duration", new_duration_seconds)
        
        for noti in self.once_notifications:
            if noti.get_index() == notification_index or (jomoaa_needs_update and noti.get_index() == 6):
                if not noti.is_before_adan:
                    # Get the appropriate duration based on notification index
                    new_duration_seconds = self.get_adan_duration(noti.get_index())

                    # update noti obj
                    noti.update_adan_duration(new_duration_seconds)
                    # update noti in db
                    self.update_notification_in_db(noti, "adan_duration", new_duration_seconds)
