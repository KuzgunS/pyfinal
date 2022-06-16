


import Coin
#ya da from Coin import Coin yapıp 
# coin1 = Coin(False) yapabilirsin

coin1 = Coin.Coin(False)

print("sideup is: ", coin1.get_sideup())

for count in range(10):
    coin1.toss()
    print("sidedown is: ", coin1.get_sideup()) # zulul