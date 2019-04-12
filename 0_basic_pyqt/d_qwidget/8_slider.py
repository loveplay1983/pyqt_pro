# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


class MainWin(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)

        self.setWindowTitle('slider demo')

        """
        QSlider provides a slide-bar widget, which functions internally much like a QDoubleSpinBox. Rather
    than display the current value numerically, it is represented by the position of the slider handle
    along the length of the widget. This is often useful when providing adjustment between two
    extremes, but where absolutel accuracy is not required. The most common use of this type of
    widget is for volume controls.
        """

        widget = QSlider(Qt.Horizontal)
        widget.setMaximum(10)
        widget.setMinimum(-10)
        widget.setSingleStep(1)

        # signal and slot
        widget.valueChanged.connect(self.val_change)
        widget.sliderMoved.connect(self.slider_move)
        widget.sliderPressed.connect(self.slider_press)
        widget.sliderReleased.connect(self.slider_release)

        self.setCentralWidget(widget)

    def val_change(self, i):
        print(i)

    def slider_move(self, p):
        print(p)

    def slider_press(self):
        print('Pressed!!!')

    def slider_release(self):
        print('Released!!!')

app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()
