# modules bildiğimiz kütüphaneler.

import Modules_Useful_tools_to_import
# ilk başta import edileni de hata var mı diye kontrol ediyor, varsa uyarıyor
# hata yoksa başka bir py dosyasındaki değişkenler, fonksiyonlar vs,
# o py dosyasının ismine nokya koyulduktan sonra ulaşılabiliyor.


print(Modules_Useful_tools_to_import.meters_in_kilometer)

print(Modules_Useful_tools_to_import.roll_dice(2))
print(Modules_Useful_tools_to_import.roll_dice(2))
print(Modules_Useful_tools_to_import.roll_dice(2))
print(Modules_Useful_tools_to_import.roll_dice(2))
print(Modules_Useful_tools_to_import.roll_dice(2))
print(Modules_Useful_tools_to_import.roll_dice(2))
print(Modules_Useful_tools_to_import.roll_dice(2))

# roll_dice(2) bu direkt işe yaramıyor, bu fonksiyonun nerede olduğu
# yukarıdaki gibi dosya ismiyle belirtilmeli ve nokta koyarak ulaşılmalı.

# module olarak kullanılacakların ismini bu yüzden basit ve sade tut.

print(Modules_Useful_tools_to_import.roll_dice(100))

Modules_Useful_tools_to_import.roll_dice(15)

