# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIdisplay.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(987, 670)
        self.QA_actionOpen = QAction(MainWindow)
        self.QA_actionOpen.setObjectName(u"QA_actionOpen")
        self.QA_actionNew = QAction(MainWindow)
        self.QA_actionNew.setObjectName(u"QA_actionNew")
        self.QA_actionSave = QAction(MainWindow)
        self.QA_actionSave.setObjectName(u"QA_actionSave")
        self.QA_actionSave_as = QAction(MainWindow)
        self.QA_actionSave_as.setObjectName(u"QA_actionSave_as")
        self.QA_actionPrint = QAction(MainWindow)
        self.QA_actionPrint.setObjectName(u"QA_actionPrint")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.GB_information_custom = QGroupBox(self.centralwidget)
        self.GB_information_custom.setObjectName(u"GB_information_custom")
        self.GB_information_custom.setGeometry(QRect(20, 10, 381, 261))
        font = QFont()
        font.setPointSize(13)
        self.GB_information_custom.setFont(font)
        self.label_address = QLabel(self.GB_information_custom)
        self.label_address.setObjectName(u"label_address")
        self.label_address.setGeometry(QRect(10, 164, 51, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_address.setFont(font1)
        self.TE_num_phone = QTextEdit(self.GB_information_custom)
        self.TE_num_phone.setObjectName(u"TE_num_phone")
        self.TE_num_phone.setGeometry(QRect(135, 134, 239, 24))
        self.label_name = QLabel(self.GB_information_custom)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(10, 40, 117, 21))
        self.label_name.setFont(font1)
        self.TE_lices_num = QTextEdit(self.GB_information_custom)
        self.TE_lices_num.setObjectName(u"TE_lices_num")
        self.TE_lices_num.setGeometry(QRect(135, 103, 239, 24))
        self.label_fix_car = QLabel(self.GB_information_custom)
        self.label_fix_car.setObjectName(u"label_fix_car")
        self.label_fix_car.setGeometry(QRect(9, 229, 110, 21))
        self.label_fix_car.setFont(font1)
        self.label_date_fix = QLabel(self.GB_information_custom)
        self.label_date_fix.setObjectName(u"label_date_fix")
        self.label_date_fix.setGeometry(QRect(10, 195, 110, 21))
        self.label_date_fix.setFont(font1)
        self.label_lices_num = QLabel(self.GB_information_custom)
        self.label_lices_num.setObjectName(u"label_lices_num")
        self.label_lices_num.setGeometry(QRect(10, 102, 55, 21))
        self.label_lices_num.setFont(font1)
        self.TE_fix_car = QTextEdit(self.GB_information_custom)
        self.TE_fix_car.setObjectName(u"TE_fix_car")
        self.TE_fix_car.setGeometry(QRect(135, 227, 239, 23))
        self.TE_date = QTextEdit(self.GB_information_custom)
        self.TE_date.setObjectName(u"TE_date")
        self.TE_date.setGeometry(QRect(135, 196, 239, 24))
        self.TE_name = QTextEdit(self.GB_information_custom)
        self.TE_name.setObjectName(u"TE_name")
        self.TE_name.setGeometry(QRect(135, 41, 239, 24))
        self.label_num_vin = QLabel(self.GB_information_custom)
        self.label_num_vin.setObjectName(u"label_num_vin")
        self.label_num_vin.setGeometry(QRect(10, 71, 54, 21))
        self.label_num_vin.setFont(font1)
        self.label_num_phone = QLabel(self.GB_information_custom)
        self.label_num_phone.setObjectName(u"label_num_phone")
        self.label_num_phone.setGeometry(QRect(10, 133, 31, 21))
        self.label_num_phone.setFont(font1)
        self.TE_address = QTextEdit(self.GB_information_custom)
        self.TE_address.setObjectName(u"TE_address")
        self.TE_address.setGeometry(QRect(135, 165, 239, 24))
        self.TE_vin_num = QTextEdit(self.GB_information_custom)
        self.TE_vin_num.setObjectName(u"TE_vin_num")
        self.TE_vin_num.setGeometry(QRect(135, 72, 239, 24))
        self.GB_car_number_VIN = QGroupBox(self.centralwidget)
        self.GB_car_number_VIN.setObjectName(u"GB_car_number_VIN")
        self.GB_car_number_VIN.setGeometry(QRect(10, 280, 391, 281))
        self.GB_car_number_VIN.setFont(font)
        self.label_area = QLabel(self.GB_car_number_VIN)
        self.label_area.setObjectName(u"label_area")
        self.label_area.setGeometry(QRect(10, 30, 117, 21))
        self.label_area.setFont(font1)
        self.TE_num_product = QTextEdit(self.GB_car_number_VIN)
        self.TE_num_product.setObjectName(u"TE_num_product")
        self.TE_num_product.setGeometry(QRect(160, 240, 221, 24))
        self.TE_product_date = QTextEdit(self.GB_car_number_VIN)
        self.TE_product_date.setObjectName(u"TE_product_date")
        self.TE_product_date.setGeometry(QRect(160, 180, 221, 24))
        self.label_product_date = QLabel(self.GB_car_number_VIN)
        self.label_product_date.setObjectName(u"label_product_date")
        self.label_product_date.setGeometry(QRect(10, 180, 117, 21))
        self.label_product_date.setFont(font1)
        self.TE_factory = QTextEdit(self.GB_car_number_VIN)
        self.TE_factory.setObjectName(u"TE_factory")
        self.TE_factory.setGeometry(QRect(160, 210, 221, 24))
        self.label_sec_num = QLabel(self.GB_car_number_VIN)
        self.label_sec_num.setObjectName(u"label_sec_num")
        self.label_sec_num.setGeometry(QRect(10, 150, 117, 21))
        self.label_sec_num.setFont(font1)
        self.TE_area = QTextEdit(self.GB_car_number_VIN)
        self.TE_area.setObjectName(u"TE_area")
        self.TE_area.setGeometry(QRect(160, 30, 221, 24))
        self.label_num_product = QLabel(self.GB_car_number_VIN)
        self.label_num_product.setObjectName(u"label_num_product")
        self.label_num_product.setGeometry(QRect(10, 240, 141, 21))
        self.label_num_product.setFont(font1)
        self.TE_car_model = QTextEdit(self.GB_car_number_VIN)
        self.TE_car_model.setObjectName(u"TE_car_model")
        self.TE_car_model.setGeometry(QRect(160, 90, 221, 24))
        self.label_factory = QLabel(self.GB_car_number_VIN)
        self.label_factory.setObjectName(u"label_factory")
        self.label_factory.setGeometry(QRect(10, 210, 131, 21))
        self.label_factory.setFont(font1)
        self.TE_sec_num = QTextEdit(self.GB_car_number_VIN)
        self.TE_sec_num.setObjectName(u"TE_sec_num")
        self.TE_sec_num.setGeometry(QRect(160, 150, 221, 24))
        self.TE_name_car = QTextEdit(self.GB_car_number_VIN)
        self.TE_name_car.setObjectName(u"TE_name_car")
        self.TE_name_car.setGeometry(QRect(160, 120, 221, 24))
        self.label_car_model = QLabel(self.GB_car_number_VIN)
        self.label_car_model.setObjectName(u"label_car_model")
        self.label_car_model.setGeometry(QRect(10, 90, 117, 21))
        self.label_car_model.setFont(font1)
        self.TE_country = QTextEdit(self.GB_car_number_VIN)
        self.TE_country.setObjectName(u"TE_country")
        self.TE_country.setGeometry(QRect(160, 60, 221, 24))
        self.label_name_car = QLabel(self.GB_car_number_VIN)
        self.label_name_car.setObjectName(u"label_name_car")
        self.label_name_car.setGeometry(QRect(10, 120, 117, 21))
        self.label_name_car.setFont(font1)
        self.label_contry = QLabel(self.GB_car_number_VIN)
        self.label_contry.setObjectName(u"label_contry")
        self.label_contry.setGeometry(QRect(10, 60, 117, 21))
        self.label_contry.setFont(font1)
        self.widget_vin_num = QWidget(self.GB_car_number_VIN)
        self.widget_vin_num.setObjectName(u"widget_vin_num")
        self.widget_vin_num.setGeometry(QRect(410, -270, 381, 251))
        self.GB_diagnose = QGroupBox(self.centralwidget)
        self.GB_diagnose.setObjectName(u"GB_diagnose")
        self.GB_diagnose.setGeometry(QRect(410, 10, 571, 551))
        self.GB_diagnose.setFont(font)
        self.TE_diagnose = QTextEdit(self.GB_diagnose)
        self.TE_diagnose.setObjectName(u"TE_diagnose")
        self.TE_diagnose.setGeometry(QRect(10, 30, 551, 511))
        self.BT_graph = QPushButton(self.centralwidget)
        self.BT_graph.setObjectName(u"BT_graph")
        self.BT_graph.setGeometry(QRect(430, 580, 93, 28))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.BT_graph.setFont(font2)
        self.BT_fix = QPushButton(self.centralwidget)
        self.BT_fix.setObjectName(u"BT_fix")
        self.BT_fix.setGeometry(QRect(530, 580, 93, 28))
        self.BT_fix.setFont(font2)
        self.BT_graph_fix = QPushButton(self.centralwidget)
        self.BT_graph_fix.setObjectName(u"BT_graph_fix")
        self.BT_graph_fix.setGeometry(QRect(330, 580, 93, 28))
        self.BT_graph_fix.setFont(font2)
        self.BT_cancel_2 = QPushButton(self.centralwidget)
        self.BT_cancel_2.setObjectName(u"BT_cancel_2")
        self.BT_cancel_2.setGeometry(QRect(630, 580, 93, 28))
        self.BT_cancel_2.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 987, 26))
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuEdit.addAction(self.QA_actionOpen)
        self.menuEdit.addAction(self.QA_actionNew)
        self.menuEdit.addAction(self.QA_actionSave)
        self.menuEdit.addAction(self.QA_actionSave_as)
        self.menuEdit.addAction(self.QA_actionPrint)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.QA_actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.QA_actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.QA_actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.QA_actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.QA_actionPrint.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.GB_information_custom.setTitle(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin kh\u00e1ch h\u00e0ng", None))
        self.label_address.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"T\u00ean kh\u00e1ch h\u00e0ng", None))
        self.label_fix_car.setText(QCoreApplication.translate("MainWindow", u"L\u1ed7i xe", None))
        self.label_date_fix.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y s\u1eeda ch\u1eefa", None))
        self.label_lices_num.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3n s\u1ed1", None))
        self.label_num_vin.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 VIN", None))
        self.label_num_phone.setText(QCoreApplication.translate("MainWindow", u"S\u0110T", None))
        self.GB_car_number_VIN.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e3 xe ", None))
        self.label_area.setText(QCoreApplication.translate("MainWindow", u"Khu v\u1ef1c", None))
        self.label_product_date.setText(QCoreApplication.translate("MainWindow", u"N\u0103m s\u1ea3n xu\u1ea5t", None))
        self.label_sec_num.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 b\u1ea3o m\u1eadt", None))
        self.label_num_product.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 th\u1ee9 t\u1ef1 s\u1ea3n xu\u1ea5t", None))
        self.label_factory.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e0 m\u00e1y l\u1eafp r\u00e1p", None))
        self.label_car_model.setText(QCoreApplication.translate("MainWindow", u"M\u1eabu xe", None))
        self.label_name_car.setText(QCoreApplication.translate("MainWindow", u"H\u00e3ng xe", None))
        self.label_contry.setText(QCoreApplication.translate("MainWindow", u"N\u01b0\u1edbc s\u1ea3n xu\u1ea5t", None))
        self.GB_diagnose.setTitle(QCoreApplication.translate("MainWindow", u"Chu\u1ea9n \u0111o\u00e1n", None))
        self.BT_graph.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ed3 th\u1ecb", None))
        self.BT_fix.setText(QCoreApplication.translate("MainWindow", u"S\u1eeda ch\u1eefa", None))
        self.BT_graph_fix.setText(QCoreApplication.translate("MainWindow", u"H\u00ecnh \u1ea3nh xe", None))
        self.BT_cancel_2.setText(QCoreApplication.translate("MainWindow", u"Tho\u00e1t", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

