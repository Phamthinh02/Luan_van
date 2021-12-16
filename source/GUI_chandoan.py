from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import numpy as np
# Import json module
from modules.library.IO_support import *


class Ui(QtWidgets.QMainWindow):
    """
    Application
    """

    def __init__(self, main_path):
        super(Ui, self).__init__()
        self.main_path = main_path
        # load GUI
        gui_path = os.path.abspath(
            os.path.join(main_path, "GUI", "GUI_chandoan.ui"))
        uic.loadUi(gui_path, self)
        # self.setup_pushButton_start()
        self.setup_pushButton_exit()
        self.show()
    
    def setup_pushButton_start(self):
        # GB_informatin_custom QGroupBox
        BT_start: QPushButton = self.findChild(QPushButton, "BT_start")
        BT_start.clicked.connect(self.BT_start_click)
        
    def BT_start_click(self):
        GB_value: QGroupBox = self.findChild(QGroupBox, "GB_value")
        LE_cyl_dm: QLineEdit = self.findChild(QLineEdit, "LE_cyl_dm")  
        LE_piston_jour: QLineEdit = self.findChild(QLineEdit, "LE_piston_jour")
        LE_rod_len: QLineEdit = self.findChild(QLineEdit, "LE_rod_len")
        LE_comp_rat: QLineEdit = self.findChild(QLineEdit, "LE_comp_rat")
        LE_xup_cor: QLineEdit = self.findChild(QLineEdit, "LE_xup_cor")
        
        
        
        GB_math: QGroupBox = self.findChild(QGroupBox, "GB_math")
        LE_extTem: QLineEdit = self.findChild(QLineEdit, "LE_extTem")    
        LE_mul_rat: QLineEdit = self.findChild(QLineEdit, "LE_mul_rat")
        LE_dym_comp_rat: QLineEdit = self.findChild(QLineEdit, "LE_dym_comp_rat")
        LE_max: QLineEdit = self.findChild(QLineEdit, "LE_max")
        LE_min: QLineEdit = self.findChild(QLineEdit, "LE_min")
        LE_load: QLineEdit = self.findChild(QLineEdit, "LE_load")
        
    def setup_pushButton_exit(self):
        # GB_informatin_custom QGroupBox
        BT_exit: QPushButton = self.findChild(QPushButton, "BT_exit")
        BT_exit.clicked.connect(self.BT_quit_click)
         
    def BT_quit_click(self):
        window.close()
        
if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    main_path = os.path.abspath(os.path.join(path, os.pardir))
    app = QtWidgets.QApplication(sys.argv)
    window = Ui(main_path=main_path)
    app.exec_()

