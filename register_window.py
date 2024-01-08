import csv
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
)
from styles import RegisterWindowStyles
from PyQt6 import QtGui
from todo_list_app import ToDoListApp
import os
import re


class RegisterWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.email_input = QLineEdit()
        self.password_input = QLineEdit()
        self.confirm_password_input = QLineEdit()
        self.register_button = QPushButton("Register")

        self.setup_ui()
        self.setup_logic()
        self.apply_styles()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout_margin = RegisterWindowStyles.get_layout_margin()
        app_stylesheet = RegisterWindowStyles.get_app_stylesheet()
        self.setStyleSheet(app_stylesheet)
        email_label = QLabel("Email:")
        layout.addWidget(email_label)
        layout.addWidget(self.email_input)

        password_label = QLabel("Password:")
        layout.addWidget(password_label)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        confirm_password_label = QLabel("Confirm Password:")
        layout.addWidget(confirm_password_label)
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.confirm_password_input)

        layout.addWidget(self.register_button)
        layout.setContentsMargins(
            layout_margin, layout_margin, layout_margin, layout_margin
        )
        self.setLayout(layout)
        self.setWindowIcon(QtGui.QIcon(ToDoListApp.resource_path("icon.ico")))
        self.setWindowTitle("Register")
        self.setGeometry(1200, 200, 300, 150)

    def setup_logic(self):
        self.register_button.clicked.connect(self.try_register)

    def try_register(self):
        email = self.email_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        # Validate email using regex
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            QMessageBox.warning(self, "Registration Failed", "Invalid email format.")
            return

        if email and password == confirm_password:
            if not register_user(email, password):
                QMessageBox.warning(self, "Registration Failed", "User already exists.")
            else:
                QMessageBox.information(
                    self, "Registration Successful", "Registration successful."
                )
                self.accept()
        else:
            QMessageBox.warning(self, "Registration Failed", "Password do not match.")

    def apply_styles(self):
        input_style = RegisterWindowStyles.get_input_style()
        button_style = RegisterWindowStyles.get_button_style()

        self.email_input.setStyleSheet(input_style)
        self.password_input.setStyleSheet(input_style)
        self.confirm_password_input.setStyleSheet(input_style)
        self.register_button.setStyleSheet(button_style)


def register_user(email, password):
    folder_path = "user_csv_files"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    try:
        csv_file_path = os.path.join(folder_path, "users.csv")

        with open(csv_file_path, "a", newline="") as csvfile:
            fieldnames = ["Email", "Password"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Check if the file is empty, if so, write the header
            if csvfile.tell() == 0:
                writer.writeheader()

            # Check if the user already exists
            with open(csv_file_path, "r") as csvfile_read:
                reader = csv.DictReader(csvfile_read)
                for row in reader:
                    if row["Email"] == email:
                        return False  # User already exists

            # Write the new user
            writer.writerow({"Email": email, "Password": password})

        return True

    except Exception as e:
        print(f"Error registering user: {e}")
        return False
