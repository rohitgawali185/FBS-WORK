m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))
m4 = int(input("Enter marks 4: "))
m5 = int(input("Enter marks 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Percentage =", percentage)

if percentage >= 75:
    print("Distinction")
elif percentage >= 60:
    print("First Class")
elif percentage >= 50:
    print("Second Class")
elif percentage >= 35:
    print("Pass")
else:
    print("Fail")