import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout , QLabel, QHBoxLayout, QApplication
from PyQt6.QtCore import Qt

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QVBoxLayout()
        
        
    def setup_ui(self):

        self.setWindowTitle("Pomodoro To-Do List App")
        self.setGeometry(100, 100, 400, 300)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.show()
    sys.exit(app.exec())