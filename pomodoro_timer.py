from PyQt6.QtCore import QTimer, QTime
from PyQt6.QtWidgets import QMessageBox


class PomodoroTimer(QTimer):
    START_MINUTES = 0
    START_SECONDS = 3
    SHORT_MINUTES = 0
    SHORT_SECONDS = 2
    LONG_MINUTES = 0
    LONG_SECONDS = 4
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.timeout.connect(self.update_timer)
        self.break_timer = QTimer(self)
        self.break_timer.timeout.connect(self.update_break_timer)
        self.long_break_timer = QTimer(self)
        self.long_break_timer.timeout.connect(self.update_long_break_timer)
        self.is_pomodoro = True
        self.break_count = 0

    def start_timer(self):
        if self.is_pomodoro:
            self.start_pomodoro()
        elif self.break_count % 3 == 0 and self.break_count != 0:
            reply = QMessageBox.question(
                self.parent(),
                "Start Long Break",
                "Are you sure you want to start the Long Break?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.start_long_break()
            else:
                self.start_short_break()
            self.break_count = 0  # Reset break count after asking for a long break
        else:
            self.start_short_break()

    def start_pomodoro(self):
        self.pomodoro_duration = QTime(0, self.START_MINUTES, self.START_SECONDS)
        self.start(1000)

    def start_short_break(self):
        self.break_duration = QTime(0, self.SHORT_MINUTES, self.SHORT_SECONDS)
        self.break_timer.start(1000)

    def start_long_break(self):
        self.break_duration = QTime(0, self.LONG_MINUTES, self.LONG_SECONDS)
        self.long_break_timer.start(1000)

    def update_timer(self):
        self.pomodoro_duration = self.pomodoro_duration.addSecs(-1)
        self.parent().update_timer_label(self.pomodoro_duration)

        if self.pomodoro_duration == QTime(0, 0):
            self.stop()
            self.parent().timer_finished()
            self.is_pomodoro = False
            self.start_timer()

    def update_break_timer(self):
        self.break_duration = self.break_duration.addSecs(-1)
        self.parent().update_timer_label(self.break_duration, is_pomodoro=False)

        if self.break_duration == QTime(0, 0):
            self.break_timer.stop()
            self.parent().break_finished()
            self.is_pomodoro = True
            self.break_count += 1
            self.start_timer()

    def update_long_break_timer(self):
        self.break_duration = self.break_duration.addSecs(-1)
        self.parent().update_timer_label(self.break_duration, is_pomodoro=False)

        if self.break_duration == QTime(0, 0):
            self.long_break_timer.stop()
            self.parent().long_break_finished()
            self.is_pomodoro = True
            self.start_timer()
