numbers = list(range(1, 11))

squares = [num**2 for num in numbers]
cubes = [num**3 for num in numbers]

print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:  ", cubes)

# Alternatively, formatted in a single structure:
pattern_data = [[num, num**2, num**3] for num in numbers]
print("\nNumber | Square | Cube")
print("-" * 22)
for num, sq, cb in pattern_data:
    print(f"{num:<6} | {sq:<6} | {cb:<4}")