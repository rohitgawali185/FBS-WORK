numbers = [10, 15, 22, 33, 40, 55, 60, 71, 84, 99]

# Keep only odd numbers
filtered_list = [num for num in numbers if num % 2 != 0]

print("Original List:", numbers)
print("List after removing even numbers:", filtered_list)