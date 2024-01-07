class ToDoListStyles:
    @staticmethod
    def get_break_tomato_style():
        return "font-size: 18pt; color: #1565C0;"  # Dark Blue

    @staticmethod
    def get_timer_label_style():
        return """                
                font-size: 62px;  /* Set your desired font size */
                font-weight: bold;
                color: #fff;  /* Set your desired text color */
                text-align: center;  /* Center the text */"""

    @staticmethod
    def get_task_input_style():
        return "font-size: 14pt; background-color: #E3F2FD; color: #1565C0;"  # Light Blue

    @staticmethod
    def get_task_list_style():
        return "background-color: #fff; color: #333;"

    @staticmethod
    def get_app_stylesheet():
        return """
            QWidget {
                background-color: #81D4FA; /* Sky Blue */
                color: #fff;
                font-size: 18px;
            }
            QPushButton {
                background-color: #1565C0; /* Dark Blue */
                color: #fff;
                border: none;
                padding: 8px 16px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #1976D2; /* Slightly darker Blue */
            }
        """


class LoginWindowStyles:
    @staticmethod
    def get_layout_margin():
        return 10

    @staticmethod
    def get_app_stylesheet():
        return """
            QDialog {
                background-color: #81D4FA; /* Sky Blue */
            }
        """

    @staticmethod
    def get_input_style():
        return """
            QLineEdit {
                font-size: 14pt;
                background-color: #E3F2FD; /* Light Blue */
                color: #1565C0; /* Dark Blue */
            }
        """

    @staticmethod
    def get_button_style():
        return """
            QPushButton {
                background-color: #1565C0; /* Dark Blue */
                color: #fff;
                border: none;
                padding: 8px 16px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #1976D2; /* Slightly darker Blue */
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
                background-color: #81D4FA; /* Sky Blue */
            }

            """



    @staticmethod
    def get_input_style():
        return """
            QLineEdit {
                font-size: 14pt;
                background-color: #E3F2FD; /* Light Blue */
                color: #1565C0; /* Dark Blue */
            }
        """

    @staticmethod
    def get_button_style():
        return """
            QPushButton {
                background-color: #1565C0; /* Dark Blue */
                color: #fff;
                border: none;
                padding: 8px 16px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #1976D2; /* Slightly darker Blue */
            }"""