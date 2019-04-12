# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


class MainWin(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)

        self.setWindowTitle('checkbox demo')

        widget = QCheckBox()

        """
        You can set a checkbox state programmatically using .setChecked or .setCheckState. 
        The former accepts either True or False representing checked or unchecked respectively. 
        However, with .setCheckState you also specify a particially checked state using a Qt. namespace flag:
        
        Qt.Unchecked                       Item is unchecked
        Qt.PartiallyChecked                Item is partially checked
        Qt.Checked                         Item is unchecked
        
        In addition to the checked and unchecked states, there is a third state: partially checked. 
        This state indicates that the regular checked/unchecked state can not be determined; generally because of 
        other states that affect the checkbox. This state is useful when several child nodes are selected in a treeview, 
        for example.
        """
        widget.setCheckState(Qt.PartiallyChecked)
        # widget.setChecked(True)

        # For tristate(三态):
        # widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)

        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)


app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()
