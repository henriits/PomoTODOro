from PyQt6.QtWidgets import QApplication
from pomodoro_timer import PomodoroTimer
from PyQt6.QtCore import QTime

def test_start_pomodoro_timer():
    app = QApplication([])
    pomodoro_timer = PomodoroTimer()
    pomodoro_timer.start_pomodoro()
    assert pomodoro_timer.isActive()
    assert pomodoro_timer.pomodoro_duration == QTime(0, 0, 5)

def test_start_short_break_timer():
    app = QApplication([])
    pomodoro_timer = PomodoroTimer()


    pomodoro_timer.start_short_break()
    assert pomodoro_timer.break_timer.isActive()
    assert pomodoro_timer.break_duration == QTime(0, 0, 10)

def test_start_long_break_timer():
    app = QApplication([])
    pomodoro_timer = PomodoroTimer()

    pomodoro_timer.start_long_break()
    assert pomodoro_timer.long_break_timer.isActive()
    assert pomodoro_timer.break_duration == QTime(0, 0, 15)
