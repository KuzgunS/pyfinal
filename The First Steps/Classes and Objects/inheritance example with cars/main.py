
import Vehicles

def main():
    car1 = Vehicles.Car("2003","25.000$",4) # model, price, doors

    #display car data
    print("car data:")
    print("model: ", car1.get_model())
    print("price: ", car1.get_price())
    print("# of doors: ", car1.get_doors())

    print("\n")
    print("truck data:")
    truck1 = Vehicles.Truck("2018","1.000.000$",300) # model, price, tonnage
    print("model: ", truck1.get_model())
    print("price: ", truck1.get_price())
    print("tonnage: ", truck1.get_tonnage())

main()