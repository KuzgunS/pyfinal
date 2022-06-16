"""
main code to run image processer with all its functions

"""

from PyQt5 import QtWidgets # for running the UI
import sys # needed for running UI
import Backhand # import Backhand module which handles the backhand connection operations of the UI


def application(): 
    """    Runs the UI with all the front and back end parts.    """
    app = QtWidgets.QApplication(sys.argv)
    win = Backhand.Operate() # UI windows

    win.show() # show window
    sys.exit(app.exec_())


application() # run application


