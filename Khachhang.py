import sys
import os
from source.GUIsearch import *
from source.modules.library.IO_support import *

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def Open_GUI():
    global ui
    ui = GUIsearch.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()