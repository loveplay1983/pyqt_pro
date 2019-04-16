# -*- coding: utf-8 -*-

from main_win_demo_py import Ui_MainWindow

from PyQt5.QtWidgets import *

import sys


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
