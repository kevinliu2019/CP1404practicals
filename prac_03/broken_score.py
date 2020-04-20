"""Get score and determine the status."""


def main():
    score = float(input("Enter score: "))
    print(detemine_status(score))


def detemine_status(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()