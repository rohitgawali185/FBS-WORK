P = float(input("Enter Principal: "))
T = float(input("Enter Time: "))
R = float(input("Enter Rate: "))

amount = P * (1 + R / 100) ** T
CI = amount - P

print("Compound Interest:", CI)