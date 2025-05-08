class Mediator:
    def __init__(self):
        self.components = {}

    def register(self, name, component):
        """Register a component with the mediator."""
        self.components[name] = component
        component.set_mediator(self)

    def notify(self, sender, event, *args, **kwargs):
        """Handle communication between components."""
        if event == "quds_diff_time_changed":
            self.components["AdanManager"].handle_quds_diff_change(args[0], args[1])
        
        
        elif event == "summer_timing_changed":
            self.components["AdanManager"].handle_summer_winter_change(args[0])
        
        
        elif event == "time_formate_changed":

            self.components["TimeManager"].update_time_formate(args[0])
            self.components["AdanManager"].handle_new_time_formate(args[1])
        
        
        elif event == "request_general_settings":

            settings = self.components["GeneralSettings"].collect_settings()


            self.components["AdanManager"].handle_quds_diff_change(settings['quds_diff_time'], settings['is_summer_formate'])
            self.components["AdanManager"].handle_summer_winter_change(settings['is_summer_formate'])
            self.components["AdanManager"].handle_new_time_formate(settings['time_formate'][1])

            self.components["TimeManager"].update_time_formate(settings['time_formate'][0])

        
        elif event == "request_time_formate":
            self.components["GeneralSettings"].set_time_formate()
        
        elif event == "emergency_frame_timer_expired":
            self.components["AdanManager"].emerg_frame_hide()

        elif event == "start_adan":
            self.components["MsgManager"].activate_emergency_frame_timer(args[0])
        
        elif event == "new_day_event":
            self.components["AdanManager"].handle_new_day(args[0])
            self.components["AdanManager"].handle_new_jomoaa()
            