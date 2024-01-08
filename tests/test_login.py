import os
import csv
from PyQt6.QtWidgets import QApplication
from login_window import LoginWindow

# Mocking a simple CSV file for testing
CSV_CONTENT = """Email,Password
test@example.com,test_password
"""


def create_mock_csv_file():
    folder_path = "user_csv_files"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    csv_file_path = os.path.join(folder_path, "users.csv")
    with open(csv_file_path, "w") as csvfile:
        csvfile.write(CSV_CONTENT)


def test_check_credentials_correct():
    app = QApplication([])
    create_mock_csv_file()
    login_window = LoginWindow()
    assert login_window.check_credentials("test@example.com", "test_password") is True
    os.remove(os.path.join("user_csv_files", "users.csv"))


def test_check_credentials_incorrect_password():
    app = QApplication([])
    create_mock_csv_file()
    login_window = LoginWindow()
    assert not login_window.check_credentials("test@example.com", "wrong_password")
    os.remove(os.path.join("user_csv_files", "users.csv"))


def test_check_credentials_incorrect_email():
    app = QApplication([])
    create_mock_csv_file()
    login_window = LoginWindow()
    assert not login_window.check_credentials("wrong@example.com", "test_password")
    os.remove(os.path.join("user_csv_files", "users.csv"))
