


# Box Layout (Mizanpaj xd)

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


    layout_yatay = QtWidgets.QHBoxLayout() # horizontal box layout
    layout_dikey = QtWidgets.QVBoxLayout()# vertical box layout

    layout_yatay.addWidget(buton1)
    layout_yatay.addWidget(buton2)
    layout_dikey.addWidget(buton3)
    layout_dikey.addWidget(buton4)


    layout_dikey.addLayout(layout_yatay) # layout içine layout
    pencere.setLayout(layout_dikey)






    pencere.show()
    sys.exit(nesne.exec_())





arayuz()
