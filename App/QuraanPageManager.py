from PySide6.QtWidgets import QWidget, QListWidget, QListWidgetItem 
from helper_functions import get_audio_files
import os
from PlayAudioCommand import PlayAudioCommand
from AudioItemWidget import AudioItemWidget
from PySide6.QtCore import QSize, QUrl

CATEGORIES = {
    "QURAAN": "quraan",
    "ADAN": "adan",
    "FAJER": "fajer"
}

class QuraanPageManager(QWidget):
    def __init__(self, quraan_list_widget: QListWidget, adan_sounds_list_widget: QListWidget, fajer_sounds_list_widget: QListWidget):
        super().__init__()

        self.quraan_audio_dir = './sounds'
        self.quraan_list_widget = quraan_list_widget
        self.quraan_list_widget.setSpacing(5)
        self.current_widget = None  # To track what's playing

        self.adan_audio_dir = './adan-sounds'
        self.adan_sounds_list_widget = adan_sounds_list_widget
        self.adan_sounds_list_widget.setSpacing(5)
        # how to track current widget

        self.fajer_audio_dir = './fajer-sounds'
        self.fajer_sounds_list_widget = fajer_sounds_list_widget
        self.fajer_sounds_list_widget.setSpacing(5)
        # how to track current widget

        self.populate_list(self.quraan_audio_dir, self.quraan_list_widget, CATEGORIES["QURAAN"])
        self.populate_list(self.adan_audio_dir, self.adan_sounds_list_widget, CATEGORIES["ADAN"])
        self.populate_list(self.fajer_audio_dir, self.fajer_sounds_list_widget, CATEGORIES["FAJER"])

    def populate_list(self, audio_dir, list_widget: QListWidget, category: str):
        audio_files = get_audio_files(audio_dir)
        list_widget.clear()

        for filename in audio_files:

            item = QListWidgetItem()
            item.setSizeHint(QSize(350, 80))

            widget = AudioItemWidget(
                filename,
                audio_dir = audio_dir,
                category = category,
                play_callback=self.play_audio,
                stop_callback=self.stop_audio
            )

            # Ask the widget for its preferred size
            item.setSizeHint(widget.sizeHint())

            list_widget.addItem(item)
            list_widget.setItemWidget(item, widget)
 
    def play_audio(self, widget: AudioItemWidget):
        full_path = os.path.join(widget.audio_dir, widget.filename)

        command = PlayAudioCommand("QuraanPageManager", full_path, index=self.get_item_index_by_widget(widget, widget.category), adan_name=widget.category)

        if self.current_widget and self.current_widget != widget:
            self.current_widget.set_inactive_style()

        self.current_widget = widget

        self.mediator.notify(self, "request_playback", command)       

    def get_item_index_by_widget(self, widget: QWidget, category: str) -> int:
        
        if category == CATEGORIES["QURAAN"]:
            list_widget = self.quraan_list_widget
        elif category == CATEGORIES["ADAN"]:
            list_widget = self.adan_sounds_list_widget
        elif category == CATEGORIES["FAJER"]:
            list_widget = self.fajer_sounds_list_widget
        else:
            return -1

        for i in range(list_widget.count()):
            item = list_widget.item(i)
            if list_widget.itemWidget(item) == widget:
                return i
        return -1  # Not found

    def set_inactive_style_by_index(self, index: int, category: str):
    
        if category == CATEGORIES["QURAAN"]:
            list_widget = self.quraan_list_widget
        elif category == CATEGORIES["ADAN"]:
            list_widget = self.adan_sounds_list_widget
        elif category == CATEGORIES["FAJER"]:
            list_widget = self.fajer_sounds_list_widget
        else:
            return

        item = list_widget.item(index)
        widget = list_widget.itemWidget(item)
        if widget:
            widget.set_inactive_style()

    def successful_play(self):
        self.current_widget.set_active_style()

    def failed_play(self):
        self.current_widget = None

    def stop_audio(self, widget):
        index = self.get_item_index_by_widget(widget, widget.category)
        self.mediator.notify(self, "stop_quraan_audio", index, widget.category)

        if self.current_widget == widget:
            self.current_widget = None

    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

        