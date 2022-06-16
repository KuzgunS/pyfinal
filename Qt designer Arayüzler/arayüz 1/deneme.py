# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deneme.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 669)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 50, 441, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.text_to_be_deleted = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.text_to_be_deleted.setObjectName("text_to_be_deleted")
        self.gridLayout_3.addWidget(self.text_to_be_deleted, 1, 0, 1, 1)
        self.label_of_tobedeleted = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(True)
        font.setKerning(True)
        self.label_of_tobedeleted.setFont(font)
        self.label_of_tobedeleted.setObjectName("label_of_tobedeleted")
        self.gridLayout_3.addWidget(self.label_of_tobedeleted, 0, 0, 1, 1)
        self.push_to_delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.push_to_delete.setObjectName("push_to_delete")
        self.gridLayout_3.addWidget(self.push_to_delete, 0, 1, 1, 1)
        self.push_to_make = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.push_to_make.setObjectName("push_to_make")
        self.gridLayout_3.addWidget(self.push_to_make, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.push_to_delete.clicked.connect(self.text_to_be_deleted.clear) # type: ignore
        self.push_to_make.clicked.connect(self.text_to_be_deleted.undo) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Designer deneme"))
        self.text_to_be_deleted.setText(_translate("MainWindow", "Sil"))
        self.label_of_tobedeleted.setText(_translate("MainWindow", "Deneme etiketi"))
        self.push_to_delete.setText(_translate("MainWindow", "SİLMEK İÇİN BANA BAS"))
        self.push_to_make.setText(_translate("MainWindow", "OLUŞTURMAK İÇİN BANA BAS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
