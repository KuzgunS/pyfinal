
#%%
import random



class Coin:

    def __str__(self):
        return "XDD the sideup is:" + self.sideup


    def __init__(self,sideup): # initializer method
        self.coin_dict = {
        "Heads" : False,
        "Tails" : True,
        False : "Heads",
        True : "Tails"
        }
        self.sideup = sideup
        self.__sidedown = not self.coin_dict[self.sideup]

    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"
        self.__sidedown = not self.coin_dict[self.sideup]

    def get_sideup(self):
        return self.sideup

    def print_sides(self):
        print("the sideup is:", self.sideup)
        print("the sidedowns is:", self.__sidedown)
        print()


# %%
