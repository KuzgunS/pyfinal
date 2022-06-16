


# Grid Layout (Izgara Mizanpaj xd)

import sys
from PyQt5 import QtWidgets

def arayuz():

    nesne = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("Layout")
    pencere.setGeometry(100,100,400,400)

    buton1 = QtWidgets.QPushButton(pencere)
    buton1.setText("Buton1")

    buton2 = QtWidgets.QPushButton(pencere)
    buton2.setText("Buton2")

    buton3 = QtWidgets.QPushButton(pencere)
    buton3.setText("Buton3")

    buton4 = QtWidgets.QPushButton(pencere)
    buton4.setText("Buton4")


    layout = QtWidgets.QGridLayout()

    layout.addWidget(buton1,1,1)
    layout.addWidget(buton2,1,2)
    layout.addWidget(buton3,1,3)
    layout.addWidget(buton4,2,4)


    pencere.setLayout(layout)






    pencere.show()
    sys.exit(nesne.exec_())





arayuz()
