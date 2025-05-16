from enum import Enum
from PySide6.QtWidgets import QFileDialog 

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