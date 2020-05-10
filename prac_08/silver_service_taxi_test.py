from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    other_taxi = SilverServiceTaxi("Test different fancy taxi", 100 ,2)
    other_taxi.drive(18)
    other_taxi.get_fare()
    print(other_taxi)


main()