# from abc import ABC, abstractmethod
from datetime import datetime as dt, timedelta
from PySide6.QtWidgets import QWidget
from ShowDialog import ShowDialog
from Sound import Sound

class Notification():

    def __init__(self, time, file_path, date = None, duration = 0):
        self.time = time
        self.duration = duration
        self.file_path = file_path
        # self.date = date
    
    def update_time(self, time):
        self.time = time

    def update_duration(self, new_duration):
        self.duration = new_duration

    def update_date(self, new_date):
        new_year = new_date.year
        new_month = new_date.month
        new_day = new_date.day
        self.time = self.time.replace(year=new_year, month=new_month, day=new_day)


    def update_sound(self, new_sound_path):
        self.file_path = new_sound_path
    
    def get_file_path(self):
        return self.file_path

    def noti_play_time(self):
        return self.time

    def get_duration(self):
        return self.duration

class AdanNotification(Notification):

    def __init__(self, is_before_adan, time, adan_index, minutes, file_path, date=None, duration=0):
        
        updated_time = time

        if date:
            year = date.year()
            month = date.month()
            day = date.day()

            updated_time = time.replace(year= year, month= month, day= day)
        
        super().__init__(updated_time, file_path, date, duration)

        if adan_index > 6 or adan_index < 1:
            raise IndexError
        
        self.is_before_adan = is_before_adan
        self.adan_index = adan_index
        self.minutes = minutes
        self.adjust_datetime_minutes(self.minutes)
        self.is_activated = True
        self.index_in_layout = -1

    def update_date(self, new_date):
        super().update_date(new_date)
        self.adjust_datetime_minutes(self.minutes)
        self.update_ui()

    def activated(self):
        return self.is_activated

    def get_minutes(self):
        return self.minutes

    def get_index(self):
        return self.adan_index

    def set_activated(self, bol):
        self.is_activated = bol

    def update_ui(self):
        self.ui_obj.noti_time_label.setText(f"{self.get_formatted_date()[1].strftime('%H:%M')}")
        self.ui_obj.noti_date_label.setText(f"{self.get_formatted_date()[0]}")

    def update_time(self, new_time):
        super().update_time(new_time)
        self.adjust_datetime_minutes(self.minutes)
        self.update_ui()

    def noti_play_time(self):
        return self.adjusted_datetime 

    def adjust_datetime_minutes(self, minute_offset):
        # Extract the original hours and minutes
        original_hours = self.time.hour
        original_minutes = self.time.minute
        
        day = self.time.day
        month = self.time.month
        year = self.time.year

        # if self.date:
        #     day = self.date.day()
        #     month = self.date.month()
        #     year = self.date.year()

        # total_minutes = original_minutes
        total_minutes = original_minutes
        seconds = 0

        if minute_offset >= 1:
            # Calculate the total minutes
            if self.is_before_adan:
                total_minutes -= minute_offset
            else:
                total_minutes += minute_offset
        else:
            seconds = minute_offset * 60
        # Determine the new hours and minutes
        new_hours, new_minutes = divmod(total_minutes, 60)

        # Adjust the date and time based on the new hours and minutes
        self.adjusted_datetime = dt(year, month, day, hour=original_hours + new_hours, minute=new_minutes, second= int(seconds))

    def get_adjusted_datetime(self):
        return self.adjusted_datetime

    def get_adjusted_time(self):
        return (self.adjusted_datetime.hour, self.adjusted_datetime.minute, self.adjusted_datetime.second)

    def show(self, layout):
        layout.addWidget(self.ui_obj.widget)
        self.ui_obj.widget.show()
    
    def dettach(self):
        self.ui_obj = None

    def update_index_in_layout(self, index):
        self.index_in_layout = index

    def get_index_in_layout(self):
        return self.index_in_layout

    def attach_ui(self, ui_obj, update_noti_in_db, delete_noti_handler, change_noti_state_in_db, main_window):

        self.update_noti_in_db = update_noti_in_db
        self.delete_noti_handler = delete_noti_handler
        
        self.change_noti_state_in_db = change_noti_state_in_db

        self.ui_obj = ui_obj
        self.ui_obj.activate_noti_button.clicked.connect(self.handle_button_click)
        self.ui_obj.show_noti_button.clicked.connect(lambda: self.show_dialog_info(main_window))
        formatted_data = self.get_formatted_date()

        self.ui_obj.noti_date_label.setText(f"{formatted_data[0]}")
        self.ui_obj.noti_time_label.setText(f"{formatted_data[1].strftime("%H:%M")}")
        self.ui_obj.noti_adan_label.setText(f"{formatted_data[2]}\n{formatted_data[3]}")

    def change_state(self, state):
        self.ui_obj.activate_noti_button.setChecked(state)

    def handle_button_click(self):
        if self.ui_obj.activate_noti_button.isChecked():
            self.ui_obj.is_noti_active_label.setText("مفعل")
            self.set_activated(True)
        else:
            self.ui_obj.is_noti_active_label.setText("غير مفعل")
            self.set_activated(False)

        self.change_noti_state_in_db(self, int(self.is_activated))
            

    def get_formatted_date(self):
        adan_list = ["الفجر", "الظهر", "العصر", "المغرب", "العشاء", "الجمعة"]
        
        time = self.adjusted_datetime.time() 
        date = self.adjusted_datetime.date()

        adan = adan_list[self.adan_index - 1]

        when = "قبل" if self.is_before_adan else "بعد"

        minutes = self.minutes
        if self.minutes < 1 :
            min_sec = "ثواني"
            minutes *= 60
        elif self.minutes > 10:
            min_sec = "دقيقة"
        else:
            min_sec = "دقائق"

        return (date, time, f"{when} اذان {adan}", f"ب {int(minutes)} {min_sec}") 

    def __str__(self):
        adans = ["فجر", "ظهر", "عصر", "مغرب", "عشاء", "الجمعة"]
        
        prefix = "دقائق"
        minutes = self.minutes
        if self.minutes < 1:
            prefix = "ثواني"
            minutes = minutes * 60
        elif self.minutes < 11:
            prefix = "دقيقة"
        
        return f"قبل صلاة ال{adans[self.get_index() - 1]} ب {minutes} {prefix}"

    def show_dialog_info(self, main_window):
        self.show_dialog = ShowDialog(self.get_adjusted_datetime(), str(self), self.edit_file_path, self.save_updates, lambda: self.delete_noti(), parent=main_window)
        self.show_dialog.show()

    def edit_file_path(self):
        sound = Sound()
        sound.select_sound_file(QWidget())
        return sound.get_file_path()

    def save_updates(self, new_file_path):
        if new_file_path != "":
            self.file_path = new_file_path
        #  update db
        self.update_noti_in_db(self, self.file_path)

    def delete_noti(self):
        self.delete_noti_handler(self)
