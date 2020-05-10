from prac_06.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_list = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!\n{}".format(MENU))
    menu_choice = input(">>> ").lower()

    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            taxis_type(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice == "0" or "1" or "2":
                already_owned_taxi = taxis[taxi_choice]
            else:
                print("Invalid option")
        elif menu_choice == "d":
            already_owned_taxi.start_fare()
            drive_distance = float(input("Drive how far? "))
            if drive_distance >= 0:
                already_owned_taxi.drive(drive_distance)
            else:
                print("Invalid option")
            travel_cost = already_owned_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(already_owned_taxi.name, travel_cost))
            total_list += travel_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_list))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_list))
    print("Taxis are now:")
    taxis_type(taxis)


def tests():
    car = Car("Datsun", 180)
    car.drive(30)
    print("fuel =", car.fuel)
    print("odo =", car.odometer)
    car.drive(55)
    print("fuel =", car.fuel)
    print("odo = ", car.odometer)
    print(car)

    distance = int(input("Drive how far? "))
    while distance > 0:
        travel = car.drive(distance)
        print("{} travelled {}".format(str(car), travel))
        distance = int(input("Drive how far? "))

    taxis = Taxi("Prius 1", 100)
    taxis.drive(25)
    print(taxis)
    print(taxis, taxis.get_fare())
    taxis.start_fare()
    taxis.drive(40)
    print(taxis, taxis.get_fare())

    silver_service_taxi = SilverServiceTaxi("Limo", 100, 2)
    print(silver_service_taxi, silver_service_taxi.get_fare())
    silver_service_taxi.drive(10)
    print(silver_service_taxi, silver_service_taxi.get_fare())


def taxis_type(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()