from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout
from styles import InfoStyles
from PyQt6 import QtGui
import os
import sys

class InfoDialog(QDialog):
    @staticmethod
    # This method is required for extraction .exe icon to show
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def __init__(self, focus_minutes, focus_seconds, short_minutes, short_seconds, long_minutes, long_seconds):
        super().__init__()

        self.setWindowIcon(QtGui.QIcon(self.resource_path("icon.ico")))
        self.setWindowTitle("Pomodoro Information")
        self.setGeometry(600, 200, 400, 200)

        info_label = QLabel(
            f"The Pomodoro Technique is a time management method that uses a timer\n"
            f"to break down work into intervals, traditionally 25 minutes in length, separated by short breaks."
            f"\n\n"
            f"Here's the typical Pomodoro cycle:\n"
            f"- Focus Time: 25 minutes\n"
            f"- Short Break: 5 minutes\n"
            f"- After completing 4 cycles, take a Long Break: 15-30 minutes and seconds\n\n"
            
            "Your setup:\n"
            f"- Focus Time: {focus_minutes} minutes and {focus_seconds} seconds\n"
            f"- Short Break: {short_minutes} minutes and {short_seconds} seconds\n"
            f"- Long Break: {long_minutes} minutes and {long_seconds} seconds\n"
            f"\n\n"
            "Emojis:\n"
            "🥱 - Long Break\n"
            "🍅 - Short Break"
            f"\n\n"
            "Tasks:\n"
            "All the tasks added, will be saved to the csv file.\n"
            "CSV file will be located in the same directory as pomotodoro.exe "
            f"\n\n"
            "Happy Focusing!"
        )

        layout = QVBoxLayout()
        layout.addWidget(info_label)
        self.setLayout(layout)

        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet(InfoStyles.get_info_dialog_stylesheet())
        info_label = self.findChild(QLabel)
        if info_label:
            info_label.setStyleSheet(InfoStyles.get_info_label_stylesheet())

    def show_info(self):
        self.exec()
