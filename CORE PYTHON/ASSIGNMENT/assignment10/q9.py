numbers = [10, 15, 22, 33, 40, 51, 64, 77]

even_list = []
odd_list = []

for j in numbers:
    if j % 2 == 0:
        even_list = even_list + [j]
    else:
        odd_list = odd_list + [j]

print("Original List:", numbers)
print("Even Numbers:", even_list)
print("Odd Numbers:", odd_list)