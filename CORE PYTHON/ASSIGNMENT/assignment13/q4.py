n = int(input("Enter the value of n: "))

square_dict = {}

for j in range(1, n + 1):
    square_dict[j] = j * j

print("Dictionary:", square_dict)