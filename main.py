import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout , QLabel, QHBoxLayout, QApplication, QPushButton
from PyQt6.QtCore import Qt

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        
 # Initialize the main layout
        self.layout = QVBoxLayout()

        # Create a list to store tasks


        # Create input field and buttons

        self.add_button = QPushButton("Add Task")
        self.start_button = QPushButton("Start Pomodoro")
        self.timer_label = QLabel("Pomodoro Timer: 00:00")
        
  

        # Set up the layout
        self.setup_ui()

    def setup_ui(self):
        # Add widgets to the layout
        self.layout.addWidget(self.timer_label, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(QLabel("To-Do List"))


        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.start_button)
        self.layout.addLayout(button_layout)

        # Set the main layout for the window
        self.setLayout(self.layout)


        # Set up the application window
        self.setWindowTitle("Pomodoro To-Do List App")
        self.setGeometry(100, 100, 400, 300)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.show()
    sys.exit(app.exec())