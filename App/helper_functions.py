from enum import Enum
from PySide6.QtWidgets import QFileDialog 
import os

def get_audio_files(directory, extensions=None):
    if extensions is None:
        extensions = ['.mp3', '.wav', '.ogg', '.flac', '.m4a']
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)) and os.path.splitext(file)[1].lower() in extensions:
            files.append(file)
    return files

def select_sound_file(widget):
        file_dialog = QFileDialog(widget)
        file_dialog.setNameFilter("Sound Files (*.wav *.mp3 *.ogg)")
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                return file_paths[0]

class AdanIndex(Enum):
    FAJER = 1
    DOHOR = 2
    ASER = 3
    MAGRIB = 4
    ISHAA = 5