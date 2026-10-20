numbers = [45, 12, 89, 33, 67, 23]
n = len(numbers)

# Bubble Sort
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted List:", numbers)
print("Second Largest Number:", numbers[-2])