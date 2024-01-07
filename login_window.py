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
import os


class LoginWindow(QDialog):
    login_successful = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.login_button = QPushButton("Login")
        self.register_button = QPushButton("Register")

        self.setup_ui()
        self.setup_logic()
        self.apply_styles()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout_margin = LoginWindowStyles.get_layout_margin()
        app_stylesheet = LoginWindowStyles.get_app_stylesheet()
        self.setStyleSheet(app_stylesheet)
        username_label = QLabel("Username:")
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        password_label = QLabel("Password:")
        layout.addWidget(password_label)

        # hide password
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.password_input)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.login_button)
        buttons_layout.addWidget(self.register_button)
        layout.addLayout(buttons_layout)
        layout.setContentsMargins(
            layout_margin, layout_margin, layout_margin, layout_margin
        )
        self.setLayout(layout)
        self.setWindowIcon(QtGui.QIcon("tomato.png"))
        self.setWindowTitle("Login")
        self.setGeometry(1200, 200, 300, 150)

    def setup_logic(self):
        self.login_button.clicked.connect(self.try_login)
        self.register_button.clicked.connect(self.open_register_window)

    def try_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username and password:
            if self.check_credentials(username, password):
                self.login_successful.emit(username)
                self.accept()
            else:
                QMessageBox.warning(self, "Login Failed", "Wrong username or password.")

    def check_credentials(self, username, password):
        try:
            folder_path = "user_csv_files"
            csv_file_path = os.path.join(folder_path, "users.csv")

            with open(csv_file_path, "r") as csvfile_read:
                reader = csv.DictReader(csvfile_read)
                for row in reader:
                    if row["Username"] == username and row["Password"] == password:
                        return True
            return False

        except Exception as e:
            print(f"Error checking credentials: {e}")
            return False

    def open_register_window(self):
        register_window = RegisterWindow()
        if register_window.exec() == QDialog.accepted:
            pass

    def get_username(self):
        return self.username_input.text()

    def apply_styles(self):
        input_style = LoginWindowStyles.get_input_style()
        button_style = LoginWindowStyles.get_button_style()

        self.username_input.setStyleSheet(input_style)
        self.password_input.setStyleSheet(input_style)
        self.login_button.setStyleSheet(button_style)
        self.register_button.setStyleSheet(button_style)
