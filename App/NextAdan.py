import datetime as dt

class NextAdan() :

    def __init__(self, five_prayers, set_not_adan_time, curr_time, adan_name_label, remaining_time_label, start_adan_func, prepare_for_adan) :
        
        self.set_not_adan_time = set_not_adan_time
        self.curr_time = curr_time
        self.next_adan = ""
        self.remaining_time = dt.timedelta(seconds=0)
        self.adan_name_ui = adan_name_label
        self.remaining_time_ui = remaining_time_label
        self.start_adan_func = start_adan_func
        self.prepare_for_adan = prepare_for_adan

        self.called_prepare_for_adan = False

        self.find_next_adan(five_prayers)
        # print(self.next_adan.get_adan_name())
        self.calc_remaining_time()
        self.update_ui()
    
    def get_next_adan_name(self):
        return self.next_adan.get_adan_name()

    def set_praper_for_adan_call(self, state):
        self.called_prepare_for_adan = state

    def find_next_adan(self, prayers):
        self.next_adan = prayers[0]

        for adan in prayers:
                
            next_time = adan.get_adan_time()

            if next_time > self.curr_time.get_curr_time():

                self.next_adan = adan    
                return

    def calc_remaining_time(self):
        self.remaining_time = self.next_adan.get_adan_time() - self.curr_time.get_curr_time()

    def formate_time(self, time):
        hours = time.seconds // 3600
        minutes = (time.seconds % 3600) // 60
        seconds = time.seconds % 60

        # Format the time difference in the desired format
        formatted_time_difference = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        return formatted_time_difference

    def update_ui(self):
        self.remaining_time_ui.setText(self.formate_time(self.remaining_time))
        if self.curr_time.get_day() == "الجمعة" and self.next_adan.get_adan_name() == "الظهر":
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
        if sec1:
            one_timedelta = dt.timedelta(days = 0, hours = 0, minutes = 0, seconds = sec1)
        else:
            one_timedelta = dt.timedelta(days = 0, hours = 0, minutes = 0, seconds = sec + 1)

        zero_timedelta = dt.timedelta(days = 0, hours = 0, minutes = 0, seconds = sec)

        return (self.remaining_time > zero_timedelta) and (self.remaining_time < one_timedelta)
    
    def run(self, prayers):
    
        self.calc_remaining_time()

        if self.compare_with_timedelta(0) :
            self.start_adan_func(self.next_adan)
            self.next_adan.remove_next_adan_ui()

        elif self.compare_with_timedelta(0, 30) and not self.called_prepare_for_adan:
            self.prepare_for_adan()
            self.set_praper_for_adan_call(True)

        elif self.dont_prepare_yet() :
            self.set_not_adan_time()
        #     print("in 30")

        self.find_next_adan(prayers)

        self.update_ui()

