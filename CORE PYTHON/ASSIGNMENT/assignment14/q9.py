numbers = [1, 2, 3, 4, 5, 6, 7]
target = 12

combinations = set()

for j in range(len(numbers)):
    for k in range(j + 1, len(numbers)):
        for m in range(k + 1, len(numbers)):
            if numbers[j] + numbers[k] + numbers[m] == target:
                combination = tuple(sorted((
                    numbers[j], numbers[k], numbers[m]
                )))
                combinations.add(combination)

print("Numbers:", numbers)
print("Target:", target)
print("Unique Combinations:")

for combination in sorted(combinations):
    print(combination)