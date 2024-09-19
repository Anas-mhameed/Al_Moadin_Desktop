
class PlayerManagerHelper:

    def __init__(self, adan_manager, notification_manager, instant_player):
        
        self.adan_manager = adan_manager 
        self.notification_manager = notification_manager
        self.instant_player = instant_player

    # def prepare_for_adan(self):
    #     self.turn_off_instant_player()
    #     self.turn_off_notification()

    def turn_off_instant_player(self):
        self.instant_player.turn_off()

    def turn_off_notification(self):
        self.notification_manager.turn_off()

    def get_adan_time_from_manager(self, adan_index):
        return self.adan_manager.get_current_adan_time(adan_index)
