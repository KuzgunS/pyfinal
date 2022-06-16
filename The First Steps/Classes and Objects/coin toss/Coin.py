
import random

class Coin:

    def __init__(self,sideup = True):
        self.__sideup = sideup
        self.__sidedown = not sideup




    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = True
        else:
            self.__sideup = False

    def get_sideup(self):
        return self.__sideup
    
    def get_sidedown(self):
        return self.__sidedown 
