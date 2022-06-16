from PyQt5 import QtWidgets
import sys
from HesapMakinesi import Ui_MainWindow # aynı directory içindeki, içinde UI'nin Ui_MainWindow class'ı bulunan HesapMakinesi.py dosya ve modülünü çağırdık
import Calculator # sinyalleri yazdığımız modülü import ettik


def application():
    app = QtWidgets.QApplication(sys.argv)
    win = Calculator.Batu_Calculator()
    win.show()
    sys.exit(app.exec_())

application()