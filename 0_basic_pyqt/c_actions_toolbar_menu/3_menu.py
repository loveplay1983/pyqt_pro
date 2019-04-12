from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MainWindow(QMainWindow):
    """
    There are couple of different ways to implement singal and slot in qt and pyqt
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Toolbar demo')

        label = QLabel('Toobar demo')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My toolbar')
        toolbar.setIconSize(QSize(16, 16))
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # self -> MainWindow object
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('../../icon/fugue-icons-3.5.6-src/icons/acorn.png'), '&New', self)
        button_action.setStatusTip('This is button 1')
        button_action.triggered.connect(self.onMyToolBarClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon('../../icon/fugue-icons-3.5.6-src/icons/animal-dog.png'), '&Open', self)
        button_action2.setStatusTip('This is button 2')
        button_action2.triggered.connect(self.onMyToolBarClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        # add widgets
        toolbar.addWidget(QLabel('Hello world'))
        toolbar.addWidget(QCheckBox())

        # add status bar
        self.setStatusBar(QStatusBar(self))

        # add menu
        menu = self.menuBar()

        # file_menu = menu.addMenu('&File')
        file_menu = menu.addMenu('&File')
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        # file_menu.addAction(button_action)

        file_submenu = file_menu.addMenu("&Exit")
        file_submenu.addAction(button_action2)

    def onMyToolBarClick(self, s):
        print('Clicked', s)


app = QApplication(sys.argv)

win = MainWindow()
win.show()

app.exec_()
