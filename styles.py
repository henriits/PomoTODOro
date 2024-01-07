class ToDoListStyles:
    @staticmethod
    def get_break_tomato_style():
        return "font-size: 18pt; color: #1565C0;"

    @staticmethod
    def get_timer_label_style():
        return """
                font-size: 76px;
                font-weight: bold;
                color: #fff;
                text-align: center;"""

    @staticmethod
    def get_task_input_style():
        return "font-size: 14pt; background-color: #E3F2FD; color: #1565C0;"

    @staticmethod
    def get_task_list_style():
        return "background-color: #fff; color: #333;"

    @staticmethod
    def get_app_stylesheet():
        return """
            QWidget {
                background-color: #81D4FA;
                color: #fff;
                font-size: 18px;
            }
            QMessageBox QLabel {
                font-size: 24px;
            }
            QPushButton {
                background-color: #1565C0;
                color: #fff;
                border: none;
                padding: 8px 16px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """


class InfoStyles:
    @staticmethod
    def get_info_dialog_stylesheet():
        return """
            QDialog {
                background-color: #81D4FA;
                color: #fff;
                font-size: 18px;
            }
        """

    @staticmethod
    def get_info_label_stylesheet():
        return "font-size: 26px; color: #fff;"


class LoginWindowStyles:
    @staticmethod
    def get_layout_margin():
        return 10

    @staticmethod
    def get_app_stylesheet():
        return """
            QDialog {
                background-color: #81D4FA;
            }
        """

    @staticmethod
    def get_input_style():
        return """
            QLineEdit {
                font-size: 14pt;
                background-color: #E3F2FD;
                color: #1565C0;
            }
        """

    @staticmethod
    def get_button_style():
        return """
            QPushButton {
                background-color: #1565C0;
                color: #fff;
                border: none;
                padding: 8px 16px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """


class RegisterWindowStyles:
    @staticmethod
    def get_layout_margin():
        return 10

    @staticmethod
    def get_app_stylesheet():
        return """
            QDialog {
                background-color: #81D4FA;
            }

            """

    @staticmethod
    def get_input_style():
        return """
            QLineEdit {
                font-size: 14pt;
                background-color: #E3F2FD;
                color: #1565C0;
                }
        """

    @staticmethod
    def get_button_style():
        return """
            QPushButton {
                background-color: #1565C0;
                color: #fff;
                border: none;
                padding: 8px 16px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }"""
