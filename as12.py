
units = float(input("Enter electricity units consumed: "))


if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = 25 + (units - 50) * 0.75
elif units <= 250:
    bill = 100 + (units - 150) * 1.20
else:
    bill = 220 + (units - 250) * 1.50


surcharge = 0.2 * bill
total_bill = bill + surcharge


print("Electricity Units Consumed:", units)
print("Electricity Bill:", bill)
print("Surcharge:", surcharge)
print("Total Bill:", total_bill)
