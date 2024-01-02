from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import pyqtSignal

class LoginWindow(QDialog):
    login_successful = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.username_input = QLineEdit()
        self.login_button = QPushButton("Login")

        self.setup_ui()
        self.setup_logic()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)
        self.setWindowTitle("Login")
        self.setGeometry(200, 200, 300, 150)

    def setup_logic(self):
        self.login_button.clicked.connect(self.try_login)

    def try_login(self):
        username = self.username_input.text()
        if username:
            self.login_successful.emit()  # Emit the signal when login is successful
            self.accept()