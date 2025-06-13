class PlayAudioCommand:
    def __init__(self, requester: str, file_path: str, volume: int = 50):
        self.requester = requester
        self.file_path = file_path
        self.volume = volume