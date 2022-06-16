"""
    Backhand module for connections and functions of UI.
"""

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from proposal_UI import Ui_MainWindow # in the same directory, import Ui_MainWindow class in the file and module Image_Operator

from skimage import io # for image processing input/output operations

from PIL import ImageQt # for saving the output.
from Plot import Plot # for plotting data


class Operate(QtWidgets.QMainWindow):
    """
    This class has necessary operations to make connections to the UI
    """
    def __init__(self):
        """The constructor"""
        super(Operate,self).__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        self.file_path = None

        self.ui.actionOpen_Data.triggered.connect(self.open_source)


        self.ui.pushButton_Open_Data.clicked.connect(self.open_source)

        """
        self.ui.menu_Exit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        
        self.ui.menu_Clear_Source.triggered.connect(self.clearSource)
        self.ui.menu_Clear_Output.triggered.connect(self.clearOutput)
        self.ui.menu_Save_Output.triggered.connect(self.file_save)
        
        self.ui.pushButton_Open_Source.clicked.connect(self.open_source)
        
        self.ui.pushButton_Clear_Source.clicked.connect(self.clearSource)
        self.ui.pushButton_Clear_Output.clicked.connect(self.clearOutput)
        """

    def open_source(self):
        self.file_path, filter_type = QFileDialog.getOpenFileName(self, 'Open Source','D:',"Text File (*.txt)")
               
        if self.file_path:
            with open(self.file_path, "r") as f:
                file_contents = f.read()
                self.ui.label_Path.setText("Path" + self.file_path)
                self.ui.textEdit_text_Area.setText(file_contents)
        #else:
         #   self.ui.invalid_path_alert_message()
        
        

    def clearSource(self):
        """Clears source image from UI"""
        self.ui.label_input_image.setPixmap(QtGui.QPixmap())
        self.disable_some_widgets_before_input()
        self.clearOutput() # clearSource is also needs to clear output as given in the specification

    def clearOutput(self):
        """Clears output image from UI"""
        self.ui.label_output_image.setPixmap(QtGui.QPixmap())
        self.disable_output_related_widgets()
    
    def file_save(self):
        image = ImageQt.fromqpixmap(self.ui.label_output_image.pixmap())
        image.save('SAVED.png')


    def enable_some_widgets_after_input(self):
    
        """Enables some widgets existing in the UI if a source image is present in the input"""
        self.ui.menu_Open_Source.setEnabled(True)
        
        self.ui.menu_Export_As_Source.setEnabled(True)
        self.ui.menuExport_As.setEnabled(True)
        self.ui.menuClear.setEnabled(True)
        self.ui.menu_Clear_Source.setEnabled(True)
        self.ui.menu_Clear_Output.setEnabled(True)
        self.ui.menu_Undo_Output.setEnabled(True)
        self.ui.menu_Redo_Output.setEnabled(True)
        self.ui.menu_RGB_to_Grayscale.setEnabled(True)
        self.ui.menu_RGB_to_HSV.setEnabled(True)
        self.ui.menu_Multi_Otsu_Thresholding.setEnabled(True)
        self.ui.menu_Chan_Vese_Segmentation.setEnabled(True)
        self.ui.menu_Morphological_Snakes.setEnabled(True)
        self.ui.menu_Roberts.setEnabled(True)
        self.ui.menu_Sobel.setEnabled(True)
        self.ui.menu_Scharr.setEnabled(True)
        self.ui.menu_Prewitt.setEnabled(True)    
        
        ###############
        
              
        self.ui.pushButton_Export_as_Source.setEnabled(True)
        self.ui.pushButton_Open_Source.setEnabled(True)
        self.ui.pushButton_Clear_Source.setEnabled(True)
        self.ui.pushButton_Clear_Output.setEnabled(True)
        self.ui.pushButton_Undo_Output.setEnabled(True)
        self.ui.pushButton_Redo_Output.setEnabled(True)
        
        self.ui.pushButton_Export_as_Source.setEnabled(True)
        self.ui.pushButton_RGB_to_Grayscale.setEnabled(True)
        self.ui.pushButton_RGB_to_HSV.setEnabled(True)
        self.ui.pushButton_Multi_Otsu_Thresholding.setEnabled(True)
        self.ui.pushButton_Chan_Vese_Segmentation.setEnabled(True)
        self.ui.pushButton_Morphological_Snakes.setEnabled(True)
        self.ui.pushButton_Roberts.setEnabled(True)
        self.ui.pushButton_Sobel.setEnabled(True)
        self.ui.pushButton_Scharr.setEnabled(True)
        self.ui.pushButton_Prewitt.setEnabled(True)
        self.ui.pushButton_Clear_Source.setEnabled(True)
        self.ui.pushButton_Clear_Output.setEnabled(True)

    def enable_output_related_widgets(self):
        """Enables output related widgets"""
        self.ui.menu_Save_Output.setEnabled(True)
        self.ui.menu_Save_As_Output.setEnabled(True)
        self.ui.menu_Export_As_Output.setEnabled(True)

        self.ui.pushButton_Save_Output.setEnabled(True)
        self.ui.pushButton_Save_as_Output.setEnabled(True)
        self.ui.pushButton_Export_as_Output.setEnabled(True)
        

    def disable_some_widgets_before_input(self):
        """Disables some widgets existing in the UI if a source image is NOT present in the input"""
        self.ui.menu_Open_Source.setEnabled(True)
        self.ui.menu_Export_As_Source.setEnabled(False)        
        self.ui.menuExport_As.setEnabled(False)
        self.ui.menuClear.setEnabled(False)
        self.ui.menu_Clear_Source.setEnabled(False)
        self.ui.menu_Clear_Output.setEnabled(False)
        self.ui.menu_Undo_Output.setEnabled(False)
        self.ui.menu_Redo_Output.setEnabled(False)
        self.ui.menu_RGB_to_Grayscale.setEnabled(False)
        self.ui.menu_RGB_to_HSV.setEnabled(False)
        self.ui.menu_Multi_Otsu_Thresholding.setEnabled(False)
        self.ui.menu_Chan_Vese_Segmentation.setEnabled(False)
        self.ui.menu_Morphological_Snakes.setEnabled(False)
        self.ui.menu_Roberts.setEnabled(False)
        self.ui.menu_Sobel.setEnabled(False)
        self.ui.menu_Scharr.setEnabled(False)
        self.ui.menu_Prewitt.setEnabled(False)    
        
        ###############

        self.ui.pushButton_Open_Source.setEnabled(True) 
        self.ui.pushButton_Export_as_Source.setEnabled(False)
        self.ui.pushButton_Clear_Source.setEnabled(False)
        self.ui.pushButton_Clear_Output.setEnabled(False)
        self.ui.pushButton_Undo_Output.setEnabled(False)
        self.ui.pushButton_Redo_Output.setEnabled(False)
        self.ui.pushButton_Export_as_Source.setEnabled(False)

        self.ui.menuExport_As.setEnabled(False)
        self.ui.pushButton_RGB_to_Grayscale.setEnabled(False)
        self.ui.pushButton_RGB_to_HSV.setEnabled(False)
        self.ui.pushButton_Multi_Otsu_Thresholding.setEnabled(False)
        self.ui.pushButton_Chan_Vese_Segmentation.setEnabled(False)
        self.ui.pushButton_Morphological_Snakes.setEnabled(False)
        self.ui.pushButton_Roberts.setEnabled(False)
        self.ui.pushButton_Sobel.setEnabled(False)
        self.ui.pushButton_Scharr.setEnabled(False)
        self.ui.pushButton_Prewitt.setEnabled(False)
        self.ui.pushButton_Clear_Source.setEnabled(False)
        self.ui.pushButton_Clear_Output.setEnabled(False)

    def disable_output_related_widgets(self):
        self.ui.menu_Save_Output.setEnabled(False)
        self.ui.menu_Save_As_Output.setEnabled(False)
        self.ui.menu_Export_As_Output.setEnabled(False)

        self.ui.pushButton_Save_Output.setEnabled(False)
        self.ui.pushButton_Save_as_Output.setEnabled(False)
        self.ui.pushButton_Export_as_Output.setEnabled(False)



