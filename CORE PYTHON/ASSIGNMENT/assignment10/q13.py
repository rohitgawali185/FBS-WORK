numbers = [10, 15, 22, 33, 40, 51, 64, 77]

new_list = []

for j in numbers:
    if j % 2 != 0:
        new_list = new_list + [j]

print("Original List:", numbers)
print("List after removing even numbers:", new_list)