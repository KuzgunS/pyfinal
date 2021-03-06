"""@package docstring
Auto-generated UI module
Handles UI 
"""


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Image_Operator_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1420, 803)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 20, 1261, 839))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MainLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setObjectName("MainLayout")
        self.label_output_image = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_output_image.setMinimumSize(QtCore.QSize(500, 800))
        self.label_output_image.setText("")
        self.label_output_image.setPixmap(QtGui.QPixmap("other assets/generate output first.png"))
        self.label_output_image.setObjectName("label_output_image")
        self.MainLayout.addWidget(self.label_output_image, 2, 5, 1, 1)
        self.label_Output = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_Output.setFont(font)
        self.label_Output.setObjectName("label_Output")
        self.MainLayout.addWidget(self.label_Output, 1, 5, 1, 1)
        self.label_input_image = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_input_image.sizePolicy().hasHeightForWidth())
        self.label_input_image.setSizePolicy(sizePolicy)
        self.label_input_image.setMinimumSize(QtCore.QSize(500, 800))
        self.label_input_image.setBaseSize(QtCore.QSize(0, 0))
        self.label_input_image.setText("")
        self.label_input_image.setPixmap(QtGui.QPixmap("other assets/input a source image.png"))
        self.label_input_image.setObjectName("label_input_image")
        self.MainLayout.addWidget(self.label_input_image, 2, 3, 1, 1)
        self.label_Input = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_Input.setFont(font)
        self.label_Input.setObjectName("label_Input")
        self.MainLayout.addWidget(self.label_Input, 1, 3, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 121, 711))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Functions_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Functions_layout.setContentsMargins(0, 0, 0, 0)
        self.Functions_layout.setObjectName("Functions_layout")
        self.groupBox_Functions = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_Functions.setObjectName("groupBox_Functions")
        self.pushButton_Open_Source = QtWidgets.QPushButton(self.groupBox_Functions)
        self.pushButton_Open_Source.setEnabled(True)
        self.pushButton_Open_Source.setGeometry(QtCore.QRect(40, 30, 41, 28))
        self.pushButton_Open_Source.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/Open Source.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Open_Source.setIcon(icon1)
        self.pushButton_Open_Source.setObjectName("pushButton_Open_Source")
        self.groupBox_Edit = QtWidgets.QGroupBox(self.groupBox_Functions)
        self.groupBox_Edit.setGeometry(QtCore.QRect(0, 200, 121, 151))
        self.groupBox_Edit.setObjectName("groupBox_Edit")
        self.pushButton_Clear_Source = QtWidgets.QPushButton(self.groupBox_Edit)
        self.pushButton_Clear_Source.setEnabled(False)
        self.pushButton_Clear_Source.setGeometry(QtCore.QRect(40, 10, 31, 28))
        self.pushButton_Clear_Source.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/clear source.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Clear_Source.setIcon(icon2)
        self.pushButton_Clear_Source.setObjectName("pushButton_Clear_Source")
        self.pushButton_Clear_Output = QtWidgets.QPushButton(self.groupBox_Edit)
        self.pushButton_Clear_Output.setEnabled(False)
        self.pushButton_Clear_Output.setGeometry(QtCore.QRect(40, 40, 31, 28))
        self.pushButton_Clear_Output.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/clear output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Clear_Output.setIcon(icon3)
        self.pushButton_Clear_Output.setObjectName("pushButton_Clear_Output")
        self.pushButton_Undo_Output = QtWidgets.QPushButton(self.groupBox_Edit)
        self.pushButton_Undo_Output.setEnabled(False)
        self.pushButton_Undo_Output.setGeometry(QtCore.QRect(40, 70, 31, 28))
        self.pushButton_Undo_Output.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/undo output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Undo_Output.setIcon(icon4)
        self.pushButton_Undo_Output.setObjectName("pushButton_Undo_Output")
        self.pushButton_Redo_Output = QtWidgets.QPushButton(self.groupBox_Edit)
        self.pushButton_Redo_Output.setEnabled(False)
        self.pushButton_Redo_Output.setGeometry(QtCore.QRect(40, 100, 31, 28))
        self.pushButton_Redo_Output.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/redo output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Redo_Output.setIcon(icon5)
        self.pushButton_Redo_Output.setObjectName("pushButton_Redo_Output")
        self.groupBox_Conversion = QtWidgets.QGroupBox(self.groupBox_Functions)
        self.groupBox_Conversion.setGeometry(QtCore.QRect(0, 360, 120, 91))
        self.groupBox_Conversion.setObjectName("groupBox_Conversion")
        self.pushButton_RGB_to_Grayscale = QtWidgets.QPushButton(self.groupBox_Conversion)
        self.pushButton_RGB_to_Grayscale.setEnabled(False)
        self.pushButton_RGB_to_Grayscale.setGeometry(QtCore.QRect(40, 20, 31, 28))
        self.pushButton_RGB_to_Grayscale.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/rgb to gray.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_RGB_to_Grayscale.setIcon(icon6)
        self.pushButton_RGB_to_Grayscale.setObjectName("pushButton_RGB_to_Grayscale")
        self.pushButton_RGB_to_HSV = QtWidgets.QPushButton(self.groupBox_Conversion)
        self.pushButton_RGB_to_HSV.setEnabled(False)
        self.pushButton_RGB_to_HSV.setGeometry(QtCore.QRect(40, 50, 31, 28))
        self.pushButton_RGB_to_HSV.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/rgb to hsv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_RGB_to_HSV.setIcon(icon7)
        self.pushButton_RGB_to_HSV.setObjectName("pushButton_RGB_to_HSV")
        self.groupBox_Segmentation = QtWidgets.QGroupBox(self.groupBox_Functions)
        self.groupBox_Segmentation.setGeometry(QtCore.QRect(0, 450, 120, 111))
        self.groupBox_Segmentation.setObjectName("groupBox_Segmentation")
        self.pushButton_Multi_Otsu_Thresholding = QtWidgets.QPushButton(self.groupBox_Segmentation)
        self.pushButton_Multi_Otsu_Thresholding.setEnabled(False)
        self.pushButton_Multi_Otsu_Thresholding.setGeometry(QtCore.QRect(40, 20, 31, 28))
        self.pushButton_Multi_Otsu_Thresholding.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/Multi otsu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Multi_Otsu_Thresholding.setIcon(icon8)
        self.pushButton_Multi_Otsu_Thresholding.setObjectName("pushButton_Multi_Otsu_Thresholding")
        self.pushButton_Chan_Vese_Segmentation = QtWidgets.QPushButton(self.groupBox_Segmentation)
        self.pushButton_Chan_Vese_Segmentation.setEnabled(False)
        self.pushButton_Chan_Vese_Segmentation.setGeometry(QtCore.QRect(40, 50, 31, 28))
        self.pushButton_Chan_Vese_Segmentation.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/chan vese.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Chan_Vese_Segmentation.setIcon(icon9)
        self.pushButton_Chan_Vese_Segmentation.setObjectName("pushButton_Chan_Vese_Segmentation")
        self.pushButton_Morphological_Snakes = QtWidgets.QPushButton(self.groupBox_Segmentation)
        self.pushButton_Morphological_Snakes.setEnabled(False)
        self.pushButton_Morphological_Snakes.setGeometry(QtCore.QRect(40, 80, 31, 31))
        self.pushButton_Morphological_Snakes.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/morphological.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Morphological_Snakes.setIcon(icon10)
        self.pushButton_Morphological_Snakes.setObjectName("pushButton_Morphological_Snakes")
        self.groupBox_Edge_Detection = QtWidgets.QGroupBox(self.groupBox_Functions)
        self.groupBox_Edge_Detection.setGeometry(QtCore.QRect(0, 570, 120, 141))
        self.groupBox_Edge_Detection.setObjectName("groupBox_Edge_Detection")
        self.pushButton_Prewitt = QtWidgets.QPushButton(self.groupBox_Edge_Detection)
        self.pushButton_Prewitt.setEnabled(False)
        self.pushButton_Prewitt.setGeometry(QtCore.QRect(40, 110, 31, 28))
        self.pushButton_Prewitt.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/Prewitt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Prewitt.setIcon(icon11)
        self.pushButton_Prewitt.setObjectName("pushButton_Prewitt")
        self.pushButton_Roberts = QtWidgets.QPushButton(self.groupBox_Edge_Detection)
        self.pushButton_Roberts.setEnabled(False)
        self.pushButton_Roberts.setGeometry(QtCore.QRect(40, 20, 31, 28))
        self.pushButton_Roberts.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/Roberts.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Roberts.setIcon(icon12)
        self.pushButton_Roberts.setObjectName("pushButton_Roberts")
        self.pushButton_Scharr = QtWidgets.QPushButton(self.groupBox_Edge_Detection)
        self.pushButton_Scharr.setEnabled(False)
        self.pushButton_Scharr.setGeometry(QtCore.QRect(40, 80, 31, 28))
        self.pushButton_Scharr.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/Scharr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Scharr.setIcon(icon13)
        self.pushButton_Scharr.setObjectName("pushButton_Scharr")
        self.pushButton_Sobel = QtWidgets.QPushButton(self.groupBox_Edge_Detection)
        self.pushButton_Sobel.setEnabled(False)
        self.pushButton_Sobel.setGeometry(QtCore.QRect(40, 50, 31, 28))
        self.pushButton_Sobel.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/Sobel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Sobel.setIcon(icon14)
        self.pushButton_Sobel.setObjectName("pushButton_Sobel")
        self.pushButton_Save_Output = QtWidgets.QPushButton(self.groupBox_Functions)
        self.pushButton_Save_Output.setEnabled(False)
        self.pushButton_Save_Output.setGeometry(QtCore.QRect(40, 60, 41, 28))
        self.pushButton_Save_Output.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/Save Output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Save_Output.setIcon(icon15)
        self.pushButton_Save_Output.setObjectName("pushButton_Save_Output")
        self.pushButton_Save_as_Output = QtWidgets.QPushButton(self.groupBox_Functions)
        self.pushButton_Save_as_Output.setEnabled(False)
        self.pushButton_Save_as_Output.setGeometry(QtCore.QRect(40, 90, 41, 28))
        self.pushButton_Save_as_Output.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/Save As.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Save_as_Output.setIcon(icon16)
        self.pushButton_Save_as_Output.setObjectName("pushButton_Save_as_Output")
        self.pushButton_Export_as_Source = QtWidgets.QPushButton(self.groupBox_Functions)
        self.pushButton_Export_as_Source.setEnabled(False)
        self.pushButton_Export_as_Source.setGeometry(QtCore.QRect(40, 130, 31, 31))
        self.pushButton_Export_as_Source.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icons/Export As_Source.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Export_as_Source.setIcon(icon17)
        self.pushButton_Export_as_Source.setObjectName("pushButton_Export_as_Source")
        self.pushButton_Export_as_Output = QtWidgets.QPushButton(self.groupBox_Functions)
        self.pushButton_Export_as_Output.setEnabled(False)
        self.pushButton_Export_as_Output.setGeometry(QtCore.QRect(40, 160, 31, 31))
        self.pushButton_Export_as_Output.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icons/Export As_ Output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Export_as_Output.setIcon(icon18)
        self.pushButton_Export_as_Output.setObjectName("pushButton_Export_as_Output")
        self.Functions_layout.addWidget(self.groupBox_Functions)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1420, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_As = QtWidgets.QMenu(self.menuFile)
        self.menuExport_As.setEnabled(False)
        self.menuExport_As.setObjectName("menuExport_As")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuClear = QtWidgets.QMenu(self.menuEdit)
        self.menuClear.setEnabled(False)
        self.menuClear.setObjectName("menuClear")
        self.menuConversion = QtWidgets.QMenu(self.menubar)
        self.menuConversion.setObjectName("menuConversion")
        self.menuSegmentation = QtWidgets.QMenu(self.menubar)
        self.menuSegmentation.setObjectName("menuSegmentation")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menu_Open_Source = QtWidgets.QAction(MainWindow)
        self.menu_Open_Source.setIcon(icon1)
        self.menu_Open_Source.setObjectName("menu_Open_Source")
        self.menu_Save_Output = QtWidgets.QAction(MainWindow)
        self.menu_Save_Output.setEnabled(False)
        self.menu_Save_Output.setIcon(icon15)
        self.menu_Save_Output.setObjectName("menu_Save_Output")
        self.menu_Save_As_Output = QtWidgets.QAction(MainWindow)
        self.menu_Save_As_Output.setEnabled(False)
        self.menu_Save_As_Output.setIcon(icon16)
        self.menu_Save_As_Output.setObjectName("menu_Save_As_Output")
        self.menu_Exit = QtWidgets.QAction(MainWindow)
        self.menu_Exit.setEnabled(True)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icons/exit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_Exit.setIcon(icon19)
        self.menu_Exit.setObjectName("menu_Exit")
        self.menu_Export_As_Source = QtWidgets.QAction(MainWindow)
        self.menu_Export_As_Source.setEnabled(False)
        self.menu_Export_As_Source.setIcon(icon17)
        self.menu_Export_As_Source.setObjectName("menu_Export_As_Source")
        self.menu_Export_As_Output = QtWidgets.QAction(MainWindow)
        self.menu_Export_As_Output.setEnabled(False)
        self.menu_Export_As_Output.setIcon(icon18)
        self.menu_Export_As_Output.setObjectName("menu_Export_As_Output")
        self.menu_Clear_Source = QtWidgets.QAction(MainWindow)
        self.menu_Clear_Source.setEnabled(False)
        self.menu_Clear_Source.setIcon(icon2)
        self.menu_Clear_Source.setObjectName("menu_Clear_Source")
        self.menu_Clear_Output = QtWidgets.QAction(MainWindow)
        self.menu_Clear_Output.setEnabled(False)
        self.menu_Clear_Output.setIcon(icon3)
        self.menu_Clear_Output.setObjectName("menu_Clear_Output")
        self.menu_Undo_Output = QtWidgets.QAction(MainWindow)
        self.menu_Undo_Output.setEnabled(False)
        self.menu_Undo_Output.setIcon(icon4)
        self.menu_Undo_Output.setObjectName("menu_Undo_Output")
        self.menu_Redo_Output = QtWidgets.QAction(MainWindow)
        self.menu_Redo_Output.setEnabled(False)
        self.menu_Redo_Output.setIcon(icon5)
        self.menu_Redo_Output.setObjectName("menu_Redo_Output")
        self.menu_RGB_to_Grayscale = QtWidgets.QAction(MainWindow)
        self.menu_RGB_to_Grayscale.setEnabled(False)
        self.menu_RGB_to_Grayscale.setIcon(icon6)
        self.menu_RGB_to_Grayscale.setObjectName("menu_RGB_to_Grayscale")
        self.menu_RGB_to_HSV = QtWidgets.QAction(MainWindow)
        self.menu_RGB_to_HSV.setEnabled(False)
        self.menu_RGB_to_HSV.setIcon(icon7)
        self.menu_RGB_to_HSV.setObjectName("menu_RGB_to_HSV")
        self.menu_Multi_Otsu_Thresholding = QtWidgets.QAction(MainWindow)
        self.menu_Multi_Otsu_Thresholding.setEnabled(False)
        self.menu_Multi_Otsu_Thresholding.setIcon(icon8)
        self.menu_Multi_Otsu_Thresholding.setObjectName("menu_Multi_Otsu_Thresholding")
        self.menu_Chan_Vese_Segmentation = QtWidgets.QAction(MainWindow)
        self.menu_Chan_Vese_Segmentation.setEnabled(False)
        self.menu_Chan_Vese_Segmentation.setIcon(icon9)
        self.menu_Chan_Vese_Segmentation.setObjectName("menu_Chan_Vese_Segmentation")
        self.menu_Morphological_Snakes = QtWidgets.QAction(MainWindow)
        self.menu_Morphological_Snakes.setEnabled(False)
        self.menu_Morphological_Snakes.setIcon(icon10)
        self.menu_Morphological_Snakes.setObjectName("menu_Morphological_Snakes")
        self.menu_Roberts = QtWidgets.QAction(MainWindow)
        self.menu_Roberts.setEnabled(False)
        self.menu_Roberts.setIcon(icon12)
        self.menu_Roberts.setObjectName("menu_Roberts")
        self.menu_Sobel = QtWidgets.QAction(MainWindow)
        self.menu_Sobel.setEnabled(False)
        self.menu_Sobel.setIcon(icon14)
        self.menu_Sobel.setObjectName("menu_Sobel")
        self.menu_Scharr = QtWidgets.QAction(MainWindow)
        self.menu_Scharr.setEnabled(False)
        self.menu_Scharr.setIcon(icon13)
        self.menu_Scharr.setObjectName("menu_Scharr")
        self.menu_Prewitt = QtWidgets.QAction(MainWindow)
        self.menu_Prewitt.setEnabled(False)
        self.menu_Prewitt.setIcon(icon11)
        self.menu_Prewitt.setWhatsThis("")
        self.menu_Prewitt.setObjectName("menu_Prewitt")
        self.menuExport_As.addAction(self.menu_Export_As_Source)
        self.menuExport_As.addAction(self.menu_Export_As_Output)
        self.menuFile.addAction(self.menu_Open_Source)
        self.menuFile.addAction(self.menu_Save_Output)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menu_Save_As_Output)
        self.menuFile.addAction(self.menuExport_As.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menu_Exit)
        self.menuClear.addAction(self.menu_Clear_Source)
        self.menuClear.addAction(self.menu_Clear_Output)
        self.menuEdit.addAction(self.menuClear.menuAction())
        self.menuEdit.addAction(self.menu_Undo_Output)
        self.menuEdit.addAction(self.menu_Redo_Output)
        self.menuConversion.addAction(self.menu_RGB_to_Grayscale)
        self.menuConversion.addAction(self.menu_RGB_to_HSV)
        self.menuSegmentation.addAction(self.menu_Multi_Otsu_Thresholding)
        self.menuSegmentation.addAction(self.menu_Chan_Vese_Segmentation)
        self.menuSegmentation.addAction(self.menu_Morphological_Snakes)
        self.menuEdge_Detection.addAction(self.menu_Roberts)
        self.menuEdge_Detection.addAction(self.menu_Sobel)
        self.menuEdge_Detection.addAction(self.menu_Scharr)
        self.menuEdge_Detection.addAction(self.menu_Prewitt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuConversion.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())
        self.menubar.addAction(self.menuEdge_Detection.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Operator"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_Output.setText(_translate("MainWindow", "Output"))
        self.label_input_image.setStatusTip(_translate("MainWindow", "Save the file on a different location with a name you input"))
        self.label_Input.setText(_translate("MainWindow", "Input"))
        self.groupBox_Functions.setTitle(_translate("MainWindow", "File"))
        self.pushButton_Open_Source.setStatusTip(_translate("MainWindow", "Input the source file"))
        self.groupBox_Edit.setTitle(_translate("MainWindow", "Edit"))
        self.pushButton_Clear_Source.setStatusTip(_translate("MainWindow", "Clear the source"))
        self.pushButton_Clear_Output.setStatusTip(_translate("MainWindow", "Clear the output"))
        self.pushButton_Undo_Output.setStatusTip(_translate("MainWindow", "Undo output"))
        self.pushButton_Redo_Output.setStatusTip(_translate("MainWindow", "Redo output"))
        self.groupBox_Conversion.setTitle(_translate("MainWindow", "Conversion"))
        self.pushButton_RGB_to_Grayscale.setStatusTip(_translate("MainWindow", "Convert RGB source to Grayscale"))
        self.pushButton_RGB_to_HSV.setStatusTip(_translate("MainWindow", "Convert RGB source to HSV"))
        self.groupBox_Segmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.pushButton_Multi_Otsu_Thresholding.setStatusTip(_translate("MainWindow", "Apply Multi-Otsu Thresholding to source"))
        self.pushButton_Chan_Vese_Segmentation.setStatusTip(_translate("MainWindow", "Apply Chan-Vese Segmentation to source"))
        self.pushButton_Morphological_Snakes.setStatusTip(_translate("MainWindow", "Apply Morphological Snakes to source"))
        self.groupBox_Edge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.pushButton_Prewitt.setStatusTip(_translate("MainWindow", "Apply Prewitt edge detection to source"))
        self.pushButton_Roberts.setStatusTip(_translate("MainWindow", "Apply Roberts edge detection to source"))
        self.pushButton_Scharr.setStatusTip(_translate("MainWindow", "Apply Scharr edge detection to source"))
        self.pushButton_Sobel.setStatusTip(_translate("MainWindow", "Apply Sobel edge detection to source"))
        self.pushButton_Save_Output.setStatusTip(_translate("MainWindow", "Save the file with the same name and extension in the same folder"))
        self.pushButton_Save_as_Output.setStatusTip(_translate("MainWindow", "Save the file on a different location with a name you input"))
        self.pushButton_Export_as_Source.setStatusTip(_translate("MainWindow", "Export output"))
        self.pushButton_Export_as_Output.setStatusTip(_translate("MainWindow", "Export the output"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport_As.setStatusTip(_translate("MainWindow", "Export output"))
        self.menuExport_As.setTitle(_translate("MainWindow", "Export As"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuClear.setStatusTip(_translate("MainWindow", "Clear"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuConversion.setTitle(_translate("MainWindow", "Conversion"))
        self.menuSegmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menu_Open_Source.setText(_translate("MainWindow", "Open Source"))
        self.menu_Open_Source.setStatusTip(_translate("MainWindow", "Input the source file"))
        self.menu_Open_Source.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.menu_Save_Output.setText(_translate("MainWindow", "Save Output"))
        self.menu_Save_Output.setStatusTip(_translate("MainWindow", "Save the file with the same name and extension in the same folder"))
        self.menu_Save_Output.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.menu_Save_As_Output.setText(_translate("MainWindow", "Save As Output"))
        self.menu_Save_As_Output.setStatusTip(_translate("MainWindow", "Save the file on a different location with a name you input"))
        self.menu_Save_As_Output.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.menu_Exit.setText(_translate("MainWindow", "Exit"))
        self.menu_Exit.setStatusTip(_translate("MainWindow", "Shut down Image Operator"))
        self.menu_Exit.setShortcut(_translate("MainWindow", "Shift+F4"))
        self.menu_Export_As_Source.setText(_translate("MainWindow", "Source"))
        self.menu_Export_As_Source.setStatusTip(_translate("MainWindow", "Export the source"))
        self.menu_Export_As_Source.setShortcut(_translate("MainWindow", "Alt+S"))
        self.menu_Export_As_Output.setText(_translate("MainWindow", "Output"))
        self.menu_Export_As_Output.setStatusTip(_translate("MainWindow", "Export the output"))
        self.menu_Export_As_Output.setShortcut(_translate("MainWindow", "Alt+O"))
        self.menu_Clear_Source.setText(_translate("MainWindow", "Source"))
        self.menu_Clear_Source.setStatusTip(_translate("MainWindow", "Clear the source"))
        self.menu_Clear_Source.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.menu_Clear_Output.setText(_translate("MainWindow", "Output"))
        self.menu_Clear_Output.setStatusTip(_translate("MainWindow", "Clear the output"))
        self.menu_Clear_Output.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.menu_Undo_Output.setText(_translate("MainWindow", "Undo Output"))
        self.menu_Undo_Output.setStatusTip(_translate("MainWindow", "Undo output"))
        self.menu_Undo_Output.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.menu_Redo_Output.setText(_translate("MainWindow", "Redo Output"))
        self.menu_Redo_Output.setStatusTip(_translate("MainWindow", "Redo output"))
        self.menu_Redo_Output.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.menu_RGB_to_Grayscale.setText(_translate("MainWindow", "RGB to Grayscale"))
        self.menu_RGB_to_Grayscale.setStatusTip(_translate("MainWindow", "Convert RGB source to Grayscale"))
        self.menu_RGB_to_Grayscale.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.menu_RGB_to_HSV.setText(_translate("MainWindow", "RGB to HSV"))
        self.menu_RGB_to_HSV.setStatusTip(_translate("MainWindow", "Convert RGB source to HSV"))
        self.menu_RGB_to_HSV.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.menu_Multi_Otsu_Thresholding.setText(_translate("MainWindow", "Multi-Otsu Thresholding"))
        self.menu_Multi_Otsu_Thresholding.setStatusTip(_translate("MainWindow", "Apply Multi-Otsu Thresholding to source"))
        self.menu_Multi_Otsu_Thresholding.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.menu_Chan_Vese_Segmentation.setText(_translate("MainWindow", "Chan-Vese Segmentation"))
        self.menu_Chan_Vese_Segmentation.setStatusTip(_translate("MainWindow", "Apply Chan-Vese Segmentation to source"))
        self.menu_Chan_Vese_Segmentation.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.menu_Morphological_Snakes.setText(_translate("MainWindow", "Morphological Snakes"))
        self.menu_Morphological_Snakes.setStatusTip(_translate("MainWindow", "Apply Morphological Snakes to source"))
        self.menu_Morphological_Snakes.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.menu_Roberts.setText(_translate("MainWindow", "Roberts"))
        self.menu_Roberts.setStatusTip(_translate("MainWindow", "Apply Roberts edge detection to source"))
        self.menu_Roberts.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.menu_Sobel.setText(_translate("MainWindow", "Sobel"))
        self.menu_Sobel.setStatusTip(_translate("MainWindow", "Apply Sobel edge detection to source"))
        self.menu_Sobel.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.menu_Scharr.setText(_translate("MainWindow", "Scharr"))
        self.menu_Scharr.setStatusTip(_translate("MainWindow", "Apply Scharr edge detection to source"))
        self.menu_Scharr.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.menu_Prewitt.setText(_translate("MainWindow", "Prewitt"))
        self.menu_Prewitt.setIconText(_translate("MainWindow", "Prewitt"))
        self.menu_Prewitt.setToolTip(_translate("MainWindow", "Prewitt"))
        self.menu_Prewitt.setStatusTip(_translate("MainWindow", "Apply Prewitt edge detection to source"))
        self.menu_Prewitt.setShortcut(_translate("MainWindow", "Ctrl+P"))
