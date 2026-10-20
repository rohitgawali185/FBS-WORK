numbers = [25, 10, 45, 5, 30]

maximum = numbers[0]
minimum = numbers[0]

for j in numbers:
    if j > maximum:
        maximum = j

    if j < minimum:
        minimum = j

print("List:", numbers)
print("Maximum element:", maximum)
print("Minimum element:", minimum)