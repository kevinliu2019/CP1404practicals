MIN_LENGTH = 4


def main():
    password = get_password(MIN_LENGTH)
    print_pass(password)


def get_password(minimum_length):
    password = input("Enter password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter password of at least {} characters: ".format(minimum_length))
    return password


def print_pass(sequence):
    print('*' * len(sequence))


main()
