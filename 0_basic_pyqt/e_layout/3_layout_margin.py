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
        layout_v_1 = QVBoxLayout()
        layout_v_2 = QVBoxLayout()

        # Define layout margin and spacing
        # You can find the difference between margin and non-margin very easily
        # Which the margin stands for how far away the distance between all the entities and the edge of window
        # Spacing is the distance in between different component
        layout_h.setContentsMargins(0, 0, 0, 0)
        layout_h.setSpacing(0)

        # Add widgets to different layouts
        layout_v_1.addWidget(Color('red'))
        layout_v_1.addWidget(Color('green'))
        layout_v_1.addWidget(Color('blue'))

        layout_v_2.addWidget(Color('purple'))
        layout_v_2.addWidget(Color('black'))
        layout_v_2.addWidget(Color('yellow'))

        # Now put sub-layouts to the overall layout
        layout_h.addLayout(layout_v_1)
        layout_h.addLayout(layout_v_2)

        # Define QWidget object which in this case will hold all the layouts
        widget = QWidget()
        widget.setLayout(layout_h)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()
