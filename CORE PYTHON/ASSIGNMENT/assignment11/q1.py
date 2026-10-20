numbers = [12, 7, 19, 24, 33, 40, 55, 62]

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Original List:", numbers)
print("Even List:", even_list)
print("Odd List:", odd_list)