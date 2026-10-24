numbers = [2, 4, 3, 5, 7, 8, 1]
target = 9

pairs = set()

for j in range(len(numbers)):
    for k in range(j + 1, len(numbers)):
        if numbers[j] + numbers[k] == target:
            pairs.add((numbers[j], numbers[k]))

print("Numbers:", numbers)
print("Target Sum:", target)
print("Pairs:", pairs)