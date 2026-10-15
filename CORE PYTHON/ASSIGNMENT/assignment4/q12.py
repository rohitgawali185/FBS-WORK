n = int(input("Enter number: "))

temp = n
sum = 0
digits = len(str(n))

while n > 0:
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10

if sum == temp:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")