import sys
import csv
from PyQt6.QtCore import Qt, QTimer, QTime
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QMessageBox,
)
from PyQt6 import QtGui

from tasks_list import TasksList
from pomodoro_timer import PomodoroTimer
from task_widget import TaskWidget
from styles import ToDoListStyles
import os


class ToDoListApp(QWidget):
    def __init__(self, username):  # Add 'username' parameter
        super().__init__()

        self.username = username 

        self.task_list = TasksList()
        self.task_input = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.remove_button = QPushButton("Remove Checked Tasks")
        self.start_button = QPushButton("Start Pomodoro")
        self.timer_label = QLabel("")
        self.pomodoro_manager = PomodoroTimer(self)
        self.break_count = 0
        self.break_tomato = QLabel("")
        self.long_break_emoji = "🥱"
        self.small_break_emoji = "🍅"
        self.emojis = []
        self.break_tomato = QLabel(self)
        self.break_tomato.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )

        self.setup_ui()
        self.setup_logic()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(
            self.timer_label,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight,
        )
        layout.addWidget(QLabel("Tasks:"))
        layout.addWidget(self.task_list)
        layout.addWidget(self.task_input)
        layout.addWidget(
            self.break_tomato,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft,
        )

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.remove_button)
        button_layout.addWidget(self.start_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.setWindowIcon(QtGui.QIcon("tomato.png"))
        self.setWindowTitle("PomoTODOro")
        self.setGeometry(100, 100, 500, 600)

        # Load tasks from CSV file on startup
        self.load_tasks_from_csv()

        self.apply_styles()

    def apply_styles(self):
        self.break_tomato.setStyleSheet(ToDoListStyles.get_break_tomato_style())
        self.timer_label.setStyleSheet(ToDoListStyles.get_timer_label_style())
        self.task_input.setStyleSheet(ToDoListStyles.get_task_input_style())
        self.task_list.setStyleSheet(ToDoListStyles.get_task_list_style())
        self.setStyleSheet(ToDoListStyles.get_app_stylesheet())

    def setup_logic(self):
        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_checked_tasks)
        self.start_button.clicked.connect(self.confirm_start_pomodoro)

    def add_task(self):
        task_text = self.task_input.text()
        self.task_list.add_task(task_text)
        self.task_input.clear()

        # Save tasks to CSV file
        self.save_tasks_to_csv()

    def remove_checked_tasks(self):
        self.task_list.remove_checked_tasks()

        # Save tasks to CSV file
        self.save_tasks_to_csv()

    def load_tasks_from_csv(self):
        try:
            folder_path = "user_csv_files"
            csv_file_path = os.path.join(folder_path, f"{self.username}_tasks.csv")

            with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    task_text = row[0]
                    self.task_list.add_task(task_text)
        except FileNotFoundError:
            pass  # Ignore if the file doesn't exist

    def save_tasks_to_csv(self):
        folder_path = "user_data"  # Change this to the desired folder name
        csv_file_path = os.path.join(folder_path, f"{self.username}_tasks.csv")

        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for i in range(self.task_list.count()):
                item = self.task_list.item(i)
                task_widget = self.task_list.itemWidget(item)
                if isinstance(task_widget, TaskWidget):
                    task_text = task_widget.task_label.text()
                    writer.writerow([task_text])

    def checkbox_state_changed(self, state, item):
        if state == 2:
            row = self.task_list.row(item)
            self.task_list.takeItem(row)
            del item
            # Save tasks to CSV file
            self.save_tasks_to_csv()

    def confirm_start_pomodoro(self):
        reply = QMessageBox.question(
            self,
            "Start Focus",
            "Are you sure you want to start the Focus timer?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
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
            self,
            "Finished",
            "Focus session finished. Take a break!",
            QMessageBox.StandardButton.Ok,
        )
        self.update_timer_label(QTime(0, 0), is_pomodoro=False)

    def break_finished(self):
        reply = QMessageBox.information(
            self, "Break Finished", "Time to continue!", QMessageBox.StandardButton.Ok
        )
        if reply == QMessageBox.StandardButton.Ok:
            self.break_count += 1
            self.emojis.append(self.small_break_emoji)
            self.break_tomato.setText(" ".join(self.emojis))
            self.update_timer_label(QTime(0, 0))

    def long_break_finished(self):
        reply = QMessageBox.information(
            self,
            "Long Break Finished",
            "Time to continue!",
            QMessageBox.StandardButton.Ok,
        )
        if reply == QMessageBox.StandardButton.Ok:
            self.emojis.append(self.long_break_emoji)
            self.break_tomato.setText(" ".join(self.emojis))
            self.update_timer_label(QTime(0, 0))

    def handle_login_successful(self, username):
        self.username = username
        # Load tasks from CSV file on login
        self.load_tasks_from_csv()
        # Show the main app window
        self.show()