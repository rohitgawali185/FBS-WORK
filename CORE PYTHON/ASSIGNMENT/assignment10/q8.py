numbers = [10, 20, 30, 40, 50]

duplicate_list = []

for j in numbers:
    duplicate_list = duplicate_list + [j]

print("Original List:", numbers)
print("Duplicate List:", duplicate_list)

duplicate_list[0] = 100

print("After modifying duplicate list:")
print("Original List:", numbers)
print("Duplicate List:", duplicate_list)