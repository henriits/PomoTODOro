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
        self.pomodoro_duration = QTime(0, 0, 10)
        self.break_duration = QTime(0, 0, 5)
        self.break_timer = QTimer(self)
        self.break_timer.timeout.connect(self.update_break_timer)

    def start_pomodoro(self):
        self.start(1000)

    def update_timer(self):
        self.pomodoro_duration = self.pomodoro_duration.addSecs(-1)
        self.parent().update_timer_label(self.pomodoro_duration)

        if self.pomodoro_duration == QTime(0, 0):
            self.stop()
            self.parent().timer_finished()

    def start_break(self):
        self.break_timer.start(1000)

    def update_break_timer(self):
        self.break_duration = self.break_duration.addSecs(-1)
        self.parent().update_timer_label(self.break_duration)

        if self.break_duration == QTime(0, 0):
            self.break_timer.stop()
            self.parent().break_finished()


class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()

        self.task_list = TasksList()
        self.task_input = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.remove_button = QPushButton("Remove Checked Tasks")
        self.start_button = QPushButton("Start Pomodoro")
        self.timer_label = QLabel("Pomodoro Timer: 00:00")
        self.pomodoro_manager = PomodoroTimer(self)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.timer_label, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("To-Do List"))
        layout.addWidget(self.task_list)
        layout.addWidget(self.task_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.remove_button)
        button_layout.addWidget(self.start_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_checked_tasks)
        self.start_button.clicked.connect(self.confirm_start_pomodoro)

        self.setWindowTitle("Pomodoro To-Do List App")
        self.setGeometry(100, 100, 400, 300)

    def add_task(self):
        """Add a new task to the list."""
        task_text = self.task_input.text()
        self.task_list.add_task(task_text)
        self.task_input.clear()

    def checkbox_state_changed(self, state, item):
        """Handle checkbox state changes."""
        if state == 2:
            row = self.task_list.row(item)
            self.task_list.takeItem(row)
            del item

    def confirm_start_pomodoro(self):
        """Ask for confirmation before starting the Pomodoro timer."""
        reply = QMessageBox.question(
            self, "Start Pomodoro", 
            "Are you sure you want to start the Pomodoro timer?", 
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.start_pomodoro()

    def start_pomodoro(self):
        """Start the Pomodoro timer."""
        self.pomodoro_manager.start_pomodoro()

    def update_timer_label(self, duration):
        """Update the timer label with the given duration."""
        self.timer_label.setText(f"Timer: {duration.toString('mm:ss')}")

    def timer_finished(self):
        """Handle the completion of the Pomodoro timer."""
        QMessageBox.information(
            self, "Pomodoro Finished", 
            "Pomodoro session finished. Take a break!", 
            QMessageBox.StandardButton.Ok
        )
        self.timer_label.setText("Break Timer: 00:00")
        self.pomodoro_manager.start_break()

    def remove_checked_tasks(self):
        """Remove checked tasks from the list."""
        self.task_list.remove_checked_tasks()

    def break_finished(self):
        """Handle the completion of the break timer."""
        self.timer_label.setText("Pomodoro Timer: 00:00")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec())
