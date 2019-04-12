# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


class MainWin(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWin, self).__init__(*args, **kwargs)

        self.setWindowTitle('combox demo')

        """
        QListBox offers an currentItemChanged signal which sends the QListItem (the element of the list box),
and a currentTextChanged signal which sends the text.

        """
        widget = QComboBox()
        widget.addItems(['one', '2', 'III'])
        widget.currentIndexChanged.connect(self.index_changed)      # return current index
        widget.currentIndexChanged[str].connect(self.txt_changed)   # return the actual value of the index
        widget.setEditable(True)

        """
        You can also set a flag to determine how the insert is handled.
        
        QComboBox.NoInsert                              No insert
        QComboBox.InsertAtTop                           Insert as first item
        QComboBox.InsertAtCurrent                       Replace currently selected item
        QComboBox.InsertAtBottom                        Insert after last item
        QComboBox.InsertAfterCurrent                    Insert after current item
        QComboBox.InsertBeforeCurrent                   Insert before current item
        QComboBox.InsertAlphabetically                  Insert in alphabetical order
        """

        widget.setInsertPolicy(QComboBox.InsertAfterCurrent)
        widget.setMaxCount(10)
        self.setCentralWidget(widget)

    def index_changed(self, i):

        print(i)

    def txt_changed(self, s):

        print(s)

app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec_()
