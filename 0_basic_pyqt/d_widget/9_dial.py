# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


class MainWin(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)

        self.setWindowTitle('dial demo')

        """
        the QDial is a rotateable widget that functions just like the slider, but appears as an
analogue dial. This looks nice, but from a UI perspective is not particularly userfriendly. However,
they are often used in audio applications as representation of real-world analogue dials.
        """
        widget = QDial()
        widget.setRange(-100, 100)
        # widget.maximum()
        # widget.minimum()
        widget.setSingleStep(2.5)

        """
        The signals are the same as for QSlider and retain the same names (e.g. .sliderMoved).
        """

        widget.valueChanged.connect(self.val_change)
        widget.sliderMoved.connect(self.slider_move)
        widget.sliderPressed.connect(self.slider_press)
        widget.sliderReleased.connect(self.slider_release)

        self.setCentralWidget(widget)

    def val_change(self, c):
        print(c)

    def slider_move(self, m):
        print(m)

    def slider_press(self):
        print('pressed')

    def slider_release(self):
        print('released')


app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()
