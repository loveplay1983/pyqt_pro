# -*- coding: utf-8 -*-

"""
Objects created from a QObject can emit signals.
The following example shows how we to emit custom signals.
"""

import sys

from PyQt5.QtCore import Qt, pyqtSignal, QObject

from PyQt5.QtWidgets import \
    (QWidget, QApplication, QMainWindow,
     QVBoxLayout, QGridLayout,
     QSlider, QLCDNumber, QLabel, QPushButton, )


class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):
    """
    This is a simple example demonstrating signals and slots in PyQt5.
    """

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.c = Communicate()
        ########################################################################
        ### connect closeApp(pyqtSignal instance) signal with self.close slot###
        ########################################################################
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emitting signal')
        self.show()

    def mousePressEvent(self, e):
        #############################################################
        # e is event object and mousePressEvent is event handler
        # self.c.closeApp.emit shows how we emit a customized signal
        # the signal was defined by pyqtSignal class
        #############################################################
        self.c.closeApp.emit()          # once the signal is emitted and received
                                        # the application is then closed since we
                                        # we have defined the self.close slot


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
