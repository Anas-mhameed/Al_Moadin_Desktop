
class Mediator:
    def __init__(self):
        self.components = {}

    def set_logger(self, logger):
        """Set the logger for the mediator."""
        self.logger = logger

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
            
            self.components["AdanManager"].handle_summer_winter_change(settings['is_summer_formate'])
            self.components["AdanManager"].handle_quds_diff_change(settings['quds_diff_time'], settings['is_summer_formate'])
            self.components["AdanManager"].handle_new_time_formate(settings['time_formate'][1])

            self.components["TimeManager"].update_time_formate(settings['time_formate'][0])

            self.components["PlayerManager"].set_pre_adan_sound_state(settings['is_pre_adan_sound_activated'])

        elif event == "request_time_formate":
            self.components["GeneralSettings"].set_time_formate()
        
        elif event == "prepare_for_adan":
            self.components["PlayerManager"].prepare_for_adan()
        
        elif event == "allow_playback":
            self.components["PlayerManager"].allow_playback()
        
        elif event == "start_adan":
            self.components["MsgManager"].activate_emergency_frame_timer(args[0])
        
        elif event == "sound_updated_successfully":
            # args[0] is the success message
            self.components["MsgManager"].show_auto_close_info("تم التحديث", args[0])

        elif event == "new_day_event":
            self.components["AdanManager"].handle_new_day(args[0])
            self.components["AdanManager"].handle_new_jomoaa()
            self.components["NotificationManager"].handel_new_day()
        
        elif event == "current_adan_changed_to_previous":
            self.components["PlayerManager"].current_adan_changed_to_previous()
        
        elif event == "cant_play_audio" or event == "error_saving_notification":
            self.components["MsgManager"].show_auto_close_error(args[0], args[1])
        
        elif event == "request_playback":
            self.components["PlayerManager"].request_playback(args[0])
        
        elif event == "audio_duration_changed":
            # args[0] is the duration
            # args[1] is the adan index (1-5)
            # NotificationManager expects a 0-based index (0-4)
            self.components["NotificationManager"].handle_adan_duration_changed(args[0], args[1] - 1)
        
        elif event == "adan_time_changed":
            self.components["NotificationManager"].update_notis_and_intiate_index(args[0])

        elif event == "adan_volume_changed":
            # args[0] is the adan name, args[1] is the new volume
            self.components["PlayerManager"].handle_adan_volume_change(args[0], args[1])

        elif event == "request_adans_duration":
            self.components["AdanManager"].get_adans_duration()
        
        elif event == "audio_finished":
            self.components["ZigbeeController"].run(False)

        elif event == "open_mic":
            if not self.components["GeneralSettings"].is_pre_adan_sound_activated:
                self.components["ZigbeeController"].run(True)

        elif event == "close_mic":
            self.components["ZigbeeController"].run(False)

        elif event == "pre_adan_preparation":
            if self.components["GeneralSettings"].is_pre_adan_sound_activated:
                self.components["PlayerManager"].start_pre_adan_sound()
            else:        
                self.components["ZigbeeController"].run(True)

        elif event == "pre_adan_sound_state_changed":
            self.components["PlayerManager"].set_pre_adan_sound_state(args[0])

        elif event == "stop_quraan_audio":
            self.components["PlayerManager"].stop_quraan_audio(args[0], args[1])
        
        elif event == "quraan_audio_finished":
            self.components["QuraanPageManager"].set_inactive_style_by_index(args[0], args[1])

        elif event == "successfully_played":
            self.components["QuraanPageManager"].successful_play()
        
        elif event == "failed_to_play":
            self.components["QuraanPageManager"].failed_play()
        
        elif event == "set_adan_sound":
            self.components["AdanManager"].update_sound(args[0], args[1])

        # elif event == "firebase_data_received":
        #     # Let each component handle Firebase data in sequence
        #     firebase_data = args[0]
            
        #     # Process in specific order if needed
        #     if "GeneralSettings" in self.components:
        #         self.components["GeneralSettings"].handle_firebase_update(firebase_data)
            
        #     if "AdanManager" in self.components:
        #         adans_data = firebase_data["adansData"]
        #         self.components["AdanManager"].set_adan_state(adans_data)

    def log(self, *args):
        """Log events using the AdanLogger if available."""
        # Check if logger is set, if not try to get it from components
        if not hasattr(self, 'logger') or not self.logger:
            if "AdanLogger" in self.components:
                self.logger = self.components["AdanLogger"]
            else:
                return  # No logger available
        
        if len(args) == 3:
            # Pattern: log(event_type, current_state, new_state)
            event_type, current_state, new_state = args
            self.logger.log_adan_state_change(current_state, new_state, event_type)
        elif len(args) == 4:
            # Pattern: log(event_type, current_state, new_state, details)
            event_type, current_state, new_state, details = args
            self.logger.log_adan_state_change(current_state, new_state, details)
        else:
            # Fallback: convert all args to string
            details = " ".join(str(arg) for arg in args)
            self.logger.log_adan_state_change("unknown", "unknown", details)
