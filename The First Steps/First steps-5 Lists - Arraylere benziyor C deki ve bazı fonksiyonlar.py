
# normal variable gibi tanımlamaya başlıyoruz.

arkadaslar = ["Ayca", 22, False]  # C'de structure oluşturuyorduk ayrı ayrı içinde bir sürü şey olan şey tanımlamak
# için. Burda direkt içine bir sürü şey yazabildik.
print(arkadaslar[1])  # arkadaslar degiskeninin icindeki 22'ye ulaştım.
print(arkadaslar[-1])  # geriye de sayıyor xdd, iyimiş
#  print(arkadaslar[3])  # buna out of range diyor, yani direkt mod alıp hangisi array elementi diye bulmuyor.
print(arkadaslar[-3])
# print(arkadaslar[-4]) buna out of range diyor mantıklı.
print("----------------------------")
print(arkadaslar[1:])
print(arkadaslar[-2:])  # yukarıda ve burda 1,-2 gibi seçilmiş elementin sağındakilerin hepsini yazdırdı.
print(arkadaslar[0:2])  # asıl olayı aralık yazdırmak.
print(arkadaslar[0:3333])  # range aşılsa bile bu şekilde hata vermeden en sona kadar yazıyor
# print(arkadaslar[0, 1]) virgülle bir sürü seçim olmuyor.

arkadaslar[1] = 123  # sonradan list içini de modifiye edebiliyorsun.
print(arkadaslar[1])

sayilar = [1,2,3,4]
isimler = ["Bob" , "memer123"]
isimler.extend(sayilar)  # isimlerin yanına sayıları ekledik
print(isimler)

isimler.append("qewr")
print(isimler)

isimler.insert(1, "XDXDXDXD")  # birinci sıraya XDXDXD ekleyip diğerlerini kaydırdı
print(isimler)

isimler.remove("XDXDXDXD")  # yazdığımız element çıkarıldı.
print(isimler)

isimler.pop()   # sondaki element çıkarıldı.
print(isimler)

print(isimler.index("memer123"))  # yazılanın hangi indexte olduğunu söylüyor
# print(isimler.index("mwerwqrwqrwqerw"))  #error veriyor olmayanı aratınca.

print(isimler.count("Bob"))  # kaç tane Bob var onu saydırdı.

# isimler.sort()  # alfabetik şekilde ya da numaraları artan şekilde listeyi sıralıyor.
# liste içinde hem yazı hem sayı varsa error veriyor.

intandfloat = [1, 3.3333, 5, 2.44]
print(intandfloat)
intandfloat.sort()
print(intandfloat)

# print(intandfloat.reverse()) burda başta func uygulamadan print içinde uygulattıramadık.
# print(intandfloat)

intandfloat2 = intandfloat.copy() #direkt eşitlemek de aslında işe yaradı ama bu func da var.
print(intandfloat2)




