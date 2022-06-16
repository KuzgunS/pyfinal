


# Grid Layout (Izgara Mizanpaj xd)

import sys
from PyQt5 import QtWidgets

def arayuz():

    nesne = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("Layout")
    pencere.setGeometry(100,100,400,400)

   
    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket1.setText("x:")
    etiket2.setText("y:")

    satir1 = QtWidgets.QLineEdit(pencere)
    satir2 = QtWidgets.QLineEdit(pencere)

    layout = QtWidgets.QFormLayout()
    layout.addRow(etiket1,satir1)
    layout.addRow(etiket2,satir2)

    pencere.setLayout(layout)


    pencere.show()
    sys.exit(nesne.exec_())


arayuz()








