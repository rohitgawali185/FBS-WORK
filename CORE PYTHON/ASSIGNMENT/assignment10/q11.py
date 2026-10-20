numbers = [12, 15, 20, 24, 30, 36, 40, 60]

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

print("Numbers divisible by both m and n:")

for j in numbers:
    if j % m == 0 and j % n == 0:
        print(j)