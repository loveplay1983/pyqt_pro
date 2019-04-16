# -*- coding: utf-8 -*-

"""
Sometimes it is convenient to know which widget is the sender of a signal.
For this, PyQt5 has the sender() method.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber,
                             QSlider, QVBoxLayout,
                             QApplication, QGridLayout,
                             QLabel, QPushButton, QMainWindow)


class Example(QMainWindow):
    """
    This is a simple example demonstrating signals and slots in PyQt5.
    """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn1 = QPushButton('Button1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('Button2', self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.btn_clicked)
        btn2.clicked.connect(self.btn_clicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def btn_clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + 'was pressed.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
