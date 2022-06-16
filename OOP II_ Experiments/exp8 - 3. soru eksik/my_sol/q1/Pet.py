


class Pet:

    def __str__(self):
        return "ANİMAL TYPE: " + self.__animal_type + "\nIT'S NAME: " + self.__name + "\nIT'S AGE: " + self.__age

    def __init__(self,name,a_type,age): # initializer method
        self.__name = name
        self.__animal_type = a_type
        self.__age = age


    def set_name(self,name):
        self.__name = name
    def set_animal_type(self,a_type):
        self.__animal_type= a_type
    def set_age(self,age):
        self.__age = age   

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return  self.__age
    
    


