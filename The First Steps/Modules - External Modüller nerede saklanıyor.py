Pycharm da solda External Libraries kısmı var,
onun altında Python ve sürümünün yazdığı yer
Onun altında "Lib" yazan yerin altında.

ya da dışarıdan bir external modül indirildiyse aynı yerde site-packages altına yükleniyor.
orada yüklenilen modüller klasör içinde olabiliyor. Mesela python-docx indirildiyse
klasör ismi docx çıktı, import docx yazarak kullanılmaya başlanıyor modül.

**************************************************


BAŞIMA ÇOK SİK SİK BİR ŞEY DE GELDİ. Ben önceden Visual Stuido'da yüklediğim için, bir şekilde
gördüm ki, External Libraries> Python "versiyon"> Lib', in directorysi D'deki visual studiodaki Lib'in
içine gidiyor ama Pip bunu c:\users\awe\appdata\local\programs\python\python38-32\lib\site-packages (0.8.10)
'e yüklüyor. Şimdi pip'in farklı yere yüklemesini sağlayabiliniyor sanırım ama, ben bu libin yerini değişmek istedim.
Direkt bu olmuyormuş ama Project interpreter diye bir şey var. Yukardan File>Settings yapınca Project:"Proje ismi"
kısmında Project interpreter kısmı var. Sağ üstteki dişliye tıklayıp add>system interpreter tıklayınca
C:\Users\Awe\AppData\Local\Programs\Python\Python38-32\python.exe kısmını seçtim, bu sefer istediğim Lib
directory'si oluştu ve oraya yüklediğim modülleri kullanabildim.
 Ancak bu sefer  Proje ismindeki klasörde> venv kısmı kırmızı oldu, "excluded folders"
olmuş. Neden bilmiyorum. Ancak kodlarımı çalıştırmaya etki etmedi bu durum.














