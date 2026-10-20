numbers = [10, 20, 30, 40, 50]

reverse_list = []

j = len(numbers) - 1

while j >= 0:
    reverse_list = reverse_list + [numbers[j]]
    j = j - 1

print("Original List:", numbers)
print("Reversed List:", reverse_list)