from enum import Enum
from PySide6.QtWidgets import QFileDialog, QInputDialog, QMessageBox
import os

def ask_user_for_token():
    token, ok = QInputDialog.getText(None, "Enter Home Assistant Token", "Please enter your Home Assistant long-lived access token:")
    if ok and token:
        return token.strip()
    return None

# def ask_user_for_credentials():
#     pass

def reset_token(database_manager):
    database_manager.clear_token()
    QMessageBox.information(None, "Token Reset", "Please restart the app to enter a new token.")

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