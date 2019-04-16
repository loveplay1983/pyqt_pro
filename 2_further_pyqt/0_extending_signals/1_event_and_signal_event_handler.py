# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber,
                             QSlider, QVBoxLayout,
                             QApplication, QGridLayout,
                             QLabel)


class Example(QWidget):
    """
    This is a simple example demonstrating signals and slots in PyQt5.
    """

    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        sld.setRange(1, 100)
        sld.setSingleStep(1)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        sld.valueChanged.connect(lcd.display)
        # x and y coordinate w, h for frame
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot demo')
        self.show()

    # Reimplementing event handler   -  Events in PyQt5 are processed often by reimplementing event handlers.
    # Inherited from QWidget
    ##############################################
    # keyPressEvent(self, e) is the event handler#
    ##############################################
    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
