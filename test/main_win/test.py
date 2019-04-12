# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# QMainWindow demo

# _*_ coding:utf-8 _*_
# import sys
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton)
# from PyQt5.QtGui import QIcon
#
# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.init_ui()
#
#     def init_ui(self):
#         #设置窗口属性
#         self.setGeometry(200, 200, 400, 200)
#         self.setWindowTitle('创建主窗口')
#         self.setWindowIcon(QIcon(r"E:\\1.jpg"))
#         #设置状态栏
#         self.status = self.statusBar()
#         self.status.showMessage('我是状态栏', 5000)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv[1:])
#
#     window = MainWindow()
#     window.show()
#
#     sys.exit(app.exec_())


from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMainWindow

class Ui_MainWindow(object):
    # Parameter MainWindow will have a concrete argument which is QMainWindow instance object
    # defined withint demo.py file
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHello_world = QtWidgets.QMenu(self.menubar)
        self.menuHello_world.setObjectName("menuHello_world")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHello_world.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHello_world.setTitle(_translate("MainWindow", "Hello world"))

