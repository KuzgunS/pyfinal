"""@package docstring
Auto-generated UI module
Handles UI 
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proposal.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1346, 859)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_Functions = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Functions.setGeometry(QtCore.QRect(690, 0, 91, 801))
        self.groupBox_Functions.setObjectName("groupBox_Functions")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_Functions)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 79, 781))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_Functions = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_Functions.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Functions.setObjectName("verticalLayout_Functions")
        self.groupBox_File = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_File.setObjectName("groupBox_File")
        self.pushButton_Open_Data = QtWidgets.QPushButton(self.groupBox_File)
        self.pushButton_Open_Data.setGeometry(QtCore.QRect(10, 20, 51, 28))
        self.pushButton_Open_Data.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/Open Source.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Open_Data.setIcon(icon1)
        self.pushButton_Open_Data.setObjectName("pushButton_Open_Data")
        self.pushButton_Save_Initial_Solution = QtWidgets.QPushButton(self.groupBox_File)
        self.pushButton_Save_Initial_Solution.setEnabled(False)
        self.pushButton_Save_Initial_Solution.setGeometry(QtCore.QRect(10, 50, 51, 28))
        self.pushButton_Save_Initial_Solution.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/Save Output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Save_Initial_Solution.setIcon(icon2)
        self.pushButton_Save_Initial_Solution.setObjectName("pushButton_Save_Initial_Solution")
        self.pushButton_Save_Final_Solution = QtWidgets.QPushButton(self.groupBox_File)
        self.pushButton_Save_Final_Solution.setEnabled(False)
        self.pushButton_Save_Final_Solution.setGeometry(QtCore.QRect(10, 80, 51, 28))
        self.pushButton_Save_Final_Solution.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/Save Output - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Save_Final_Solution.setIcon(icon3)
        self.pushButton_Save_Final_Solution.setObjectName("pushButton_Save_Final_Solution")
        self.verticalLayout_Functions.addWidget(self.groupBox_File)
        self.groupBox_Edit = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_Edit.setObjectName("groupBox_Edit")
        self.pushButton_Clear_Final_Solution = QtWidgets.QPushButton(self.groupBox_Edit)
        self.pushButton_Clear_Final_Solution.setEnabled(False)
        self.pushButton_Clear_Final_Solution.setGeometry(QtCore.QRect(10, 50, 51, 28))
        self.pushButton_Clear_Final_Solution.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/clear output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Clear_Final_Solution.setIcon(icon4)
        self.pushButton_Clear_Final_Solution.setObjectName("pushButton_Clear_Final_Solution")
        self.pushButton_Clear_Initial_Solution = QtWidgets.QPushButton(self.groupBox_Edit)
        self.pushButton_Clear_Initial_Solution.setEnabled(False)
        self.pushButton_Clear_Initial_Solution.setGeometry(QtCore.QRect(10, 20, 51, 28))
        self.pushButton_Clear_Initial_Solution.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/clear source.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Clear_Initial_Solution.setIcon(icon5)
        self.pushButton_Clear_Initial_Solution.setObjectName("pushButton_Clear_Initial_Solution")
        self.verticalLayout_Functions.addWidget(self.groupBox_Edit)
        self.groupBox_Clustering = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Clustering.sizePolicy().hasHeightForWidth())
        self.groupBox_Clustering.setSizePolicy(sizePolicy)
        self.groupBox_Clustering.setMinimumSize(QtCore.QSize(0, 250))
        self.groupBox_Clustering.setObjectName("groupBox_Clustering")
        self.pushButton_K_Means = QtWidgets.QPushButton(self.groupBox_Clustering)
        self.pushButton_K_Means.setEnabled(False)
        self.pushButton_K_Means.setGeometry(QtCore.QRect(10, 20, 51, 28))
        self.pushButton_K_Means.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/K means,.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_K_Means.setIcon(icon6)
        self.pushButton_K_Means.setObjectName("pushButton_K_Means")
        self.pushButton_Affinity_Propagation = QtWidgets.QPushButton(self.groupBox_Clustering)
        self.pushButton_Affinity_Propagation.setEnabled(False)
        self.pushButton_Affinity_Propagation.setGeometry(QtCore.QRect(10, 50, 51, 28))
        self.pushButton_Affinity_Propagation.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/Affinity.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Affinity_Propagation.setIcon(icon7)
        self.pushButton_Affinity_Propagation.setObjectName("pushButton_Affinity_Propagation")
        self.pushButton_Mean_Shift = QtWidgets.QPushButton(self.groupBox_Clustering)
        self.pushButton_Mean_Shift.setEnabled(False)
        self.pushButton_Mean_Shift.setGeometry(QtCore.QRect(10, 80, 51, 28))
        self.pushButton_Mean_Shift.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/Mean shift.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Mean_Shift.setIcon(icon8)
        self.pushButton_Mean_Shift.setObjectName("pushButton_Mean_Shift")
        self.pushButton_Spectral_Clustering = QtWidgets.QPushButton(self.groupBox_Clustering)
        self.pushButton_Spectral_Clustering.setEnabled(False)
        self.pushButton_Spectral_Clustering.setGeometry(QtCore.QRect(10, 110, 51, 28))
        self.pushButton_Spectral_Clustering.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/Spectral.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Spectral_Clustering.setIcon(icon9)
        self.pushButton_Spectral_Clustering.setObjectName("pushButton_Spectral_Clustering")
        self.pushButton_Hierarchical_Clustering = QtWidgets.QPushButton(self.groupBox_Clustering)
        self.pushButton_Hierarchical_Clustering.setEnabled(False)
        self.pushButton_Hierarchical_Clustering.setGeometry(QtCore.QRect(10, 140, 51, 28))
        self.pushButton_Hierarchical_Clustering.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/Hier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Hierarchical_Clustering.setIcon(icon10)
        self.pushButton_Hierarchical_Clustering.setObjectName("pushButton_Hierarchical_Clustering")
        self.pushButton_DBSCAN = QtWidgets.QPushButton(self.groupBox_Clustering)
        self.pushButton_DBSCAN.setEnabled(False)
        self.pushButton_DBSCAN.setGeometry(QtCore.QRect(10, 170, 51, 28))
        self.pushButton_DBSCAN.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/DBSCAN.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_DBSCAN.setIcon(icon11)
        self.pushButton_DBSCAN.setObjectName("pushButton_DBSCAN")
        self.verticalLayout_Functions.addWidget(self.groupBox_Clustering)
        self.groupBox_Heuristic = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_Heuristic.setObjectName("groupBox_Heuristic")
        self.pushButton_Hill_Climbing = QtWidgets.QPushButton(self.groupBox_Heuristic)
        self.pushButton_Hill_Climbing.setEnabled(False)
        self.pushButton_Hill_Climbing.setGeometry(QtCore.QRect(10, 20, 51, 28))
        self.pushButton_Hill_Climbing.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/Hill Climb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Hill_Climbing.setIcon(icon12)
        self.pushButton_Hill_Climbing.setObjectName("pushButton_Hill_Climbing")
        self.pushButton_Simulated_Anneling = QtWidgets.QPushButton(self.groupBox_Heuristic)
        self.pushButton_Simulated_Anneling.setEnabled(False)
        self.pushButton_Simulated_Anneling.setGeometry(QtCore.QRect(10, 50, 51, 28))
        self.pushButton_Simulated_Anneling.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/Simulated Annealing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Simulated_Anneling.setIcon(icon13)
        self.pushButton_Simulated_Anneling.setObjectName("pushButton_Simulated_Anneling")
        self.verticalLayout_Functions.addWidget(self.groupBox_Heuristic)
        self.groupBox_Initial_Solution = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Initial_Solution.setGeometry(QtCore.QRect(0, 10, 681, 701))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Initial_Solution.setFont(font)
        self.groupBox_Initial_Solution.setObjectName("groupBox_Initial_Solution")
        self.label_Initial_Solution = QtWidgets.QLabel(self.groupBox_Initial_Solution)
        self.label_Initial_Solution.setGeometry(QtCore.QRect(10, 30, 501, 401))
        self.label_Initial_Solution.setText("")
        self.label_Initial_Solution.setObjectName("label_Initial_Solution")
        self.label_Path = QtWidgets.QLabel(self.groupBox_Initial_Solution)
        self.label_Path.setGeometry(QtCore.QRect(10, 30, 501, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_Path.setFont(font)
        self.label_Path.setObjectName("label_Path")
        self.label_data_image = QtWidgets.QLabel(self.groupBox_Initial_Solution)
        self.label_data_image.setGeometry(QtCore.QRect(30, 60, 631, 621))
        self.label_data_image.setText("")
        self.label_data_image.setObjectName("label_data_image")
        self.groupBox_Final_Solution = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Final_Solution.setGeometry(QtCore.QRect(790, 10, 521, 431))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Final_Solution.setFont(font)
        self.groupBox_Final_Solution.setObjectName("groupBox_Final_Solution")
        self.groupBox_Info_Panel = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Info_Panel.setGeometry(QtCore.QRect(10, 710, 671, 91))
        self.groupBox_Info_Panel.setObjectName("groupBox_Info_Panel")
        self.lineEdit_Info_Panel = QtWidgets.QLineEdit(self.groupBox_Info_Panel)
        self.lineEdit_Info_Panel.setGeometry(QtCore.QRect(10, 20, 651, 61))
        self.lineEdit_Info_Panel.setText("")
        self.lineEdit_Info_Panel.setObjectName("lineEdit_Info_Panel")
        self.groupBox_Manual_Solution = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Manual_Solution.setGeometry(QtCore.QRect(800, 470, 511, 321))
        self.groupBox_Manual_Solution.setObjectName("groupBox_Manual_Solution")
        self.lineEdit_Hubs = QtWidgets.QLineEdit(self.groupBox_Manual_Solution)
        self.lineEdit_Hubs.setGeometry(QtCore.QRect(10, 50, 231, 111))
        self.lineEdit_Hubs.setObjectName("lineEdit_Hubs")
        self.label_Hubs = QtWidgets.QLabel(self.groupBox_Manual_Solution)
        self.label_Hubs.setGeometry(QtCore.QRect(10, 30, 55, 16))
        self.label_Hubs.setObjectName("label_Hubs")
        self.label_Nodes = QtWidgets.QLabel(self.groupBox_Manual_Solution)
        self.label_Nodes.setGeometry(QtCore.QRect(10, 170, 55, 16))
        self.label_Nodes.setObjectName("label_Nodes")
        self.lineEdit_Nodes = QtWidgets.QLineEdit(self.groupBox_Manual_Solution)
        self.lineEdit_Nodes.setGeometry(QtCore.QRect(10, 190, 231, 111))
        self.lineEdit_Nodes.setText("")
        self.lineEdit_Nodes.setObjectName("lineEdit_Nodes")
        self.groupBox_Results = QtWidgets.QGroupBox(self.groupBox_Manual_Solution)
        self.groupBox_Results.setGeometry(QtCore.QRect(260, 30, 241, 271))
        self.groupBox_Results.setObjectName("groupBox_Results")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1346, 26))
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
        self.menuUndo = QtWidgets.QMenu(self.menuEdit)
        self.menuUndo.setEnabled(False)
        self.menuUndo.setObjectName("menuUndo")
        self.menuRedo = QtWidgets.QMenu(self.menuEdit)
        self.menuRedo.setEnabled(False)
        self.menuRedo.setObjectName("menuRedo")
        self.menuClustering = QtWidgets.QMenu(self.menubar)
        self.menuClustering.setObjectName("menuClustering")
        self.menuHeuristics = QtWidgets.QMenu(self.menubar)
        self.menuHeuristics.setObjectName("menuHeuristics")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Data = QtWidgets.QAction(MainWindow)
        self.actionOpen_Data.setIcon(icon1)
        self.actionOpen_Data.setStatusTip("Get some data into the program")
        self.actionOpen_Data.setObjectName("actionOpen_Data")
        self.actionSave_Initial_Solution = QtWidgets.QAction(MainWindow)
        self.actionSave_Initial_Solution.setEnabled(False)
        self.actionSave_Initial_Solution.setIcon(icon2)
        self.actionSave_Initial_Solution.setObjectName("actionSave_Initial_Solution")
        self.actionSave_Final_Solution = QtWidgets.QAction(MainWindow)
        self.actionSave_Final_Solution.setEnabled(False)
        self.actionSave_Final_Solution.setIcon(icon3)
        self.actionSave_Final_Solution.setObjectName("actionSave_Final_Solution")
        self.actionInitial_Solution = QtWidgets.QAction(MainWindow)
        self.actionInitial_Solution.setEnabled(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/Export As_ Output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInitial_Solution.setIcon(icon14)
        self.actionInitial_Solution.setObjectName("actionInitial_Solution")
        self.actionFinal_Solution = QtWidgets.QAction(MainWindow)
        self.actionFinal_Solution.setEnabled(False)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/Export As_ Output - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFinal_Solution.setIcon(icon15)
        self.actionFinal_Solution.setObjectName("actionFinal_Solution")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/exit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon16)
        self.actionExit.setObjectName("actionExit")
        self.actionInitial_Clear_Initial_Solution = QtWidgets.QAction(MainWindow)
        self.actionInitial_Clear_Initial_Solution.setIcon(icon5)
        self.actionInitial_Clear_Initial_Solution.setObjectName("actionInitial_Clear_Initial_Solution")
        self.actionInitial_Clear_Final_Solution = QtWidgets.QAction(MainWindow)
        self.actionInitial_Clear_Final_Solution.setEnabled(False)
        self.actionInitial_Clear_Final_Solution.setIcon(icon4)
        self.actionInitial_Clear_Final_Solution.setObjectName("actionInitial_Clear_Final_Solution")
        self.actionUndo_Initial_Solution = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icons/undo output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo_Initial_Solution.setIcon(icon17)
        self.actionUndo_Initial_Solution.setObjectName("actionUndo_Initial_Solution")
        self.actionUndo_Final_Solution = QtWidgets.QAction(MainWindow)
        self.actionUndo_Final_Solution.setEnabled(False)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icons/undo output - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo_Final_Solution.setIcon(icon18)
        self.actionUndo_Final_Solution.setObjectName("actionUndo_Final_Solution")
        self.actionRedo_Initial_Solution = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icons/redo output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo_Initial_Solution.setIcon(icon19)
        self.actionRedo_Initial_Solution.setObjectName("actionRedo_Initial_Solution")
        self.actionRedo_Final_Solution = QtWidgets.QAction(MainWindow)
        self.actionRedo_Final_Solution.setEnabled(False)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("icons/redo output - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo_Final_Solution.setIcon(icon20)
        self.actionRedo_Final_Solution.setObjectName("actionRedo_Final_Solution")
        self.action_K_Means = QtWidgets.QAction(MainWindow)
        self.action_K_Means.setEnabled(False)
        self.action_K_Means.setIcon(icon6)
        self.action_K_Means.setObjectName("action_K_Means")
        self.action_Affinity_Propagation = QtWidgets.QAction(MainWindow)
        self.action_Affinity_Propagation.setEnabled(False)
        self.action_Affinity_Propagation.setIcon(icon7)
        self.action_Affinity_Propagation.setObjectName("action_Affinity_Propagation")
        self.action_Mean_shift = QtWidgets.QAction(MainWindow)
        self.action_Mean_shift.setEnabled(False)
        self.action_Mean_shift.setIcon(icon8)
        self.action_Mean_shift.setObjectName("action_Mean_shift")
        self.action_Spectral_Clustering = QtWidgets.QAction(MainWindow)
        self.action_Spectral_Clustering.setEnabled(False)
        self.action_Spectral_Clustering.setIcon(icon9)
        self.action_Spectral_Clustering.setObjectName("action_Spectral_Clustering")
        self.action_Hierarchical_Clustering = QtWidgets.QAction(MainWindow)
        self.action_Hierarchical_Clustering.setEnabled(False)
        self.action_Hierarchical_Clustering.setIcon(icon10)
        self.action_Hierarchical_Clustering.setObjectName("action_Hierarchical_Clustering")
        self.action_DBSCAN = QtWidgets.QAction(MainWindow)
        self.action_DBSCAN.setEnabled(False)
        self.action_DBSCAN.setIcon(icon11)
        self.action_DBSCAN.setObjectName("action_DBSCAN")
        self.actionHill_Climbing = QtWidgets.QAction(MainWindow)
        self.actionHill_Climbing.setEnabled(False)
        self.actionHill_Climbing.setIcon(icon12)
        self.actionHill_Climbing.setObjectName("actionHill_Climbing")
        self.actionSimulated_Anneling = QtWidgets.QAction(MainWindow)
        self.actionSimulated_Anneling.setEnabled(False)
        self.actionSimulated_Anneling.setIcon(icon13)
        self.actionSimulated_Anneling.setObjectName("actionSimulated_Anneling")
        self.menuExport_As.addAction(self.actionInitial_Solution)
        self.menuExport_As.addAction(self.actionFinal_Solution)
        self.menuFile.addAction(self.actionOpen_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Initial_Solution)
        self.menuFile.addAction(self.actionSave_Final_Solution)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExport_As.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuClear.addAction(self.actionInitial_Clear_Initial_Solution)
        self.menuClear.addAction(self.actionInitial_Clear_Final_Solution)
        self.menuUndo.addAction(self.actionUndo_Initial_Solution)
        self.menuUndo.addAction(self.actionUndo_Final_Solution)
        self.menuRedo.addAction(self.actionRedo_Initial_Solution)
        self.menuRedo.addAction(self.actionRedo_Final_Solution)
        self.menuEdit.addAction(self.menuClear.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuUndo.menuAction())
        self.menuEdit.addAction(self.menuRedo.menuAction())
        self.menuClustering.addAction(self.action_K_Means)
        self.menuClustering.addAction(self.action_Affinity_Propagation)
        self.menuClustering.addAction(self.action_Mean_shift)
        self.menuClustering.addAction(self.action_Spectral_Clustering)
        self.menuClustering.addAction(self.action_Hierarchical_Clustering)
        self.menuClustering.addAction(self.action_DBSCAN)
        self.menuHeuristics.addAction(self.actionHill_Climbing)
        self.menuHeuristics.addAction(self.actionSimulated_Anneling)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuClustering.menuAction())
        self.menubar.addAction(self.menuHeuristics.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Clusterer"))
        MainWindow.setStatusTip(_translate("MainWindow", "Cluster those data!"))
        self.groupBox_Functions.setTitle(_translate("MainWindow", "Functions"))
        self.groupBox_File.setTitle(_translate("MainWindow", "File"))
        self.pushButton_Open_Data.setStatusTip(_translate("MainWindow", "Get some data into the program"))
        self.pushButton_Save_Initial_Solution.setStatusTip(_translate("MainWindow", "Save Initial Solution"))
        self.pushButton_Save_Final_Solution.setStatusTip(_translate("MainWindow", "Save Final Solution"))
        self.groupBox_Edit.setTitle(_translate("MainWindow", "Edit"))
        self.pushButton_Clear_Final_Solution.setStatusTip(_translate("MainWindow", "Clear Final Solution"))
        self.pushButton_Clear_Initial_Solution.setStatusTip(_translate("MainWindow", "Clear Initial Solution"))
        self.groupBox_Clustering.setTitle(_translate("MainWindow", "Clustering"))
        self.pushButton_K_Means.setStatusTip(_translate("MainWindow", "Apply K-Means Clustering"))
        self.pushButton_Affinity_Propagation.setStatusTip(_translate("MainWindow", "Apply Affinity Propagation Clustering"))
        self.pushButton_Mean_Shift.setStatusTip(_translate("MainWindow", "Apply Mean-shift Clustering"))
        self.pushButton_Spectral_Clustering.setStatusTip(_translate("MainWindow", "Apply Spectral Clustering"))
        self.pushButton_Hierarchical_Clustering.setStatusTip(_translate("MainWindow", "Apply Hierarchical Clustering"))
        self.pushButton_DBSCAN.setStatusTip(_translate("MainWindow", "Apply DBSCAN"))
        self.groupBox_Heuristic.setTitle(_translate("MainWindow", "Heuristics"))
        self.pushButton_Hill_Climbing.setStatusTip(_translate("MainWindow", "Apply Hill Climb Heuristics"))
        self.pushButton_Simulated_Anneling.setStatusTip(_translate("MainWindow", "Apply Simulated Anneling Optimization"))
        self.groupBox_Initial_Solution.setTitle(_translate("MainWindow", "Initial Solution"))
        self.label_Path.setText(_translate("MainWindow", "Path:"))
        self.groupBox_Final_Solution.setTitle(_translate("MainWindow", "Final Solution"))
        self.groupBox_Info_Panel.setTitle(_translate("MainWindow", "Info Panel"))
        self.groupBox_Manual_Solution.setTitle(_translate("MainWindow", "Manual Solution"))
        self.label_Hubs.setText(_translate("MainWindow", "Hubs"))
        self.label_Nodes.setText(_translate("MainWindow", "Nodes"))
        self.groupBox_Results.setTitle(_translate("MainWindow", "Results"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport_As.setTitle(_translate("MainWindow", "Export As"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuUndo.setTitle(_translate("MainWindow", "Undo"))
        self.menuRedo.setTitle(_translate("MainWindow", "Redo"))
        self.menuClustering.setTitle(_translate("MainWindow", "Clustering"))
        self.menuHeuristics.setTitle(_translate("MainWindow", "Heuristics"))
        self.actionOpen_Data.setText(_translate("MainWindow", "Open Data"))
        self.actionOpen_Data.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Initial_Solution.setText(_translate("MainWindow", "Save Initial Solution"))
        self.actionSave_Initial_Solution.setStatusTip(_translate("MainWindow", "Save Initial Solution"))
        self.actionSave_Initial_Solution.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_Final_Solution.setText(_translate("MainWindow", "Save Final Solution"))
        self.actionSave_Final_Solution.setStatusTip(_translate("MainWindow", "Save Final Solution"))
        self.actionSave_Final_Solution.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionInitial_Solution.setText(_translate("MainWindow", "Initial Solution"))
        self.actionInitial_Solution.setStatusTip(_translate("MainWindow", "Export as Initial Solution"))
        self.actionInitial_Solution.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionFinal_Solution.setText(_translate("MainWindow", "Final Solution"))
        self.actionFinal_Solution.setStatusTip(_translate("MainWindow", "Export as Final Solution"))
        self.actionFinal_Solution.setShortcut(_translate("MainWindow", "Alt+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Shut down the program"))
        self.actionInitial_Clear_Initial_Solution.setText(_translate("MainWindow", "Initial Solution"))
        self.actionInitial_Clear_Initial_Solution.setStatusTip(_translate("MainWindow", "Clear Initial Solution"))
        self.actionInitial_Clear_Initial_Solution.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionInitial_Clear_Final_Solution.setText(_translate("MainWindow", "Final Solution"))
        self.actionInitial_Clear_Final_Solution.setStatusTip(_translate("MainWindow", "Clear Final Solution"))
        self.actionInitial_Clear_Final_Solution.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.actionUndo_Initial_Solution.setText(_translate("MainWindow", "Undo Initial Solution"))
        self.actionUndo_Initial_Solution.setStatusTip(_translate("MainWindow", "Undo Initial Solution"))
        self.actionUndo_Initial_Solution.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionUndo_Final_Solution.setText(_translate("MainWindow", "Undo Final Solution"))
        self.actionUndo_Final_Solution.setStatusTip(_translate("MainWindow", "Undo Final Solution"))
        self.actionUndo_Final_Solution.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionRedo_Initial_Solution.setText(_translate("MainWindow", "Redo Initial Solution"))
        self.actionRedo_Initial_Solution.setStatusTip(_translate("MainWindow", "Redo Initial Solution"))
        self.actionRedo_Initial_Solution.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionRedo_Final_Solution.setText(_translate("MainWindow", "Redo Final Solution"))
        self.actionRedo_Final_Solution.setStatusTip(_translate("MainWindow", "Redo Final Solution"))
        self.actionRedo_Final_Solution.setShortcut(_translate("MainWindow", "Ctrl+Shift+Y"))
        self.action_K_Means.setText(_translate("MainWindow", "K-Means"))
        self.action_K_Means.setStatusTip(_translate("MainWindow", "Apply K-Means Clustering"))
        self.action_K_Means.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.action_Affinity_Propagation.setText(_translate("MainWindow", "Affinity Propagation"))
        self.action_Affinity_Propagation.setStatusTip(_translate("MainWindow", "Apply Affinity Propagation Clustering"))
        self.action_Affinity_Propagation.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.action_Mean_shift.setText(_translate("MainWindow", "Mean-shift"))
        self.action_Mean_shift.setToolTip(_translate("MainWindow", "Mean-shift"))
        self.action_Mean_shift.setStatusTip(_translate("MainWindow", "Apply Mean-shift Clustering"))
        self.action_Mean_shift.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.action_Spectral_Clustering.setText(_translate("MainWindow", "Spectral Clustering"))
        self.action_Spectral_Clustering.setStatusTip(_translate("MainWindow", "Apply Spectral Clustering"))
        self.action_Spectral_Clustering.setShortcut(_translate("MainWindow", "Ctrl+4"))
        self.action_Hierarchical_Clustering.setText(_translate("MainWindow", "Hierarchical Clustering"))
        self.action_Hierarchical_Clustering.setStatusTip(_translate("MainWindow", "Apply Hierarchical Clustering"))
        self.action_Hierarchical_Clustering.setShortcut(_translate("MainWindow", "Ctrl+5"))
        self.action_DBSCAN.setText(_translate("MainWindow", "DBSCAN"))
        self.action_DBSCAN.setStatusTip(_translate("MainWindow", "Apply DBSCAN"))
        self.action_DBSCAN.setShortcut(_translate("MainWindow", "Ctrl+6"))
        self.actionHill_Climbing.setText(_translate("MainWindow", "Hill Climbing"))
        self.actionHill_Climbing.setStatusTip(_translate("MainWindow", "Apply Hill Climb Heuristics"))
        self.actionHill_Climbing.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionSimulated_Anneling.setText(_translate("MainWindow", "Simulated Anneling"))
        self.actionSimulated_Anneling.setStatusTip(_translate("MainWindow", "Apply Simulated Anneling Optimization"))
        self.actionSimulated_Anneling.setShortcut(_translate("MainWindow", "Ctrl+J"))
