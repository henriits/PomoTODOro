import sys
from PyQt6.QtCore import Qt, QTimer, QTime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QListWidget, QPushButton, QLineEdit, QLabel, QCheckBox, QListWidgetItem, QMessageBox
)

class TaskWidget(QWidget):
    def __init__(self, text):
        super().__init__()
        self.task_label = QLabel(text)
        self.checkbox = QCheckBox()
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.addWidget(self.task_label)
        layout.addWidget(self.checkbox)
        self.setLayout(layout)

    def isChecked(self):
        return self.checkbox.isChecked()

class TasksList(QListWidget):
    def add_task(self, task_text):
        if task_text:
            task_widget = TaskWidget(task_text)
            item = QListWidgetItem()
            item.setSizeHint(task_widget.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, task_widget)

    def remove_checked_tasks(self):
        for i in reversed(range(self.count())):
            item = self.item(i)
            task_widget = self.itemWidget(item)
            if isinstance(task_widget, TaskWidget) and task_widget.isChecked():
                self.takeItem(i)

class PomodoroTimer(QTimer):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.timeout.connect(self.update_timer)
        self.break_timer = QTimer(self)
        self.break_timer.timeout.connect(self.update_break_timer)
        self.is_pomodoro = True  # Flag to track the current timer type
        self.break_count = 0
        

    def start_timer(self):
        if self.is_pomodoro:
            self.start_pomodoro()
        elif self.break_count % 5 == 0 and self.break_count != 0:
            reply = QMessageBox.question(
                self.parent(), "Start Long Break", 
                "Are you sure you want to start the Long Break?", 
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.start_long_break()
            else:
                self.start_short_break()
        else:
            self.start_short_break()

    def start_pomodoro(self):
        self.pomodoro_duration = QTime(0, 0, 1)
        self.start(1000)

    def start_short_break(self):
        self.break_duration = QTime(0, 0, 1) 
        self.break_timer.start(1000)

    def start_long_break(self):
        self.break_duration = QTime(0, 0, 1) 
        self.break_timer.start(1000)

    def update_timer(self):
        self.pomodoro_duration = self.pomodoro_duration.addSecs(-1)
        self.parent().update_timer_label(self.pomodoro_duration)

        if self.pomodoro_duration == QTime(0, 0):
            self.stop()
            self.parent().timer_finished()
            self.is_pomodoro = False  # Switch to break timer
            self.start_timer()

    def update_break_timer(self):
        self.break_duration = self.break_duration.addSecs(-1)
        self.parent().update_timer_label(self.break_duration, is_pomodoro=False)

        if self.break_duration == QTime(0, 0):
            self.break_timer.stop()
            self.parent().break_finished()
            self.is_pomodoro = True  # Switch to Pomodoro timer
            self.break_count += 1
            self.start_timer()

class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()

        self.task_list = TasksList()
        self.task_input = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.remove_button = QPushButton("Remove Checked Tasks")
        self.start_button = QPushButton("Start Pomodoro")
        self.timer_label = QLabel("")
        self.pomodoro_manager = PomodoroTimer(self)
        self.break_count = 0
        self.break_tomato = QLabel("")
        self.EMOJI = "🍅"

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.timer_label, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("To-Do List"))
        layout.addWidget(self.task_list)
        layout.addWidget(self.task_input)
        layout.addWidget(self.break_tomato, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.remove_button)
        button_layout.addWidget(self.start_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_checked_tasks)
        self.start_button.clicked.connect(self.confirm_start_pomodoro)

        self.setWindowTitle("PomoTODOro")
        self.setGeometry(100, 100, 400, 300)

    def add_task(self):
        task_text = self.task_input.text()
        self.task_list.add_task(task_text)
        self.task_input.clear()

    def checkbox_state_changed(self, state, item):
        if state == 2:
            row = self.task_list.row(item)
            self.task_list.takeItem(row)
            del item

    def confirm_start_pomodoro(self):
        reply = QMessageBox.question(
            self, "Start Focus", 
            "Are you sure you want to start the Focus timer?", 
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.start_pomodoro()

    def start_pomodoro(self):
        self.pomodoro_manager.start_timer()

    def update_timer_label(self, duration, is_pomodoro=True):
        timer_type = "Focus" if is_pomodoro else "Break"
        self.timer_label.setText(f"{timer_type} Timer: {duration.toString('mm:ss')}")

    def timer_finished(self):
        QMessageBox.information(
            self, "Finished", 
            "Focus session finished. Take a break!", 
            QMessageBox.StandardButton.Ok
        )
        self.update_timer_label(QTime(0, 0), is_pomodoro=False)

    def remove_checked_tasks(self):
        self.task_list.remove_checked_tasks()

    def break_finished(self):
        reply = QMessageBox.information(
            self, "Break Finished", 
            "Time to continue!", 
            QMessageBox.StandardButton.Ok
        )
        if reply == QMessageBox.StandardButton.Ok:
            self.break_count += 1
            if self.break_count % 5 == 0:
                self.EMOJI = "🥱"  # Change emoji only for the 5th break
            self.break_tomato.setText(self.EMOJI * self.break_count)
            self.update_timer_label(QTime(0, 0))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec())