finished = False
result = 0
while not finished:
    try:
        # TODO: this line
        # TODO: this line
        result = int(input("Enter the number: "))
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)