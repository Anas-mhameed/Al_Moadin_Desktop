from Runnable import Runnable
from PySide6.QtCore import QObject, Signal
from DatabaseManager import DatabaseManager  # Import DatabaseManager directly

class SettingsSignals(QObject):
    
    # adan_time_updated = Signal(object)

    adan_time_formate_signal = Signal(str)
    time_formate_signal = Signal(str)
    summer_timing_signal = Signal(bool)
    quds_diff_signal = Signal(int)

    def __init__(self):
        super().__init__()


class GeneralSettings():

    settings_signals = SettingsSignals()
    
    time_formate_changed = settings_signals.time_formate_signal
    adan_time_formate_changed = settings_signals.adan_time_formate_signal
    summer_timing_changed = settings_signals.summer_timing_signal
    quds_diff_changed = settings_signals.quds_diff_signal

    def __init__(self, masjed_name_label, masjed_name_input, city_input, quds_time_diff_input, winter_summer_buttons, time_formate_buttons, runnable_manager, *args, **kwargs):

        self.database_manager = DatabaseManager()  # Initialize DatabaseManager directly

        self.masjed_name_label = masjed_name_label
        self.masjed_name_input = masjed_name_input
        self.city_input = city_input
        self.quds_time_diff_input = quds_time_diff_input
        self.summer_winter_buttons = winter_summer_buttons
        self.time_formate_buttons = time_formate_buttons

        self.runnable_manager = runnable_manager

        data = self.database_manager.get_settings_data()

        self.msjed_name = data[0][1]
        self.city = data[1][1]

        self.update_ui()

        self.quds_time_diff = int(data[2][1])

        self.is_summer_time = bool(int(data[3][1]))

        self.is_24_formate = bool(int(data[4][1]))

        self.set_time_formate()

        # intiate quds time diff to db value
        self.quds_time_diff_input.setValue(self.quds_time_diff)

        # intiate summer winter buttons to db values
        self.summer_winter_buttons[0].setChecked(self.is_summer_time)

        self.summer_winter_buttons[1].setChecked(not self.is_summer_time)

        # intiate time formate buttons to db values
        self.time_formate_buttons[0].setChecked(not self.is_24_formate)

        self.time_formate_buttons[1].setChecked(self.is_24_formate)

        # self.is_24_formate = self.summer_winter_buttons[1].isChecked()

        # self.time_handling_functions = []

        self.masjed_name_input.textChanged.connect(lambda: self.update_masjed_name())
        self.city_input.textChanged.connect(lambda: self.update_city())
        self.quds_time_diff_input.valueChanged.connect(lambda: self.change_quds_diff())
        self.summer_winter_buttons[0].clicked.connect(lambda: self.switch_summer_winter(index=0))
        self.summer_winter_buttons[1].clicked.connect(lambda: self.switch_summer_winter(index=1))
        self.time_formate_buttons[0].clicked.connect(lambda: self.change_time_formate(0))
        self.time_formate_buttons[1].clicked.connect(lambda: self.change_time_formate(1))

    def update_masjed_name(self):
        temp = self.masjed_name_input.text() if self.masjed_name_input.text() != "" else "اسم المسجد"

        self.msjed_name = temp.rstrip()
        
        # save to db
        self.save_to_db('masjed_name',self.msjed_name)

        self.update_ui()

    def save_to_db(self, row_name, value):

        def temp_func(func):
            if func():
                self.database_manager.update_settings(row_name, value)
        
        runnable = Runnable(temp_func)
        self.runnable_manager.runTask(runnable)

    def update_city(self):
        temp = self.city_input.text() if self.city_input.text() != "" else "البلد"

        self.city = temp.rstrip()

        # save to db
        self.save_to_db('city', self.city)

        self.update_ui()

    # def set_handle_timing_functions(self, functions_list):
    #     self.time_handling_functions = functions_list

    #     self.time_handling_functions[0](True)

    #     if not self.is_summer_time:
    #         self.time_handling_functions[0](self.is_summer_time)

    #     self.time_handling_functions[1](self.quds_time_diff, self.is_summer_time)

    def change_quds_diff(self):
        self.quds_time_diff = self.quds_time_diff_input.value()

        # save to db 
        self.save_to_db('quds_time_diff', str(self.quds_time_diff))

        self.quds_diff_changed.emit(self.quds_time_diff)

        # self.time_handling_functions[1](self.quds_time_diff, self.is_summer_time)

    def change_time_formate(self, index):
        
        temp = '0'

        if index == 0:
            
            self.is_24_formate = False
            
            temp = '0'

            self.time_formate_buttons[0].setChecked(True)
            self.time_formate_buttons[1].setChecked(False)

        else:

            self.is_24_formate = True

            temp = '1'

            self.time_formate_buttons[0].setChecked(False)
            self.time_formate_buttons[1].setChecked(True)

        self.set_time_formate()

        # save to db
        self.save_to_db('time_formate',temp)
       
    def switch_summer_winter(self, index):

        temp = '1'
        if index == 0:

            if self.is_summer_time == False: 

                self.is_summer_time = True
                
                self.summer_timing_changed.emit(self.is_summer_time)

                temp = '1'

                # self.time_handling_functions[0](self.is_summer_time)

            self.summer_winter_buttons[0].setChecked(True)
            self.summer_winter_buttons[1].setChecked(False)

        else:

            if self.is_summer_time:

                self.is_summer_time = False

                self.summer_timing_changed.emit(self.is_summer_time)

                temp = '0'

                # self.time_handling_functions[0](self.is_summer_time)

            self.summer_winter_buttons[0].setChecked(False)
            self.summer_winter_buttons[1].setChecked(True)

        # save to db        
        self.save_to_db('is_summer_time', temp)

    def set_time_formate(self):

        if self.is_24_formate :
            self.time_formate = ("%H:%M:%S", "%H:%M")
        else:
            self.time_formate = ("%I:%M:%S %p", "%I:%M %p")

        # emit time formate changed
        self.time_formate_changed.emit(self.time_formate[0])
        self.adan_time_formate_changed.emit(self.time_formate[1])

    def update_ui(self):
        self.masjed_name_label.setText(f"{self.msjed_name} - {self.city}")

    def send_all_settings_to_adan_manager(self):
        self.summer_timing_changed.emit(self.is_summer_time)
        self.quds_diff_changed.emit(self.quds_time_diff)

        self.adan_time_formate_changed.emit(self.time_formate[1])

