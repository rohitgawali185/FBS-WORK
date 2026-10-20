numbers = [10, 20, 10, 30, 10, 40, 50]

number = int(input("Enter a number to search: "))

count = 0

for j in numbers:
    if j == number:
        count = count + 1

if count > 0:
    print("Element is present in the list")
    print("Number of occurrences:", count)
else:
    print("Element is not present in the list")