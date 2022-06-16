from PyQt5 import QtWidgets
import sys
from HesapMakinesi import Ui_MainWindow # aynı directory içindeki, içinde UI'nin Ui_MainWindow class'ı bulunan HesapMakinesi.py dosya ve modülünü çağırdık


class Batu_Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Batu_Calculator,self).__init__()
        self.ui = Ui_MainWindow() #obje oluşturduk
        self.ui.setupUi(self)

        self.ui.pushButton_toplama.clicked.connect(self.hesapla)
        self.ui.pushButton_cikarma.clicked.connect(self.hesapla)
        self.ui.pushButton_carpma.clicked.connect(self.hesapla)
        self.ui.pushButton_bolme.clicked.connect(self.hesapla)

        
    def hesapla(self):
        gelenVeri = self.sender().text()

        if gelenVeri == "TOPLAMA":
            sonuc = int(self.ui.lineEdit_birinci_sayi.text()) + int(self.ui.lineEdit_ikinci_sayi.text())
        elif gelenVeri == "ÇIKARMA":
            sonuc = int(self.ui.lineEdit_birinci_sayi.text()) - int(self.ui.lineEdit_ikinci_sayi.text())
        elif gelenVeri == "ÇARPMA":
            sonuc = int(self.ui.lineEdit_birinci_sayi.text()) * int(self.ui.lineEdit_ikinci_sayi.text())
        elif gelenVeri == "BÖLME":
            sonuc = round(float(self.ui.lineEdit_birinci_sayi.text()) / float(self.ui.lineEdit_ikinci_sayi.text()),4) 
        
        self.ui.label_sonuc.setText('Sonuç:' + str(sonuc))

