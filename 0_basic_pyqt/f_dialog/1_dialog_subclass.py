# -*- coding: utf8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


class MyDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(MyDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle('customized dialog')

        dlg_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.button_box = QDialogButtonBox(dlg_btn)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        label = QLabel('dialog demo')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My toolbar')
        # self -> MainWindow object
        self.addToolBar(toolbar)

        button_action = QAction('Your button', self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.on_tool_bar_click)

        toolbar.addAction(button_action)

        # add status bar
        self.setStatusBar(QStatusBar(self))

    def on_tool_bar_click(self, s):
        print('Clicked', s)

        # Making this dialog window a modal window
        dlg = MyDialog(self)
        # dlg.setGeometry(400, 500, 800, 600)
        dlg.setWindowTitle('MessageBox')
        if dlg.exec_():
            print('Success!')
        else:
            print('Cancel!')


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
