# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


class MainWin(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)

        self.setWindowTitle('listbox demo')

        widget = QListWidget()
        widget.addItems(['1', 'b', 'three'])

        widget.currentItemChanged.connect(self.index_changed)
        # widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):

        # print(i.text())
        print(i)

    def text_changed(self, s):

        print(s)

app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()
