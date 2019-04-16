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
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)
        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    ########################
    # e is the event object#
    ########################
    """
    The e is the event object; it contains data about the event that was triggered; 
    in our case, a mouse move event. With the x() and y() methods we determine the x and y 
    coordinates of the mouse pointer. We build the string and set it to the label widget.
    """

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = 'x:{0}, y:{1}'.format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
