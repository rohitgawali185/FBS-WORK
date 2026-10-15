feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

total_inches = (feet * 12) + inches
centimeter = total_inches * 2.54
meter = centimeter / 100

print("Meter:", meter)
print("Centimeter:", centimeter)