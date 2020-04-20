"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

#Question 1

sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 0.1
    print("Bonus is $",bonus)
else:
    bonus = sales * 0.15
    print("Bonus is $",bonus)

#Question 2

sales = float(input("Enter sales: $"))
while sales >= 0:
   if sales < 1000:
       bonus = sales * 0.1
       print("Bonus is $", bonus)
   else:
       bonus = sales * 0.15
       print("Bonus is $", bonus)
   sales = float(input("Enter sales: $"))
else:
    print("Negative number is invalid sales")