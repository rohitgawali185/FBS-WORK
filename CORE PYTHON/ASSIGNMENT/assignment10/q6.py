numbers = [10, 20, 10, 30, 20, 40, 50, 30]

unique_list = []

for j in numbers:
    found = False

    for k in unique_list:
        if j == k:
            found = True
            break

    if found == False:
        unique_list = unique_list + [j]

print("Original List:", numbers)
print("List after removing duplicates:", unique_list)