from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


# QMainWindow is part of QtWidgets
class MainWin(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)

        self.setWindowTitle("QPixmap Demo")

        widget = QLabel('Hello Kitty')
        widget.setPixmap(QPixmap('../../img/kitty.jpg'))
        widget.setScaledContents(True)

        self.setCentralWidget(widget)

        # btn = QPushButton('Click Me')
        # self.setCentralWidget(btn)


app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()
