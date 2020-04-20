#Q2
print("Electricity bill estimator")
power = float(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days: "))
total_bill = 0.01 * power * daily_use * days
print("Estimated bill: ${:.2f}".format(total_bill))

#Q3
print("Electricity bill estimator 2.0")
traiff_number = input("Which tariff? 11 or 31: ")
daily_use = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days: "))
if traiff_number == "11":
    total_bill = 0.244618 * daily_use * days
elif traiff_number == "31":
    total_bill = 0.136928 * daily_use * days
else:
    False
print("Estimated bill: ${:.2f}".format(total_bill))

