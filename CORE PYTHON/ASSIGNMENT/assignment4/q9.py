start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
num = int(input("Enter number: "))

for i in range(start, end + 1):
    if i % num == 0:
        print(i)