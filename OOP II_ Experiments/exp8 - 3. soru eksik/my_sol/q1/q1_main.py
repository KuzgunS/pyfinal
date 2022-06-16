


import Pet


def main():
    name = input("enter your pet's name ")
    anim_type = input("enter your pet type ")
    age = input("enter your pets age ")

    my_pet = Pet.Pet(name,anim_type,age)

    print("oops wrong kind of animal is input, changing it")
    my_pet.set_animal_type("foken donkeey")

    print(my_pet)

main()
