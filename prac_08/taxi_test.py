from prac_08.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    my_taxi.get_fare()
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    my_taxi.get_fare()
    print(my_taxi)


main()