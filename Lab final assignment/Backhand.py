"""@package docstring
    Backhand module for connections and functions of UI.
"""

from PyQt5 import QtWidgets, QtGui, QtCore# for working with UI
from PyQt5.QtWidgets import QFileDialog # for file functions
from Image_Operator import Ui_MainWindow # in the same directory, import Ui_MainWindow class in the file and module Image_Operator

import skimage # for image processing
from skimage import io # for image processing input/output operations

import numpy as np # necessary for some side operations for image processing
from PIL import ImageQt # for saving the output image.

class Operate(QtWidgets.QMainWindow):
    """
    This class conducts necessary operations to handle image operator functions and ui connections.
    """
    def __init__(self):
        """The constructor"""
        super(Operate,self).__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        #set signal connections
        self.ui.menu_Open_Source.triggered.connect(self.open_source)
        self.ui.menu_Exit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        self.ui.menu_RGB_to_Grayscale.triggered.connect(self.RGB2Gray)
        self.ui.menu_RGB_to_HSV.triggered.connect(self.RGB2HSV)
        self.ui.menu_Multi_Otsu_Thresholding.triggered.connect(self.multi_otsu_threshold)
        self.ui.menu_Chan_Vese_Segmentation.triggered.connect(self.chan_vese)
        self.ui.menu_Morphological_Snakes.triggered.connect(self.Morphological_Snakes)
        self.ui.menu_Roberts.triggered.connect(self.Roberts_edge) 
        self.ui.menu_Sobel.triggered.connect(self.Sobel_edge)
        self.ui.menu_Scharr.triggered.connect(self.Scharr_edge) 
        self.ui.menu_Prewitt.triggered.connect(self.Prewitt_edge) 
        self.ui.menu_Clear_Source.triggered.connect(self.clearSource)
        self.ui.menu_Clear_Output.triggered.connect(self.clearOutput)
        self.ui.menu_Save_Output.triggered.connect(self.file_save)
        self.ui.menu_Save_As_Output.triggered.connect(self.save_as)
        self.ui.menu_Export_As_Source.triggered.connect(self.export_as_source)
        self.ui.menu_Export_As_Output.triggered.connect(self.export_as_output) 
        
        self.ui.pushButton_Open_Source.clicked.connect(self.open_source)
        self.ui.pushButton_RGB_to_Grayscale.clicked.connect(self.RGB2Gray)
        self.ui.pushButton_RGB_to_HSV.clicked.connect(self.RGB2HSV)
        self.ui.pushButton_Multi_Otsu_Thresholding.clicked.connect(self.multi_otsu_threshold)
        self.ui.pushButton_Chan_Vese_Segmentation.clicked.connect(self.chan_vese)
        self.ui.pushButton_Morphological_Snakes.clicked.connect(self.Morphological_Snakes)
        self.ui.pushButton_Roberts.clicked.connect(self.Roberts_edge) 
        self.ui.pushButton_Sobel.clicked.connect(self.Sobel_edge)
        self.ui.pushButton_Scharr.clicked.connect(self.Scharr_edge) 
        self.ui.pushButton_Prewitt.clicked.connect(self.Prewitt_edge) 
        self.ui.pushButton_Clear_Source.clicked.connect(self.clearSource)
        self.ui.pushButton_Clear_Output.clicked.connect(self.clearOutput)
        self.ui.pushButton_Save_as_Output.clicked.connect(self.save_as)
        self.ui.pushButton_Export_as_Source.clicked.connect(self.export_as_source)
        self.ui.pushButton_Export_as_Output.clicked.connect(self.export_as_output)

    def open_source(self):
        """Open a file by browsing and enable some UI widgets"""
        filename = QFileDialog.getOpenFileName(self,'Open Source','D:',"Image Files (*.png *.jpg)")
        self.ui.label_input_image.setPixmap(QtGui.QPixmap(filename[0])) #filename comes as a tuple so we use the 0th indice for directory string
        self.source_image = io.imread(filename[0]) #read image
        self.enable_some_widgets_after_input()  # enables some UI widgets 
        

    def clearSource(self):
        """Clears source image from UI and disables some UI widgets"""
        self.ui.label_input_image.setPixmap(QtGui.QPixmap()) #clear image from input on the UI
        self.disable_some_widgets_before_input() # disables some UI widgets 
        self.clearOutput() # clearSource also clears output as given in the specification

    def clearOutput(self):
        """Clears output image from UI and disables some UI widgets related to the output""" 
        self.ui.label_output_image.setPixmap(QtGui.QPixmap()) #clear output
        self.disable_output_related_widgets() #disables some UI widgets related to the output
    
    def file_save(self):
        image = ImageQt.fromqpixmap(self.ui.label_output_image.pixmap()) #save output image on the UI
        image.save('SAVED.png') # save it as png

    def save_as(self):
        """Save output to chosen location with a chosen file name"""
        image = ImageQt.fromqpixmap(self.ui.label_output_image.pixmap()) # get image on the output of the UI
        new_file_path = QFileDialog.getSaveFileName(self, "Save as", "", "Image Files (*.png *.jpg)") # select file path
        file_path = new_file_path[0]
        image.save(file_path) #  save image to chosen filepath

    def export_as_source(self):
        """Export source as .pdf"""
        image1 = ImageQt.fromqpixmap(self.ui.label_input_image.pixmap()) #get image on the input 
        im1 = image1.convert('RGB')
        im1.save(r'SOURCE_PDF_SAVED.pdf') # save image as pdf

    def export_as_output(self):
        """Export input as .pdf"""
        image1 = ImageQt.fromqpixmap(self.ui.label_output_image.pixmap()) #get image on the output 
        im1 = image1.convert('RGB') 
        im1.save(r'OUTPUT_PDF_SAVED.pdf') # save image as pdf

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


    def RGB2Gray(self):
        """Transforms source image to Grayscale and shows it at the output of UI"""
        grayscale_image = skimage.color.rgb2gray(self.source_image)
        io.imsave("temp.png", grayscale_image)
        self.ui.label_output_image.setPixmap(QtGui.QPixmap("temp.png")) 
        self.enable_output_related_widgets()

  
    def RGB2HSV(self):
        """Transforms source image to HSV and shows it at the output of UI"""
        HSV_image = skimage.color.rgb2hsv(self.source_image)
        io.imsave("temp.png", HSV_image)
        self.ui.label_output_image.setPixmap(QtGui.QPixmap("temp.png")) 
        self.enable_output_related_widgets()

    def multi_otsu_threshold(self):
        """Applies Multi-Otsu threshold segmentation to source image and shows it at the output of UI"""
        otsu_threshold =  skimage.filters.threshold_multiotsu(self.source_image)
        regions = np.digitize(self.source_image, bins = otsu_threshold) # otsu image
        io.imsave("temp.png", regions) # save image
        self.ui.label_output_image.setPixmap(QtGui.QPixmap("temp.png")) # show image at the output on the UI
        self.enable_output_related_widgets()

    def chan_vese(self):
        """Applies Chan-Vese segmentation to source image and shows it at the output of UI""" 
        img = skimage.img_as_float(self.source_image)
        chan_vese_image = skimage.segmentation.chan_vese(img, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,  max_num_iter=200, dt=0.5, init_level_set="checkerboard",  extended_output=True)
        io.imsave("temp.png", chan_vese_image[1])
        self.ui.label_output_image.setPixmap(QtGui.QPixmap("temp.png")) 
        self.enable_output_related_widgets()

    def Morphological_Snakes(self): # Morphological ACWE segmentation
        """Applies Morphological Snakes segmentation to source image and shows it at the output of UI"""
        def store_evolution_in(lst):
        # Returns a callback function to store the evolution of the level sets in the given list.   
            def _store(x):
                lst.append(np.copy(x))
            return _store

        image = skimage.img_as_float(self.source_image)
        # Initial level set
        init_ls = skimage.segmentation.checkerboard_level_set(image.shape, 6)
        # List with intermediate results for plotting the evolution
        evolution = []
        callback = store_evolution_in(evolution)
        Morphological_ACWE = skimage.segmentation.morphological_chan_vese(image, num_iter=35, init_level_set=init_ls,smoothing=3, iter_callback=callback)
        io.imsave("temp.png", Morphological_ACWE)
        self.ui.label_output_image.setPixmap(QtGui.QPixmap("temp.png")) 
        self.enable_output_related_widgets()

    def Roberts_edge(self):
        """Applies Roberts edge detection to source image and shows it at the output of UI"""
        edge_roberts = skimage.filters.roberts(self.source_image)
        io.imsave("temp.png", edge_roberts)
        self.ui.label_output_image.setPixmap(QtGui.QPixmap("temp.png")) 
        self.enable_output_related_widgets()

    def Sobel_edge(self):
        """Applies Sobel edge detection to source image and shows it at the output of UI"""
        edge_sobel = skimage.filters.sobel(self.source_image)
        io.imsave("temp.png", edge_sobel)
        self.ui.label_output_image.setPixmap(QtGui.QPixmap("temp.png")) 
        self.enable_output_related_widgets()

    def Scharr_edge(self):
        """Applies Scharr edge detection to source image and shows it at the output of UI"""
        edge_scharr = skimage.filters.scharr(self.source_image)
        io.imsave("temp.png", edge_scharr)
        self.ui.label_output_image.setPixmap(QtGui.QPixmap("temp.png"))
        self.enable_output_related_widgets() 

    def Prewitt_edge(self):
        """Applies Prewitt edge detection to source image and shows it at the output of UI"""
        edge_prewitt = skimage.filters.prewitt(self.source_image)
        io.imsave("temp.png", edge_prewitt)
        self.ui.label_output_image.setPixmap(QtGui.QPixmap("temp.png")) 
        self.enable_output_related_widgets()





