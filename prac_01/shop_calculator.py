number_of_items = int(input("Number of items:"))
total_price = 0
while number_of_items < 0:
    print("Invaild number of items.")
    number_of_items = int(input("Number of items:"))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: " ))
    total_price += price_of_item
if total_price > 100:
    total_price = total_price * (1 - 0.1)
    print("Total price for {} items is ${:.2f}".format(number_of_items,total_price))
else:
    print("Total price for {} items is ${:.2f}".format(number_of_items,total_price))
