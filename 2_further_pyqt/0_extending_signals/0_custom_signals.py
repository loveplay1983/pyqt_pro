# -*- coding: utf-8 -*-

"""
The final bit of signals we’re going to cover is custom signals.
These allow you to use the Qt event loop to send data around your
application. It’s a great way to keep your app modular and responsive.
"""

# You can define your own signals using the pyQtSignal method provided by PyQt5.
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication

# def MainWindow(QMainWindow):
#     message = pyqtSignal(str)
#     value = pyqtSignal(int)


# window.value.emit(23) # Signal on another object.
# self.message.emit("my message") # Signal on self.

# def MyClass(QObject):
#     keyvalue = pyqtSignal(dict)
#     data = pyqtSignal(tuple)

