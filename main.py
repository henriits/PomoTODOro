import sys
from PyQt6.QtWidgets import QApplication
from todo_list_app import ToDoListApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec())
