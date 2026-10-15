passengers = int(input("Enter number of passengers: "))
ticket = float(input("Enter ticket cost: "))

total = 0

for i in range(passengers):
    age = int(input("Enter age: "))

    if age < 12:
        amount = ticket - (ticket * 30 / 100)
    elif age > 59:
        amount = ticket - (ticket * 50 / 100)
    else:
        amount = ticket

    total = total + amount

print("Total Ticket Amount =", total)