"""
The QApplication class
• QApplication holds the Qt event loop
• One QApplication instance required
• You application sits waiting in the event loop until an action is taken
• There is only one event loop


QtCore is the module that provides core infrastructure for Qt, it does not have any dependencies on UI resources,
it can be used for server and service type programs.

QtGui is the module that provides the main UI integration, the module that loads the QPA (Qt platform abstraction)
plugin and provides access to windows, drawing buffers and OpenGL (on platforms that support it).

QtWidgets is one of the UI modules that use the functionalities provided by QtCore and QtGui to high level UI
components such as buttons, etc.
"""


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arg
import sys

# app = QApplication([])
app = QApplication(sys.argv)

win = QMainWindow()
win.show()                    # IMPORTANT!!! Windows are hidden by default.

"""
The underscore is there because exec is a reserved word in Python and can’t be
used as a function name. PyQt5 handles this by appending an underscore to the
name used in the C++ library. You’ll also see it for .print_().
"""
app.exec_()


