import sys
from PyQt6.QtWidgets import QApplication
from login_window import LoginWindow
from todo_list_app import ToDoListApp

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    login_window = LoginWindow()

    # Create an instance of ToDoListApp with the username from the login window
    todo_list_app = ToDoListApp(username=login_window.get_username())

    # Connect the login_successful signal to handle_login_successful slot in ToDoListApp
    login_window.login_successful.connect(todo_list_app.handle_login_successful)

    login_window.show()
    sys.exit(app.exec())
