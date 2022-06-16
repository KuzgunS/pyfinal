grid = [
    [1, 2, 3],
    [4, 5, 6 ],
    [7, 8, 9],
    [0],
    ["lul",True]
]

# list ve array arası fark bu, listlerin içinde bir sürü farklı type data girilebiliyor.
# array'da ise buna izin verilmiyor, array "1 boyutlu" ama daha memory efficient.

print(grid[0][2]) # ilk satır "0" ve onun içindeki üçüncü eleman "2" yani 3 yazdıracak.
print(grid[4][1])

print("\n")

for row in grid:
    print(row)

for row in grid:
    for column in row:
        print(column)

#Pythondaki for loop özelliğini anlamak için iyi bir örnek. Buradaki for, belli bir değere sahip variable'ı saydırmıyor
# "in grid" kısmı koyulduğu an, listenin baştan sonuna listenin elemanlarını saydırıyor, o liste içindekileri de
# saydırmak için tekrar bir for loop kullandık.











