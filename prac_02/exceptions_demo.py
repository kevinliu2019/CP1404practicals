"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#Q1: When numerator or denominator is not number, it will occur ValueError.
#Q2: When denominator is 0, it will occur ZeroDivisionError.

#Q3
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
if denominator == 0:
    print("Cannot divide by zero")
else:
    try:
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
print("Finished.")