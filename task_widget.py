from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QCheckBox
from PyQt6.QtGui import QFont

class TaskWidget(QWidget):
    def __init__(self, text):
        super().__init__()
        self.task_label = QLabel(text)
        self.checkbox = QCheckBox()
        self.task_label.setFont(QFont("Arial", 15))
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.task_label)
        self.setLayout(layout)

    def isChecked(self):
        return self.checkbox.isChecked()
