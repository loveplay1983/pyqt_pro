# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


class MainWin(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)

        self.setWindowTitle('lineedit demo')

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText('Hello World')

        # widget.setReadOnly(True)

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        widget.setInputMask('000.000.000.000;_')

        self.setCentralWidget(widget)

    def return_pressed(self):
        print('Return pressed!')
        self.centralWidget().setText('Boom!')

    def selection_changed(self):
        print('Selection changed')
        qDebug('Selection changed')

    def text_changed(self, s):
        print('Text changed')
        print(s)

    def text_edited(self, s):
        print('Text edited...')
        print(s)

app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()
