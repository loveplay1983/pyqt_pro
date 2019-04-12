# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


class MainWin(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)

        self.setWindowTitle('spinbox demo')

        widget = QSpinBox()
        # widget = QDoubleSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(10)
        # widget.setRange(-10, 10)

        widget.setPrefix('_')
        widget.setSuffix('_')

        widget.setSingleStep(1)

        # signal and slot
        """
        Both QSpinBox and QDoubleSpinBox have a .valueChanged signal which fires whenever their value is
altered. The raw .valueChanged signal sends the numeric value (either an int or a float) while the
str alternate signal, accessible via .valueChanged[str] sends the value as a string, including both the
prefix and suffix characters.
        """
        widget.valueChanged.connect(self.value_changed)
        # widget.valueChanged[str].connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)
    def value_changed_str(self, s):
        print(s)

app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()
