numbers = [10, 20, 10, 30, 10, 40, 50]

number = int(input("Enter the element to remove: "))

new_list = []

for j in numbers:
    if j != number:
        new_list = new_list + [j]

print("Original List:", numbers)
print("List after removing element:", new_list)