from math import *   # bu importladı başka mat fonksiyonları olan bir yerden, bir de bu en üstte olması lazımmış verdiği
# uyarıya göre

# bu kodlar pycharm ile yazılıyor. Her satırın yanında pek güzel renklerle öneminin belirtildiği uyarı veya
# satırdaki hata notları belirtilmiş hoş güzel.

onun_ismi = "Recep"
onun_yasi = "123"  # bu string olarak algılandı, sayılar tırnaksız yazılıyor.
şunu_sever = "Ayasofya ve Gündem Değişikliği ve Siyasal İslam"  # ASCII'de olmayan karakterlerin variable name
# içinde olmasını istemese de program çalışıyor bak bak bi de line too long diyor bak şimdi asdfkjasdkfjasdfasjfhaskldjfhdsakjfhaslk

print("benim adım Batu, 22 yaşındayım, kedileri severim.")
print("senin adın şu:" + onun_ismi + ", yaşın bu:" + onun_yasi + ", şunu da seversin:" + şunu_sever)  # + operatoründen
# sonra hep boşluk istiyor la.

onun_ismi = "Gılıjdar"  # variable ler bu şekilde sonradan değiştirilebildi.

print("Eyyyy " + onun_ismi + " sen de aynı boksun")

numara = 44.4
print("+numara")
# print(+ "numara") bu şekil kullanımı olmamağlı. type error veriyor.
print(+ numara)  # bu şekil işe yaradı.
print(numara)  # direkt + koymadan numara yazarak başlamak da işe yaradı
#  print(numara + "slm") #  bu olmuyor la, biri int, diğeri string diyor.
print("-------------------------------------------")
#  Boolean fonkları da datatype oluyormuş.
isTrue = True
isFalse = False
print(isTrue)
print(isFalse)
print(isTrue * isFalse)  # hehe mantıksal aritmetik de yapıyor la
print("-------------------------------------------")

print("Bak yazı aşağıya\nkaydı ve tırnak yazdırdım\"\"\"\"\"")
string_1 = "merhabalar"
string_2 = "selamlar"
print(string_1)
print("-------------------------------------------")

#  print(+ string_1)  bu olmeyo bi hata veriyor.
print(string_1 + " " + string_2)  # concatenation

print("-------------------------------------------")
print("fonksiyonlar")

print(string_1.upper())  # sadece yazdırırken değiştiriyor, variable değişmedi.
print(string_1.isupper())
print(string_1.upper().isupper())  # hmm ilginç, yani fonkları soldan sağa sıralayıp sıra sıra işe yarattırabiliyorz.
print(len(string_1))  # len fonk içine variable koyduk, bize length ini geri dönüyor.

print(string_1[2])  # Merhabalar stringinin 3. harfini geri döndü.

print(string_1.index("m"))
print(string_1.index("merha"))
print(string_1.index("ha"))
print(string_1.index("r"))  # bu fonksiyon içine giren parametrenin ilk nerede göründüğünü 0'dan başlayarak söylüyor.
# print(string_1.index("QWE")) #stringin içinde yazılan parametre yoksa hata veriyor.

string_3 = "merhabalar merak Merul"
print(string_3.replace("mer", "yar"))

print("working with numbers----------------------------------")
print(1 + 2, 943)  # bu ilginçmiş virgül ne işe yarıyor anlamadım
print(3 * 5)

print(5 % 3)  # mod yapıyor

a_number = 3
print(a_number)
#  print(a_number + "will this work?") böyle çalışmıyor, sayıyı str ye çevirmek gerekiyor.
print(str(a_number) + " will this work ?")

a_negative_number = -12
print(abs(a_negative_number))
print(pow(a_negative_number, 2))
print(max(4, -3))
print(min(4, -3))
print(round(3.5))



print(floor(3.7))  # sayıyı önce gelen ilk integere yuvarladı
print(sqrt(2))