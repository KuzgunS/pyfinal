

#%%
import coin_module # coin classı import edildi


my_coin1= coin_module.Coin("Heads") # Coin classından obje oluşturuldu.
my_coin1.print_sides()
my_coin1.toss()
my_coin1.print_sides()


# my_coin1.sideup = "LULS ITS NOT HIDDEN" #sideup isnt private
my_coin1.__sidedown = "hidden so error"
my_coin1.print_sides()

print(my_coin1) # __str__(self) metodu kullanılacak

msg1 = str(my_coin1) # objeyi yazdıracakken classın str metodunun döndürdüğü stringi bu şekilde variable da çekebiliyorsun
print(msg1)
msg2 = my_coin1.__str__()  #buna da denedim bu da oluyormuş da önemli değil
print(msg2) #yukardakiyle aynı 
# %%
