"""@package docstring
This module exist for plotting the input data.
"""
import matplotlib.pyplot as plt # to show initial data as a scatter plot
import os #for file paths

class Plot:
    """This class is used for plotting data.
    """

    def __init__(self):
        """The constructor"""   

    def plot_Scatter(self,f):
        """Shows input data as a scatter on an image file."""
        
        lines = f.readlines()
        x = [float(line.split()[0]) for line in lines]
        y = [float(line.split()[1]) for line in lines]
        plt.scatter(x, y, c ="black")
        plt.savefig(os.getcwd() + "\\input_data.png")
