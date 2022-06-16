"""@package docstring
    Backhand module for connections and functions of UI.
"""

from PyQt5 import QtWidgets, QtGui, QtCore # for working with UI
from PyQt5.QtWidgets import QFileDialog # for file functions
from proposal_UI import Ui_MainWindow # in the same directory, import Ui_MainWindow class in the file and module Image_Operator

from PIL import ImageQt # for saving the output.
from Plot import Plot # for plotting data

import os #for paths of files

class Operate(QtWidgets.QMainWindow):
    """
    This class conducts necessary operations to handle data clustering and ui connections.
    """
    def __init__(self):
        """The constructor"""
        super(Operate,self).__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        self.file_path = None
        self.f = None

        #set signal connections
        self.ui.actionOpen_Data.triggered.connect(self.open_data)
        self.ui.actionSave_Initial_Solution.triggered.connect(self.save_initial_solution)
        self.ui.actionInitial_Clear_Initial_Solution.triggered.connect(self.clear_initial_solution)
        self.ui.actionInitial_Solution.triggered.connect(self.export_as_init_sol)
        self.ui.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit)


        self.ui.pushButton_Open_Data.clicked.connect(self.open_data)
        self.ui.pushButton_Save_Initial_Solution.clicked.connect(self.save_initial_solution) 
        self.ui.pushButton_Clear_Initial_Solution.clicked.connect(self.clear_initial_solution) 


    def open_data(self):
        """Opens data from a chosen location and shows it at initial data place of the UI """
        p = Plot() # for plotting the input data at the UI
        self.file_path, filter_type = QFileDialog.getOpenFileName(self, 'Open Source','D:',"Text File (*.txt)") #get file path
        
        if self.file_path:
            with open(self.file_path, "r") as self.f:
                p.plot_Scatter(self.f) #shows data as a scatter plot
                self.ui.label_Path.setText("Path: " + self.file_path) # shows the file path at the UI at the top of the initial data
               
        
        self.ui.label_data_image.setPixmap(QtGui.QPixmap(os.getcwd() + "\\input_data.png")) #filename comes as a tuple so we use the 0th indice for directory string
        self.enable_some_widgets_after_input() #enabla some widgets after data is opened

    def save_initial_solution(self):
        """Saves initial solution to a text file"""
        with   open(self.file_path, "r") as self.f:
            file_contents = self.f.read() # get contents

        new_file_path = QFileDialog.getSaveFileName(self, "Save this file as txt", "", "Text Files (*.txt)") # get the save location
        file_path = new_file_path[0]

        with  open(file_path, "w+") as f: # write the data to file
            f.write(file_contents)

            
    def export_as_init_sol(self):
        """Exports initial data as .jpg"""
        image = ImageQt.fromqpixmap(self.ui.label_data_image.pixmap()) #export image
        image.save('SAVED.jpg') # save is at .jpg at the workspace location
        
    def clear_initial_solution(self):
        """Clears initial data from UI"""
        self.ui.label_data_image.setPixmap(QtGui.QPixmap()) # clear initial solution
        self.disable_some_widgets_if_no_input() # disable some widgets since there is no input no more

    def enable_some_widgets_after_input(self):
        """Enables some widgets existing in the UI if an input data is present in the input"""
        self.ui.actionOpen_Data.setEnabled(True)
        self.ui.actionSave_Initial_Solution.setEnabled(True)
        self.ui.menuExport_As.setEnabled(True)
        self.ui.actionInitial_Solution.setEnabled(True)
        self.ui.menuClear.setEnabled(True)
        self.ui.actionInitial_Clear_Initial_Solution.setEnabled(True)
        self.ui.menuUndo.setEnabled(True)
        self.ui.actionUndo_Initial_Solution.setEnabled(True)
        self.ui.menuRedo.setEnabled(True)
        self.ui.actionRedo_Initial_Solution.setEnabled(True)
        self.ui.action_K_Means.setEnabled(True)
        self.ui.action_Affinity_Propagation.setEnabled(True)
        self.ui.action_Mean_shift.setEnabled(True)
        self.ui.action_Spectral_Clustering.setEnabled(True)
        self.ui.action_Hierarchical_Clustering.setEnabled(True)
        self.ui.action_DBSCAN.setEnabled(True)
        self.ui.actionHill_Climbing.setEnabled(True)
        self.ui.actionSimulated_Anneling.setEnabled(True)
        ##
        self.ui.pushButton_Save_Initial_Solution.setEnabled(True)
        self.ui.pushButton_Clear_Initial_Solution.setEnabled(True)
        self.ui.pushButton_K_Means.setEnabled(True)
        self.ui.pushButton_Affinity_Propagation.setEnabled(True)
        self.ui.pushButton_Mean_Shift.setEnabled(True)
        self.ui.pushButton_Spectral_Clustering.setEnabled(True)
        self.ui.pushButton_Hierarchical_Clustering.setEnabled(True)
        self.ui.pushButton_DBSCAN.setEnabled(True)
        self.ui.pushButton_Hill_Climbing.setEnabled(True)
        self.ui.pushButton_Simulated_Anneling.setEnabled(True)
        
        
      
    def disable_some_widgets_if_no_input(self):
        """Disables some widgets existing in the UI if an input data is NOT present in the input"""
        self.ui.actionSave_Initial_Solution.setEnabled(False)
        self.ui.menuExport_As.setEnabled(False)
        self.ui.actionInitial_Solution.setEnabled(False)
        self.ui.menuClear.setEnabled(False)
        self.ui.actionInitial_Clear_Initial_Solution.setEnabled(False)
        self.ui.menuUndo.setEnabled(False)
        self.ui.actionUndo_Initial_Solution.setEnabled(False)
        self.ui.menuRedo.setEnabled(False)
        self.ui.actionRedo_Initial_Solution.setEnabled(False)
        self.ui.action_K_Means.setEnabled(False)
        self.ui.action_Affinity_Propagation.setEnabled(False)
        self.ui.action_Mean_shift.setEnabled(False)
        self.ui.action_Spectral_Clustering.setEnabled(False)
        self.ui.action_Hierarchical_Clustering.setEnabled(False)
        self.ui.action_DBSCAN.setEnabled(False)
        self.ui.actionHill_Climbing.setEnabled(False)
        self.ui.actionSimulated_Anneling.setEnabled(False)
        ##
        self.ui.pushButton_Save_Initial_Solution.setEnabled(False)
        self.ui.pushButton_Clear_Initial_Solution.setEnabled(False)
        self.ui.pushButton_K_Means.setEnabled(False)
        self.ui.pushButton_Affinity_Propagation.setEnabled(False)
        self.ui.pushButton_Mean_Shift.setEnabled(False)
        self.ui.pushButton_Spectral_Clustering.setEnabled(False)
        self.ui.pushButton_Hierarchical_Clustering.setEnabled(False)
        self.ui.pushButton_DBSCAN.setEnabled(False)
        self.ui.pushButton_Hill_Climbing.setEnabled(False)
        self.ui.pushButton_Simulated_Anneling.setEnabled(False)


