
# tuples
coordinates = (4,5,23,2) # köşeli parantez kullanmadık.
                    # tupleler değiştirilemiyor (immutable), üstüne yazılamıyormuş vs vs
print(coordinates[2])  # listlerdeki gibi ulaşabiliyoruz okumak için
#  coordinates[1] =333333333
#  print(coordinates) 'tuple' object does not support item assignment

coordinateslist = [ (4, 5), 4, (1,2,44), 1.532] #tuple içeren list oluyor.
print(coordinateslist)

coordinatestuple = ([1,2,7,3], 7)

# coordinates.insert(1,333333) tuplelara fonksiyonu IDE otomatik tamamlama yaptırmadı değiştirlemez oldukları için,
# yazınca bile hata veriyor zaten

