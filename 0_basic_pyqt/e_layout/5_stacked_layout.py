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

        layout_total = QVBoxLayout()

        # Define layouts
        self.layout_stacked = QStackedLayout()

        self.layout_stacked.addWidget(Color('red'))
        self.layout_stacked.addWidget(Color('black'))
        self.layout_stacked.addWidget(Color('purple'))
        self.layout_stacked.addWidget(Color('brown'))
        self.layout_stacked.addWidget(Color('green'))
        self.layout_stacked.addWidget(Color('yellow'))
        self.layout_stacked.addWidget(Color('dark'))

        self.layout_stacked.setCurrentIndex(4)

        self.layout = QVBoxLayout()

        button = QPushButton('Switch')
        self.layout.addWidget(button)
        button.clicked.connect(lambda next: self.on_click(next))

        layout_total.addLayout(self.layout_stacked)
        layout_total.addLayout(self.layout)

        widget = QWidget()
        widget.setLayout(layout_total)
        self.setCentralWidget(widget)

    def on_click(self, next):
        self.layout_stacked.setCurrentIndex(next+1)


app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()
