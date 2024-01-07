from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout
from styles import InfoStyles
class InfoDialog(QDialog):
    def __init__(self, focus_time, short_break_time, long_break_time):
        super().__init__()

        self.setWindowTitle("Pomodoro Information")
        self.setGeometry(200, 200, 400, 200)

        info_label = QLabel(
            f"The Pomodoro Technique is a time management method that uses a timer\n"
            f"to break down work into intervals, traditionally {focus_time} minutes in length, separated by short breaks."
            f"\n\n"
            f"Here's the typical Pomodoro cycle:\n"
            f"- Focus Time: {focus_time} minutes\n"
            f"- Short Break: {short_break_time} minutes\n"
            f"- After completing 4 cycles, take a Long Break: {long_break_time} minutes"
            f"\n\n"
            "Emojis:\n"
            "🥱 - Long Break\n"
            "🍅 - Short Break"
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
