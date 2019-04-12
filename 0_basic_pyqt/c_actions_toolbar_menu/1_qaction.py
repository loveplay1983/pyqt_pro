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
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My toolbar')
        # self -> MainWindow object
        self.addToolBar(toolbar)

        button_action = QAction('Your button', self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolBarClick)

        toolbar.addAction(button_action)

        # add status bar
        self.setStatusBar(QStatusBar(self))

    def onMyToolBarClick(self, s):
        print('Clicked', s)


app = QApplication(sys.argv)

win = MainWindow()
win.show()

app.exec_()
