from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from main_win import test
import sys


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QMainWindow()
    ui = test.Ui_MainWindow()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
