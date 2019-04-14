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

        # Layout can sometimes be stacked together i.e. nested layouts

        # Define layouts
        layout_h = QHBoxLayout()

        layout_h.setContentsMargins(0, 0, 0, 0)
        layout_h.setSpacing(0)

        # Define QGridLayout
        layout_grid_1 = QGridLayout()
        layout_grid_2 = QGridLayout()

        layout_grid_1.addWidget(Color('red'), 0, 0)
        layout_grid_1.addWidget(Color('green'), 0, 1)
        layout_grid_1.addWidget(Color('blue'), 1, 0)
        layout_grid_1.addWidget(Color('purple'), 1, 1)

        layout_grid_2.addWidget(Color('yellow'), 0, 0)
        layout_grid_2.addWidget(Color('white'), 0, 1)
        layout_grid_2.addWidget(Color('white'), 1, 0)
        layout_grid_2.addWidget(Color('black'), 1, 1)

        # Hook the sub-layouts with overall layout
        layout_h.addLayout(layout_grid_1)
        layout_h.addLayout(layout_grid_2)

        # Define QWidget object which in this case will hold all the layouts
        widget = QWidget()
        widget.setLayout(layout_h)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()
