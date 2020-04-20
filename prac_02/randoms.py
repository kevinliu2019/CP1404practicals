import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# line 1, the smallest number is 5, the largest number is 20.
# line 2, the smallest number is 3, the largest number is 10.
# The line 2 can not produce the 4, because it start at 3, and step is 2. So, the next number is 5, not 4.
# line 3, the smallest number is 2.5, the largest number is 5.5.

print(random.uniform(1, 100))