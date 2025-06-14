class PlayAudioCommand:
    def __init__(self, requester: str, file_path: str, volume: int = 50, adan_name: str = None):
        self.requester = requester
        self.file_path = file_path
        self.volume = volume
        self.adan_name = adan_name  # Add adan_name to identify which adan is playing
