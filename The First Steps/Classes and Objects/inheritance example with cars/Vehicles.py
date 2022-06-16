


class Automobile:
    def __init__(self,model,price):
        self.__model = model
        self.__price = price


    def set_model(self,model):
        self.__model = model
    
    def set_price(self,price):
        self.__price = price

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price


class Car(Automobile): #Car class is subclass of Automobile, it inherits from Automobile class
    def __init__(self, model,price, doors):
        
        Automobile.__init__(self,model,price)
        self.__doors = doors

    def set_doors(self,doors):
        self.__doors = doors
    def get_doors(self):
        return self.__doors

class Truck(Automobile):
    def __init__(self, model,price, tonnage):
        Automobile.__init__(self,model,price)
        self.__tonnage = tonnage
    
    def set_tonnage(self,tonnage):
        self.__tonnage = tonnage
    def get_tonnage(self):
        return self.__tonnage