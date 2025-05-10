from AudioPriority import AudioPriority

class PlayAudioCommand:
    def __init__(self, requester: str, file_path: str, priority: AudioPriority):
        self.requester = requester
        self.file_path = file_path
        self.priority = priority

