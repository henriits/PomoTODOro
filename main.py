import sys
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QApplication,
    QPushButton,
    QListWidget,
    QLineEdit,
)
from PyQt6.QtCore import Qt, QTimer, QTime


class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.task_list = QListWidget()

        self.task_input = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.start_button = QPushButton("Start Pomodoro")
        self.timer_label = QLabel("Pomodoro Timer: 00:00")

        self.pomodoro_timer = QTimer(self)
        self.pomodoro_duration = QTime(0, 1)  # 1 minute for each Pomodoro
        self.break_duration = QTime(0, 0, 10)  # 10 seconds break

        self.setup_ui()

    def setup_ui(self):
        # Add widgets to the layout
        self.layout.addWidget(
            self.timer_label,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight,
        )
        self.layout.addWidget(QLabel("To-Do List"))
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.task_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.start_button)
        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)

        self.setWindowTitle("Pomodoro To-Do List App")
        self.setGeometry(100, 100, 400, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.show()
    sys.exit(app.exec())
