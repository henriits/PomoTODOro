import csv
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from styles import RegisterWindowStyles

class RegisterWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.username_input = QLineEdit()
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
        username_label = QLabel("Username:")
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        password_label = QLabel("Password:")
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        confirm_password_label = QLabel("Confirm Password:")
        layout.addWidget(confirm_password_label)
        layout.addWidget(self.confirm_password_input)
        layout.addWidget(self.register_button)
        layout.setContentsMargins(layout_margin, layout_margin, layout_margin, layout_margin)
        self.setLayout(layout)
        self.setWindowTitle("Register")
        self.setGeometry(1200, 200, 300, 100)

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

    def apply_styles(self):
        input_style = RegisterWindowStyles.get_input_style()
        button_style = RegisterWindowStyles.get_button_style()

        self.username_input.setStyleSheet(input_style)
        self.password_input.setStyleSheet(input_style)
        self.confirm_password_input.setStyleSheet(input_style)
        self.register_button.setStyleSheet(button_style)

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