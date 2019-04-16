# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from main_win_demo_py import Ui_MainWindow

import random
import sys


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # You can still override values from your UI file within your code,
        # but if possible, set them in Qt Creator. See the properties panel.
        f = self.label.font()
        f.setPointSize(30)
        self.label.setAlignment(Qt.AlignLeft)

        self.label.setFont(f)

        # Signals from Ui widgts can be connected as normal
        self.pushButton.pressed.connect(self.update_label)

    def update_label(self):
        n = random.randint(1, 6)
        self.label.setText('%d' %n)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()
