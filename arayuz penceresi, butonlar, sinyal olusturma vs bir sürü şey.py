





import sys
from PyQt5 import QtWidgets, QtCore
from sympy import rad

def arayuz():
    nesne = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    

    pencere.setWindowTitle("PyQt5 ile Arayüz Penceresi")
    pencere.setGeometry(10,50,900,800) #x'den 10 pilsel sağda, y'den 50 piksel aşağıda, diğerleri genişlik


    #arayuze etiket ekleme
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("etiket")
    etiket.move(100,200) #etiketi belli lokasyona attık

    #arayuze giriş alanı ekleme(Line Edit)
    etiket_line_edit = QtWidgets.QLabel(pencere)
    etiket_line_edit.setText("Line Edit")
    etiket_line_edit.move(100,280)

    satir = QtWidgets.QLineEdit(pencere)    
    satir.move(100,300)
    
    satir.setEchoMode(QtWidgets.QLineEdit.Password)
        # alana default bir şey yazdırıp onun değiştirilmemesini istersen
    #satir.setText("2.4 asdfa")#
    #satir.setReadOnly(True)


    #arayuze push button ekleme
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Ben butonum")
    buton.move(100,400)
    buton.setEnabled(False) #butonu inaktif yapmak için

    #arayuze radiobutton ekleme
    radiobutton1 = QtWidgets.QRadioButton(pencere)
    radiobutton2 = QtWidgets.QRadioButton(pencere)
    radiobutton3 = QtWidgets.QRadioButton(pencere)
    radiobutton1.move(100,500)
    radiobutton2.move(100,520)
    radiobutton3.move(100,540)
    radiobutton1.setText("Seçenek1")
    radiobutton2.setText("Seçenek1")
    radiobutton3.setText("Seçenek1")

    radiobutton3.setCheckable(False) # radio3'ü seçilemez yapmak için

    #arayuze kontrol kutusu ekleme (checkbox)
    checkbox1 = QtWidgets.QCheckBox(pencere)
    checkbox2 = QtWidgets.QCheckBox(pencere)
    checkbox3 = QtWidgets.QCheckBox(pencere)

    checkbox1.setText("Seçenek 1")
    checkbox2.setText("Seçenek 2")
    checkbox3.setText("Seçenek 3")
    
    checkbox1.move(100,600)
    checkbox2.move(100,620)
    checkbox3.move(100,640)

    checkbox1.setCheckable(False) #seçilemez yapmak için

    #arayüze açılır seçim kutusu (combo box) ekleme

    combo = QtWidgets.QComboBox(pencere)
    combo.addItem("scan")
    combo.addItem("qwe")
    combo.addItem("asdf")
    combo.move(300,200)
    print(combo.count()) #içinde kaç seçenek var yazdırıyor
    combo.setItemText(1,"qwe'yi bu şekilde değiştirdim")

    #arayüze spin box  (combo box) ekleme

    spin_box = QtWidgets.QSpinBox(pencere)
    spin_box.move(300,300)
    spin_box.setRange(-500,10000) # max min aralıklarını ayarlama
    spin_box.setSingleStep(100) # artış azalış kaç kaç olsun diye
        # artışları float yapmak istersen
    spin_box = QtWidgets.QDoubleSpinBox(pencere)
    spin_box.move(300,400)
    spin_box.setSingleStep(.5)


    #arayüze slider  ekleme (slider)
    slider1 = QtWidgets.QSlider(QtCore.Qt.Horizontal,pencere) # horizontal slider
    slider1.move(300,500)
    slider1.setMinimum(0)
    slider1.setMaximum(1000)
    slider1.setTickPosition(QtWidgets.QSlider.TicksBelow) #altta çizgi gösteriyor
    slider1.setTickInterval(250) # çizgilerin aralıklarını gösteriyor
    slider1.setValue(250) # initial bir değerden başlaması için


    slider2 =  QtWidgets.QSlider(QtCore.Qt.Vertical,pencere)
    slider2.move(300,600)

    #signal slot hazırlama
    satir2 = QtWidgets.QLineEdit(pencere)    
    satir2.setReadOnly(True)
    satir2.move(600,200)

    buton2 = QtWidgets.QPushButton(pencere)
    buton2.move(600,300)
    buton2.setText("Gonder")

    def guncelle():
        satir2.setText("XDDD")

    buton2.clicked.connect(guncelle) #burada, tıklandığında bir fonksiyona bağlanacak hale getirdik


#----------
    pencere.show() 
    sys.exit(nesne.exec_())

    

arayuz()