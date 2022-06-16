def myfirstfunc(): # sadece indentlenmiş yerler fonksiyon tanımı içinde oluyor
    print("Selam <:)")
  #print("deneme1")
 #print("deneme2")
#print("deneme3")  # vay amk ya böyle yarı indentlilerde resmen error verdi.
print("deneme4")

myfirstfunc()

def say_hi(name, number): #içine değişken aldığını böyle gösteriyoruz.
    print("Selam " + name + " your age is " + number)
say_hi("Ömer", "12")

avariable = "BEN BİR DEĞİŞKENİM"
say_hi(avariable, "12") # içine variable de atayabiliyoruz güzel.

print("----------------------------------------------")


def cube(num):
    return num*num*num  #return sonrası kod yazılamıyor. Return koddan çıkartıyor.
    #return her türlü değişkeni gönderebiliyormuş.
    print("xdxdxd") #never printed

a_float_number=0.455
print(cube(a_float_number)) #fonksiyon çağırıldığında içinde işlemler yapıldı ve geriye bir şey döndürdü, onu da yazdırdık
                   #sadece bu haldeyken bize print işlemini yaptırdı.
print(str(cube(a_float_number)) + " is the cube of " + str(a_float_number) )
#direkt string halinde kullanmak için str lazım oldu.
