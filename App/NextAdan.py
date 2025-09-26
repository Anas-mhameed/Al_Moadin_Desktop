import datetime as dt
from PySide6.QtCore import QObject, Signal
from Adan import Adan

class AdanSignal(QObject):

    adan_time = Signal(Adan)
    # prepare_for_adan = Signal()
    force_stop_adan = Signal()
    open_mic = Signal()
    possible_not_adan_time_signal = Signal()
    update_adan_times_signal = Signal()

    def __init__(self):
        super().__init__()

class NextAdan() :

    adan_signal = AdanSignal()
    adan_time_signal = adan_signal.adan_time
    # prepare_for_adan_signal = adan_signal.prepare_for_adan
    force_stop_adan = adan_signal.force_stop_adan
    possible_not_adan_time_signal = adan_signal.possible_not_adan_time_signal
    update_adan_times_signal = adan_signal.update_adan_times_signal

    def __init__(self, five_prayers, adan_name_label, remaining_time_label) :

        self.curr_day = ""
        self.adan_index = -1
        self.next_adan = None
        self.previous_adan = None

        self.prepare_adan_signal_emitted = False

        self.pre_adan_sound_emitted = False

        self.mediator = None

        self.time_to_find_next_adan = False
        self.automatic_find_next_adan_counter = 0

        self.curr_time = dt.datetime.now()
        self.curr_day = self.curr_time.strftime('%A')

        if self.curr_day == "Friday" :
            self.curr_day = "الجمعة"

        self.remaining_time = dt.timedelta(seconds=0)
        self.adan_name_ui = adan_name_label
        self.remaining_time_ui = remaining_time_label

        self.called_prepare_for_adan = False
        self.five_prayers = five_prayers

    def update_five_prayers(self, new_prayers):
        self.five_prayers = new_prayers

    def update_curr_day(self, day):
        self.curr_day = day

    def get_next_adan_name(self):
        return self.next_adan.get_adan_name()

    def set_praper_for_adan_call(self, state):
        self.called_prepare_for_adan = state

    def intiate_next_adan(self):

        for adan in self.five_prayers:
                
            next_time = adan.get_adan_time()

            if next_time > self.curr_time:

                self.next_adan = adan  
                self.adan_index = self.five_prayers.index(adan)  
                return

        self.next_adan = self.five_prayers[0]
        self.adan_index = 0

    def calc_remaining_time(self):
        
        temp = self.next_adan.get_adan_time() - self.curr_time
        temp1 = temp + dt.timedelta(seconds=1)
 
        self.remaining_time = temp1 - dt.timedelta(microseconds= temp1.microseconds)

    def formate_time(self, time):
        hours = time.seconds // 3600
        minutes = (time.seconds % 3600) // 60
        seconds = time.seconds % 60

        # Format the time difference in the desired format
        formatted_time_difference = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        return formatted_time_difference

    def update_ui(self):
        self.remaining_time_ui.setText(self.formate_time(self.remaining_time))
        if self.curr_day == "الجمعة" and self.next_adan.get_adan_name() == "الظهر":
            self.adan_name_ui.setText("الجمعة")
        else :
            self.adan_name_ui.setText(self.next_adan.get_adan_name())

    def time_to_update_adan_times(self):
        if self.next_adan.get_adan_name() == "العشاء" and self.compare_with_timedelta(0):
            return True
        return False

    def dont_prepare_yet(self):
        return (self.remaining_time > dt.timedelta(days = 0, hours = 0, minutes = 0, seconds = 30)) and self.remaining_time < dt.timedelta(days = 0, hours = 0, minutes = 1, seconds = 30)

    def compare_with_timedelta(self, sec, sec1 = None):

        remaining_time = self.remaining_time

        zero_timedelta = dt.timedelta(days = 0, hours = 0, minutes = 0, seconds = sec, microseconds= remaining_time.microseconds)
        
        if sec1:
            temp_timedelta = dt.timedelta(days = 0, hours = 0, minutes = 0, seconds = sec1, microseconds= remaining_time.microseconds)
            return (self.remaining_time > zero_timedelta ) and (self.remaining_time < temp_timedelta)
        else:
            return (remaining_time == zero_timedelta)
        
    def update_curr_time(self, new_curr_time):
        self.curr_time = new_curr_time

    def find_next_adan(self):
        self.next_adan = self.five_prayers[self.adan_index]

    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    def handle_time_updated(self, curr_time):

        self.update_curr_time(curr_time)

        self.automatic_find_next_adan_counter += 1

        if self.next_adan == None or self.time_to_find_next_adan or self.automatic_find_next_adan_counter == 30:
            print("IM IN -------------------------------------")
            self.intiate_next_adan()
            self.time_to_find_next_adan = False
            self.automatic_find_next_adan_counter = 0

        if self.previous_adan and self.previous_adan == self.next_adan.get_adan_name():

            self.previous_adan = self.five_prayers[(self.adan_index - 1) % 5 ].get_adan_name()

            self.mediator.notify("NextAdan", "current_adan_changed_to_previous")

        self.calc_remaining_time()

        self.update_ui()

        if self.compare_with_timedelta(0):
            # emit a signal to start adan
            self.adan_time_signal.emit(self.next_adan)
            self.previous_adan = self.next_adan.get_adan_name()

            self.time_to_find_next_adan = True

        elif self.compare_with_timedelta(0, 30) and not self.prepare_adan_signal_emitted:
            self.mediator.notify("NextAdan", "prepare_for_adan")
            self.prepare_adan_signal_emitted = True
        
        elif not self.compare_with_timedelta(0, 30) and self.prepare_adan_signal_emitted:
            self.mediator.notify("NextAdan", "allow_playback")
            self.prepare_adan_signal_emitted = False 
        
        if self.compare_with_timedelta(2, 10) and not self.pre_adan_sound_emitted and self.next_adan.check_state():
            self.mediator.notify("NextAdan", "pre_adan_preparation")
            self.pre_adan_sound_emitted = True    

        elif not self.compare_with_timedelta(2, 10) and self.pre_adan_sound_emitted:
            self.pre_adan_sound_emitted = False