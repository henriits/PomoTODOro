import csv
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
)
from PyQt6 import QtGui
from PyQt6.QtCore import pyqtSignal
from styles import LoginWindowStyles
from register_window import RegisterWindow
from todo_list_app import ToDoListApp
import os
import re


class LoginWindow(QDialog):
    login_successful = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.email_input = QLineEdit()
        self.password_input = QLineEdit()
        self.login_button = QPushButton("Login")
        self.register_button = QPushButton("Register")
        self.show_password_button = QPushButton("Show Password")
        self.show_password_button.setCheckable(True)

        self.setup_ui()
        self.setup_logic()
        self.apply_styles()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout_margin = LoginWindowStyles.get_layout_margin()
        app_stylesheet = LoginWindowStyles.get_app_stylesheet()
        self.setStyleSheet(app_stylesheet)
        email_label = QLabel("Email:")
        layout.addWidget(email_label)
        layout.addWidget(self.email_input)
        password_label = QLabel("Password:")
        layout.addWidget(password_label)

        # hide password
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.password_input)
        layout.addWidget(self.show_password_button)
        
        self.show_password_button.clicked.connect(self.toggle_password_visibility)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.login_button)
        buttons_layout.addWidget(self.register_button)
        layout.addLayout(buttons_layout)
        layout.setContentsMargins(
            layout_margin, layout_margin, layout_margin, layout_margin
        )
        self.setLayout(layout)
        self.setWindowIcon(QtGui.QIcon(ToDoListApp.resource_path("icon.ico")))
        self.setWindowTitle("Login")
        self.setGeometry(1200, 200, 300, 150)
        
    def toggle_password_visibility(self):
        if self.show_password_button.isChecked():
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
 

    def setup_logic(self):
        self.login_button.clicked.connect(self.try_login)
        self.register_button.clicked.connect(self.open_register_window)

    def try_login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        # Validate email using regex
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            QMessageBox.warning(self, "Login Failed", "Invalid email format.")
            return

        if email and password:
            if self.check_credentials(email, password):
                self.login_successful.emit(email)
                self.accept()
            else:
                QMessageBox.warning(self, "Login Failed", "Wrong email or password.")

    def check_credentials(self, email, password):
        try:
            folder_path = "user_csv_files"
            csv_file_path = os.path.join(folder_path, "users.csv")

            with open(csv_file_path, "r") as csvfile_read:
                reader = csv.DictReader(csvfile_read)
                for row in reader:
                    if row["Email"] == email and row["Password"] == password:
                        return True
            return False

        except Exception as e:
            print(f"Error checking credentials: {e}")
            return False

    def open_register_window(self):
        register_window = RegisterWindow()
        if register_window.exec() == QDialog.accepted:
            pass

    def get_email(self):
        return self.email_input.text()

    def apply_styles(self):
        input_style = LoginWindowStyles.get_input_style()
        button_style = LoginWindowStyles.get_button_style()

        self.email_input.setStyleSheet(input_style)
        self.password_input.setStyleSheet(input_style)
        self.login_button.setStyleSheet(button_style)
        self.register_button.setStyleSheet(button_style)
