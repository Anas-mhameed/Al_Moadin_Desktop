
class SpinBoxTrack:

    def __init__(self, spinbox):
        
        self.spinbox = spinbox
        self.previous_value = self.spinbox.value()
        self.curr_suffix = self.spinbox.suffix() 
        self.curr_maximum = self.spinbox.maximum()
        self.curr_minimum = self.spinbox.minimum()

        self.spinbox.valueChanged.connect(self.on_value_changed)

    def on_value_changed(self, value):

        if value == 60 and self.previous_value < 60 and self.curr_suffix == " ثواني":
            self.spinbox.setSuffix(" دقائق")
            
            self.spinbox.setRange(0, 90)
            self.spinbox.setSingleStep(1)
            self.spinbox.setValue(1)

            self.curr_minimum = 0
            self.curr_maximum = 90
            self.curr_suffix = " دقائق"

        if value == 0 and self.previous_value > 0 and self.curr_suffix == " دقائق":
            self.spinbox.setSuffix(" ثواني")
            
            self.spinbox.setRange(10, 60)
            self.spinbox.setSingleStep(10)
            self.spinbox.setValue(50)

            self.curr_minimum = 10
            self.curr_maximum = 60
            self.curr_suffix = " ثواني"
        
        if value == 11 and self.previous_value == 10 and self.curr_suffix == " دقائق":
            self.spinbox.setSuffix(" دقيقة")
            self.curr_suffix = " دقيقة"
        
        if value == 10 and self.previous_value == 11 and self.curr_suffix == " دقيقة":
            self.spinbox.setSuffix(" دقائق")
            self.curr_suffix = " دقائق"

        self.previous_value = value

    def reset_values(self):
        self.previous_value = 10
        self.curr_suffix =  " ثواني"
        self.curr_maximum = 10
        self.curr_minimum = 60
