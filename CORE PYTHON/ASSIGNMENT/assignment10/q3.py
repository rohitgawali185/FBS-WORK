numbers = [10, 50, 30, 40, 20]

largest = numbers[0]
second_largest = None

for j in numbers:
    if j > largest:
        second_largest = largest
        largest = j
    elif j != largest:
        if second_largest is None or j > second_largest:
            second_largest = j

print("List:", numbers)
print("Second largest element:", second_largest)