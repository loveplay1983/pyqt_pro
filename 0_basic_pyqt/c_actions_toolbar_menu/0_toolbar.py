from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MainWindow(QMainWindow):
    """
    There are couple of different ways to implement singal and slot in qt and pyqt
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Toolbar demo')

        label = QLabel('Toobar demo')
        label.setAlignment(Qt.AlignLeft)

        self.setCentralWidget(label)

        toolbar = QToolBar('My toolbar')
        # self -> MainWindow object
        self.addToolBar(toolbar)

    def onMyToolBarClick(self, s):
        print('Clicked', s)


app = QApplication(sys.argv)

win = MainWindow()
win.show()

app.exec_()
