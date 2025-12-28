import datetime as dt
from hijri_converter import convert
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal, QObject
from ResourceFile import resource_path
from PySide6.QtGui import QFontDatabase, QFont

hijri_months = ["محرم","صفر","ربيع الأول","ربيع الآخر","جمادى الأولى","جمادى الآخرة","رجب","شعبان","رمضان","شوال","ذو القعدة","ذو الحجة"]
my_calendar = ["الإثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]

class ClickableLabel(QLabel):
    # Define a custom signal
    clicked = Signal()

    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Noto_Kufi_Arabic/static/NotoKufiArabic-SemiBold.ttf"))
        self.kufi_regular_font_family = QFontDatabase.applicationFontFamilies(self.font_id)[0]
        self.kufi_font_24 = QFont(self.kufi_regular_font_family, 24)
        self.kufi_font_24.setBold(True)
        self.setFont(self.kufi_font_24)

        self.setStyleSheet("""
        color: black;
        """)

    def mousePressEvent(self, event):
        """Override the mousePressEvent to emit the clicked signal."""
        self.clicked.emit()

class TimeSignal(QObject):

    time_updated = Signal(dt.datetime)
    new_day = Signal(str)

    def __init__(self):
        super().__init__()

class Time():

    time_signal = TimeSignal()

    time_updated = time_signal.time_updated

    def __init__(self, mediator, am_pm_label, seconds_label, am_pm_frame, time_lower_widget, time_label, day_label, date_label):
        
        self.first_time_firestore_update = True

        self.mediator = None
        mediator.register("Time", self)

        self.time_formate = "%I:%M:%S %p"

        self.am_pm_frame = am_pm_frame
        self.am_pm_label = am_pm_label
        self.seconds_label = seconds_label
        font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Chivo_Mono/ChivoMono-VariableFont_wght.ttf"))
        
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, 44)
        font.setWeight(QFont.Bold)
        self.seconds_label.setFont(font)
        self.am_pm_label.setFont(font)

        self.time_lower_widget = time_lower_widget
        layout = self.time_lower_widget.layout()

        self.higri_date_label = ClickableLabel()
        
        layout.insertWidget(0, self.higri_date_label)

        self.factor = 0
        self.higri_date_label.clicked.connect(self.hijri_label_click_handel)

        self.update_time()
        self.update_date()
        self.update_day()

        self.previous_date = None

        self.time_label = time_label
        self.day_label = day_label
        self.date_label = date_label 

        self.initate_labels()

    
    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator
    
    def update_factor(self):
        if self.factor == 3:
            self.factor = -3
        else:
            self.factor += 1

    def initate_labels(self):
        self.day_label.setText(self.day)
        self.date_label.setText(self.date.strftime("%d/%m/%Y"))
        self.higri_date_label.setText(self.set_hijri_date())

    def update_time(self):
        self.curr_dt = dt.datetime.now()
    
    def update_date(self):
        self.date = dt.date.today()

    def update_day(self):
        self.day = my_calendar[self.date.weekday()]

    def get_curr_time(self):
        return self.curr_dt
    
    def get_day(self):
        return self.day

    def gregorian_to_hijri(self, year, month, day):
        hijri_date = convert.Gregorian(year, month, day).to_hijri()
        return hijri_date

    def set_hijri_date(self):
        hijri_date = self.gregorian_to_hijri(self.date.year, self.date.month, self.date.day)

        day = hijri_date.day + self.factor
        month = hijri_date.month
        year = hijri_date.year

        if day > 30:
            day -= 30
            month += 1
        elif day < 1:
            day = 30 + day
            month -= 1
        
        if month > 12:
            month -= 12
            year += 1
        elif month < 1:
            month = 12
            year -= 1

        return f"{ day } { hijri_months[ month - 1 ] } { year }"
    
    def handle_next_day(self):
        self.update_date()
        self.update_day()
        
    def check_if_new_day(self):
        if self.date != self.curr_dt.date():
            self.handle_next_day()
            return True
        return False

    def check_if_jomoaa_passed(self):
        if self.day == my_calendar[5]:
            if self.curr_dt.time() > dt.time(0,0,0) and self.curr_dt.time() < dt.time(0,0,1):
                return True
        return False

    def update_time_formate(self, new_formate):
        self.time_formate = new_formate

    
    def update_ui(self):
        if self.time_formate == "%I:%M:%S %p":
            self.am_pm_frame.show()
            self.time_label.setText(self.curr_dt.strftime("%I:%M"))

            self.seconds_label.setText(self.curr_dt.strftime(":%S"))
            self.am_pm_label.setText(self.curr_dt.strftime("%p"))

        else:
            self.am_pm_frame.hide()
            self.time_label.setText(self.curr_dt.strftime(self.time_formate))

    def hijri_label_click_handel(self):
        self.update_factor()
        new_hijri = self.set_hijri_date()
        self.higri_date_label.setText(new_hijri)
        if self.mediator:
            self.mediator.notify(self, "send_firebase_update", { 'hijriDate': new_hijri })

    def update_day_date_hijri(self):
        self.day_label.setText(self.day)
        self.date_label.setText(self.date.strftime("%d/%m/%Y"))
        self.higri_date_label.setText(self.set_hijri_date())

    def run(self):
        self.update_time()
        self.update_ui()

        self.time_updated.emit(self.curr_dt)

        is_new_day = self.check_if_new_day()

        if is_new_day:
            self.update_day_date_hijri()

            if self.mediator:
                self.mediator.notify(self, "new_day_event", self.day)
                self.mediator.notify(self, "send_firebase_update", { 'day': self.day, 'hijriDate': self.higri_date_label.text() })

        if self.first_time_firestore_update:
            self.first_time_firestore_update = False
            if self.mediator:
                self.mediator.notify(self, "send_firebase_update", { 'day': self.day, 'hijriDate': self.higri_date_label.text() })