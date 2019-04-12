from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

# Event handlers
"""
class CustomButton(Qbutton):
    def keyPressEvent(self, e):
        # My custom event handling
        super(CustomButton, self).keyPressEvent(e)

class CustomButton99(Qbutton):
    def keyPressEvent(self, e):
        # My custom event handling
        super(CustomButton99, self).keyPressEvent(e)
"""


class MainWindow(QMainWindow):
    """
    There are couple of different ways to implement singal and slot in qt and pyqt
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # self.windowTitleChanged.connect is signal
        # self.onWindowTitleChange is slot

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title will be passed to the function.

        self.windowTitleChanged.connect(self.onWindowTitleChange)

        self.windowTitleChanged.connect(lambda x: self.my_custom_fun())

        self.windowTitleChanged.connect(lambda x: self.my_custom_fun(x))

        self.windowTitleChanged.connect(lambda x: self.my_custom_fun(x, 25))

        self.setWindowTitle('My awesome app')

        label = QLabel('Signal demo')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    def onWindowTitleChange(self, s):
        print(s)

    def my_custom_fun(self, a='Hello', b=5):
        print(a, b)


app = QApplication(sys.argv)

win = MainWindow()
win.show()

app.exec_()
