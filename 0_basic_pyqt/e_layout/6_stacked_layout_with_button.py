# -*- coding: utf-8 -*-
"""
QHBoxLayout             Linear horizontal layout
QVBoxLayout             Linear vertical layout
QGridLayout             In indexable grid XxY
QStackedLayout          Stacked (z) in front of one another
"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


class Color(QWidget):

    # Note that "color" is a string which used as an input argument later on for Qcolor() method
    # line 19 <-> line 35
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)

        self.setAutoFillBackground(True)

        # palette() is the function contained within Qwidget
        # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qwidget.html?highlight=qwidget#palette
        palette = self.palette()

        # PyQt5.QtGui.QPalette
        # https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtgui/qpalette.html
        # The QPalette class contains color groups for each widget state.

        # PyQt5.QtGui.QColor
        # The QColor class provides colors based on RGB, HSV or CMYK values.
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWin(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)

        self.setWindowTitle('Layout demo')

        layout_total = QVBoxLayout()
        layout_button = QHBoxLayout()
        layout_stacked = QStackedLayout()

        layout_total.addLayout(layout_button)
        layout_total.addLayout(layout_stacked)

        for n, color in enumerate(['red', 'green', 'blue', 'yellow', 'purple']):
            btn = QPushButton(str(color))
            btn.pressed.connect(lambda x=n: layout_stacked.setCurrentIndex(x))
            layout_button.addWidget(btn)
            layout_stacked.addWidget(Color(color))

        widget = QWidget()
        widget.setLayout(layout_total)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()
