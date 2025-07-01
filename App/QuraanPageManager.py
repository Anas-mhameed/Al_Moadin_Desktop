from PySide6.QtWidgets import QWidget, QListWidget, QListWidgetItem 
from helper_functions import get_audio_files
import os
from PlayAudioCommand import PlayAudioCommand
from AudioItemWidget import AudioItemWidget
from PySide6.QtCore import QSize, QUrl

class QuraanPageManager(QWidget):
    def __init__(self, list_widget: QListWidget):
        super().__init__()

        self.audio_dir = './sounds'
        self.list_widget = list_widget
        self.list_widget.setSpacing(5)
        self.current_widget = None  # To track what's playing

        self.populate_list()


    def populate_list(self):
        audio_files = get_audio_files(self.audio_dir)
        self.list_widget.clear()

        for filename in audio_files:

            item = QListWidgetItem()
            item.setSizeHint(QSize(350, 80))

            widget = AudioItemWidget(
                filename,
                play_callback=self.play_audio,
                stop_callback=self.stop_audio
            )

            # Ask the widget for its preferred size
            item.setSizeHint(widget.sizeHint())

            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, widget)
 
    def play_audio(self, filename, widget):
        full_path = os.path.join(self.audio_dir, filename)

        command = PlayAudioCommand("QuraanPageManager", full_path, index=self.get_item_index_by_widget(widget))

        self.mediator.notify(self, "request_playback", command)       

        if self.current_widget and self.current_widget != widget:
            self.current_widget.set_inactive_style()

        self.current_widget = widget
        widget.set_active_style()

    def get_item_index_by_widget(self, widget: QWidget) -> int:
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if self.list_widget.itemWidget(item) == widget:
                return i
        return -1  # Not found

    def set_inactive_style_by_index(self, index: int):
        item = self.list_widget.item(index)
        widget = self.list_widget.itemWidget(item)
        if widget:
            widget.set_inactive_style()

    def stop_audio(self, widget):
        index = self.get_item_index_by_widget(widget)
        self.mediator.notify(self, "stop_quraan_audio", index)

        if self.current_widget == widget:
            self.current_widget = None

    def set_mediator(self, mediator):
        """Set the mediator for communication."""
        self.mediator = mediator

        