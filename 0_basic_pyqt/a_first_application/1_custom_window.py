"""
If you want to create a custom window, the best approach is to subclass QMainWindow and then
include the setup for the window in the __init__ block. This allows the window behaviour to be self
contained. We can add our own subclass of QMainWindow — call it MainWindow to keep things simple.
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('My awesome application')
        label = QLabel('Demo label')

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)


app = QApplication(sys.argv)

win = MainWindow()
win.show()

app.exec_()
