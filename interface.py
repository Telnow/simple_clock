import time

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class Watch_interface(QWidget):

    def main_interface(self):
        self.resize(300, 100)
        self.setWindowTitle('Часы')

        font = QFont()
        font.setPointSize(25)
        self.label = QLabel()
        self.label.setFont(font)
        self.label.setText(time.strftime('%H:%M:%S'))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox_container = QVBoxLayout()
        self.vbox_container.addWidget(self.label)
        self.setLayout(self.vbox_container)