from Runnable import Runnable
from DatabaseManager import DatabaseManager  # Import DatabaseManager directly

class GeneralSettings():

    def __init__(self, mobile_connection_code, zigbee_checkbox, pre_adan_sound_checkbox, masjed_name_label, masjed_name_input, city_input, quds_time_diff_input, winter_summer_buttons, time_formate_buttons, runnable_manager, *args, **kwargs):

        self.database_manager = DatabaseManager()  # Initialize DatabaseManager directly

        self.mediator = None

        self.masjed_name_label = masjed_name_label
        self.masjed_name_input = masjed_name_input
        self.city_input = city_input
        self.quds_time_diff_input = quds_time_diff_input
        self.summer_winter_buttons = winter_summer_buttons
        self.time_formate_buttons = time_formate_buttons
        self.pre_adan_sound_checkbox = pre_adan_sound_checkbox
        self.zigbee_checkbox = zigbee_checkbox
        
        self.mobile_connection_code = mobile_connection_code
        self.mobile_connection_code.editingFinished.connect(self.update_mobile_connection_code)

        self.runnable_manager = runnable_manager

        data = self.database_manager.get_settings_data()

        self.msjed_name = data[0][1]
        self.city = data[1][1]

        self.update_ui()

        self.quds_time_diff = int(data[2][1])

        self.is_summer_time = bool(int(data[3][1]))

        self.is_24_formate = bool(int(data[4][1]))

        self.time_formate = ("%H:%M:%S", "%H:%M")

        self.is_pre_adan_sound_activated = bool(int(data[5][1]))
        
        # intiate pre adan sound checkbox to db value
        self.pre_adan_sound_checkbox.setChecked(self.is_pre_adan_sound_activated)

        self.zigbee_checkbox.setChecked(not self.is_pre_adan_sound_activated)

        # intiate quds time diff to db value
        self.quds_time_diff_input.setValue(self.quds_time_diff)

        # intiate summer winter buttons to db values
        self.summer_winter_buttons[0].setChecked(self.is_summer_time)

        self.summer_winter_buttons[1].setChecked(not self.is_summer_time)

        # intiate time formate buttons to db values
        self.time_formate_buttons[0].setChecked(not self.is_24_formate)

        self.time_formate_buttons[1].setChecked(self.is_24_formate)

        self.masjed_name_input.textChanged.connect(lambda: self.update_masjed_name())
        self.city_input.textChanged.connect(lambda: self.update_city())
        self.quds_time_diff_input.valueChanged.connect(lambda: self.change_quds_diff())
        self.summer_winter_buttons[0].clicked.connect(lambda: self.switch_summer_winter(index=0))
        self.summer_winter_buttons[1].clicked.connect(lambda: self.switch_summer_winter(index=1))
        self.time_formate_buttons[0].clicked.connect(lambda: self.change_time_formate(0))
        self.time_formate_buttons[1].clicked.connect(lambda: self.change_time_formate(1))
        self.pre_adan_sound_checkbox.toggled.connect(lambda checked: self.change_pre_adan_sound_state(checked))
        self.zigbee_checkbox.toggled.connect(lambda checked: self.change_zigbee_state(checked))

    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

    def update_mobile_connection_code(self):
        new_code = self.mobile_connection_code.text()
        
        if new_code == "":
            return

        # save to db
        self.save_to_db('mobile_connection_code', new_code)
        
        self.mobile_connection_code.clear()

    def update_masjed_name(self, masjed_name = None):
        if masjed_name is None:
            if self.masjed_name_input.text() != "":
                temp = self.masjed_name_input.text()
            else:
                temp = "اسم المسجد"
        else :
            temp = masjed_name

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

    def update_city(self, city = None):
        if city is None:
            if self.city_input.text() != "":
                temp = self.city_input.text()
            else:
                temp = "البلد"
        else :
            temp = city

        self.city = temp.rstrip()

        # save to db
        self.save_to_db('city', self.city)

        self.update_ui()

    def change_quds_diff(self, quds_diff = None):
        if quds_diff is None:
            self.quds_time_diff = self.quds_time_diff_input.value()
        else:
            self.quds_time_diff_input.setValue(quds_diff)
            return 

        # save to db 
        self.save_to_db('quds_time_diff', str(self.quds_time_diff))
        
        if self.mediator:
            self.mediator.notify(self, "quds_diff_time_changed", self.quds_time_diff,self.is_summer_time)

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
                
                if self.mediator:
                    self.mediator.notify(self, "summer_timing_changed", self.is_summer_time)

                temp = '1'

            self.summer_winter_buttons[0].setChecked(True)
            self.summer_winter_buttons[1].setChecked(False)

        else:

            if self.is_summer_time:

                self.is_summer_time = False

                if self.mediator:
                    self.mediator.notify(self, "summer_timing_changed", self.is_summer_time)

                temp = '0'

            self.summer_winter_buttons[0].setChecked(False)
            self.summer_winter_buttons[1].setChecked(True)

        # save to db        
        self.save_to_db('is_summer_time', temp)

    def set_time_formate(self):

        if self.is_24_formate :
            self.time_formate = ("%H:%M:%S", "%H:%M")
        else:
            self.time_formate = ("%I:%M:%S %p", "%I:%M %p")


        if self.mediator:
            self.mediator.notify(self, "time_formate_changed", self.time_formate[0], self.time_formate[1])
        
    def change_pre_adan_sound_state(self, checked):
        """Handle pre-adan sound checkbox toggle"""
        # Temporarily disconnect signals to prevent infinite recursion
        self.zigbee_checkbox.toggled.disconnect()

        # Update internal state
        self.is_pre_adan_sound_activated = checked

        # Update the other checkbox (zigbee should be opposite)
        self.zigbee_checkbox.setChecked(not checked)

        # Save to database
        self.save_to_db('is_pre_adan_sound_activated', '1' if checked else '0')

        # Notify mediator if available
        if self.mediator:
            self.mediator.notify(self, "pre_adan_sound_state_changed", checked)

        # Reconnect the signal
        self.zigbee_checkbox.toggled.connect(lambda checked: self.change_zigbee_state(checked))

    def change_zigbee_state(self, checked):

        """Handle zigbee checkbox toggle"""
        # Temporarily disconnect signals to prevent infinite recursion
        self.pre_adan_sound_checkbox.toggled.disconnect()

        # Update internal state (zigbee is opposite of pre_adan_sound)
        self.is_pre_adan_sound_activated = not checked

        # Update the other checkbox (pre_adan_sound should be opposite)
        self.pre_adan_sound_checkbox.setChecked(not checked)

        # Save to database (save the pre_adan_sound state, not zigbee state)
        self.save_to_db('is_pre_adan_sound_activated', '0' if checked else '1')

        # Notify mediator if available
        if self.mediator:
            self.mediator.notify(self, "pre_adan_sound_state_changed", not checked)

        # Reconnect the signal
        self.pre_adan_sound_checkbox.toggled.connect(lambda checked: self.change_pre_adan_sound_state(checked))

    def update_ui(self):
        self.masjed_name_label.setText(f"{self.msjed_name} - {self.city}")

    def collect_settings(self):
        settings = {
            'is_summer_formate' : self.is_summer_time,
            'quds_diff_time' : self.quds_time_diff,
            'time_formate' : self.time_formate,
            'is_pre_adan_sound_activated' : self.is_pre_adan_sound_activated
            }
        return settings

    # def handle_firebase_update(self, data):

    #     masjed_name = data["name"]
    #     city = data["city"]

    #     quds_diff = data["qudsDifferenceTime"]
    #     summer_time = data["summerTime"]

    #     self.set_masjed_name_input(masjed_name)
    #     self.set_city_input(city)

    #     self.set_quds_diff_input(quds_diff)
    #     self.switch_summer_winter(0 if summer_time else 1)

    # def set_quds_diff_input(self, value):
    #     self.quds_time_diff_input.setValue(value)
    
    # def set_masjed_name_input(self, value):
    #     self.masjed_name_input.setText(value)
    
    # def set_city_input(self, value):
    #     self.city_input.setText(value)