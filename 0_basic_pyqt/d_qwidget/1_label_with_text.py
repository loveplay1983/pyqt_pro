from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

# QMainWindow is part of QtWidgets
class MainWin(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)

        self.setWindowTitle("QWidget Demo")

        label1 = QLabel('label1')
        font = label1.font()
        font.setPointSize(30)
        label1.setFont(font)
        # label1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label1.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label1)


app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()