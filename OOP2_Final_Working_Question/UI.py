# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(629, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_primes = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_primes.setGeometry(QtCore.QRect(100, 20, 331, 131))
        self.textEdit_primes.setReadOnly(True)
        self.textEdit_primes.setObjectName("textEdit_primes")
        self.lineEdit_number = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_number.setGeometry(QtCore.QRect(220, 170, 211, 21))
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.label_enter_number = QtWidgets.QLabel(self.centralwidget)
        self.label_enter_number.setGeometry(QtCore.QRect(110, 170, 91, 16))
        self.label_enter_number.setObjectName("label_enter_number")
        self.comboBox_run_settings = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_run_settings.setGeometry(QtCore.QRect(100, 210, 121, 22))
        self.comboBox_run_settings.setObjectName("comboBox_run_settings")
        self.comboBox_run_settings.addItem("")
        self.comboBox_run_settings.addItem("")
        self.pushButton_run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_run.setGeometry(QtCore.QRect(240, 210, 93, 28))
        self.pushButton_run.setObjectName("pushButton_run")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(100, 250, 331, 16))
        self.label_status.setObjectName("label_status")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_enter_number.setText(_translate("MainWindow", "Enter Number"))
        self.comboBox_run_settings.setItemText(0, _translate("MainWindow", "Print the text box"))
        self.comboBox_run_settings.setItemText(1, _translate("MainWindow", "Write to file"))
        self.pushButton_run.setText(_translate("MainWindow", "RUN"))
        self.label_status.setText(_translate("MainWindow", "STATUS: "))