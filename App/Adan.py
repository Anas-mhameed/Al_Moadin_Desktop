
class Adan:

    def __init__(self, adan_name_label, adan_time, time_label_ui, active=False):
        
        self.name_label = adan_name_label
        self.name = adan_name_label.text()
        self.original_time = adan_time
        self.time = adan_time
        self.time_label_ui = time_label_ui
        self.is_active = active

        # self.update_ui()
    def get_adan_time(self):
        return self.time
    
    def get_adan_name(self):
        return self.name

    def get_original_time(self):
        return self.original_time

    def update_original_time(self, new_original_time):
        self.original_time = new_original_time

    def update_time(self, new_time):
        self.time = new_time
    
    def check_state(self):
        return self.is_active

    def change_state(self, is_checked):
        self.is_active = is_checked
    
    def update_ui(self, formate):
        #update adan time label
        self.time_label_ui.setText(self.time.strftime(formate))

    def set_next_adan_ui(self):
        # self.name_label.setText("blabla")
        self.name_label.setStyleSheet("color: rgb(8, 148, 108);")

    def remove_next_adan_ui(self):
        self.name_label.setStyleSheet("color: black;")
