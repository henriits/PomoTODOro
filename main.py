import sys
from PyQt6.QtWidgets import QApplication
from login_window import LoginWindow
from todo_list_app import ToDoListApp

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Show login window first
    login_window = LoginWindow()

    # Create the main app window
    todo_app = ToDoListApp()

    # Connect the login_successful signal to show the main app window
    login_window.login_successful.connect(todo_app.show)

    # Show login window
    login_window.show()

    sys.exit(app.exec())