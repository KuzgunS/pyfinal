

from venv import create
import Animals


def main():
    mammal1 = Animals.Mammal("whale")
    mammal1.show_species()
    mammal1.make_sound()

    print("\n")
    dog1 = Animals.Dog()
    dog1.show_species()
    dog1.make_sound()

    print("\n\n-----show_mammal_info")
    show_mammal_info(mammal1)
    show_mammal_info(dog1)

    print("\n\n-----show_mammal_info_without_attribute_error")   
    show_mammal_info_without_attribute_error(mammal1)
    show_mammal_info_without_attribute_error(dog1)
    show_mammal_info_without_attribute_error(12321321321)
    show_mammal_info_without_attribute_error("xddd")

def show_mammal_info(object):
    object.show_species()
    object.make_sound()

def show_mammal_info_without_attribute_error(object):
    if isinstance(object, Animals.Mammal):
        object.show_species()
        object.make_sound()
    else:
        print("thats not a mammal you duck")



main() 