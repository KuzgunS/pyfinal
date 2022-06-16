




class Mammal:

    def __init__(self,species):
        self.__species = species

    def show_species(self):
        print("I am a", self.__species)
    
    def make_sound(self):
        print("Grrr")


class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self,"Dog")
        
    def make_sound(self):
        print('Woof! Woof!')