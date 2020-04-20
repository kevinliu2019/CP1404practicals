"""
CP1404/CP5632 - Practical - Suggested Solution
Quick file opening/writing/reading exercises
"""
#Q1
NAME = open("name.txt", "w")
name = input("What's your name? ")
NAME.write(name)
NAME.close()
#Q2
NAME = open("name.txt", "r")
name = NAME.read().strip()
NAME.close()
print("Your name is", name)
#Q3
NUMBER = open("numbers.txt", "r")
number1 = int(NUMBER.readline())
number2 = int(NUMBER.readline())
NUMBER.close()
print(number1 + number2)
#Q4
NUMBER = open("numbers.txt", "r")
total = 0
for line in NUMBER:
    number = int(line)
    total += number
NUMBER.close()
print(total)