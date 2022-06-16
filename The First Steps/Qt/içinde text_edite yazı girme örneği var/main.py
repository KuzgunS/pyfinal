"""
main code to run data clusterer with all its functions

"""

from PyQt5 import QtWidgets # for running the UI
import sys # needed for running UI
import Backhand # import Backhand module which handles the backhand connection operations of the UI


def application(): 
    """    
    Runs the UI with all the front and back end parts.    
    """
    app = QtWidgets.QApplication(sys.argv)
    win = Backhand.Operate() # UI windows

    win.show()
    sys.exit(app.exec_())


application() # run application


