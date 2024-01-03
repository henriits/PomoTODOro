import csv
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
    QApplication,
)
from PyQt6.QtCore import pyqtSignal
from todo_list_app import ToDoListApp  # Import the ToDoListApp class


class RegisterWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.confirm_password_input = QLineEdit()
        self.register_button = QPushButton("Register")

        self.setup_ui()
        self.setup_logic()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(QLabel("Confirm Password:"))
        layout.addWidget(self.confirm_password_input)
        layout.addWidget(self.register_button)

        self.setLayout(layout)
        self.setWindowTitle("Register")
        self.setGeometry(200, 200, 300, 200)

    def setup_logic(self):
        self.register_button.clicked.connect(self.try_register)

    def try_register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if username and password == confirm_password:
            # Perform registration logic here
            if not register_user(username, password):
                QMessageBox.warning(self, "Registration Failed", "User already exists.")
            else:
                QMessageBox.information(
                    self, "Registration Successful", "Registration successful."
                )
                self.accept()
        else:
            QMessageBox.warning(self, "Registration Failed", "Password do not match.")


def register_user(username, password):
    try:
        with open("users.csv", "a", newline="") as csvfile:
            fieldnames = ["Username", "Password"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Check if the file is empty, if so, write the header
            if csvfile.tell() == 0:
                writer.writeheader()

            # Check if the user already exists
            with open("users.csv", "r") as csvfile_read:
                reader = csv.DictReader(csvfile_read)
                for row in reader:
                    if row["Username"] == username:
                        return False  # User already exists

            # Write the new user
            writer.writerow({"Username": username, "Password": password})

        return True  # Registration successful

    except Exception as e:
        print(f"Error registering user: {e}")
        return False  # Registration failed


class LoginWindow(QDialog):
    login_successful = pyqtSignal(str)  # Update the signal to include the username

    def __init__(self):
        super().__init__()

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.login_button = QPushButton("Login")
        self.register_button = QPushButton("Register")

        self.setup_ui()
        self.setup_logic()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.login_button)
        buttons_layout.addWidget(self.register_button)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)
        self.setWindowTitle("Login")
        self.setGeometry(200, 200, 300, 150)

    def setup_logic(self):
        self.login_button.clicked.connect(self.try_login)
        self.register_button.clicked.connect(self.open_register_window)

    def try_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username and password:
            # Check login credentials
            if self.check_credentials(username, password):
                self.login_successful.emit(username)  # Emit the username
                self.accept()
            else:
                QMessageBox.warning(self, "Login Failed", "Wrong username or password.")

    def check_credentials(self, username, password):
        try:
            with open("users.csv", "r") as csvfile_read:
                reader = csv.DictReader(csvfile_read)
                for row in reader:
                    if row["Username"] == username and row["Password"] == password:
                        return True  # Username and password match
            return False  # No matching credentials found

        except Exception as e:
            print(f"Error checking credentials: {e}")
            return False  # Login check failed

    def open_register_window(self):
        register_window = RegisterWindow()
        if register_window.exec() == QDialog.accepted:
            # Handle registration success
            pass

    def get_username(self):
        return self.username_input.text()
    
    
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    login_window = LoginWindow()

    # Create an instance of ToDoListApp
    todo_list_app = ToDoListApp()

    # Connect the login_successful signal to handle_login_successful slot in ToDoListApp
    login_window.login_successful.connect(todo_list_app.handle_login_successful)

    login_window.show()
    sys.exit(app.exec())
