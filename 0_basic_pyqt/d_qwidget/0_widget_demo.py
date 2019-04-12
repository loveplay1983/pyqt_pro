from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# Only needed for access to command line arguments
import sys


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.width = 800
        self.height = 600
        self.left = 500
        self.top = 200
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setWindowTitle("My Awesome App")
        layout = QVBoxLayout()
        # Tricky part which to add all the widgets you want in one swoop
        widgets = [QCheckBox,
                   QComboBox,
                   QDateEdit,
                   QDateTimeEdit,
                   QDial,
                   QDoubleSpinBox,
                   QFontComboBox,
                   QLCDNumber,
                   QLabel,
                   QLineEdit,
                   QProgressBar,
                   QPushButton,
                   QRadioButton,
                   QSlider,
                   QSpinBox,
                   QTimeEdit]
        for w in widgets:
            layout.addWidget(w())      # It needs () right after w since each w element is a class

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.

app = QApplication(sys.argv)
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.
# Start the event loop.
app.exec_()
# Your application won't reach here until you exit and the event
# loop has stopped.
