numbers = [2, 3, 4, 5, 6]

cube_list = []

for j in numbers:
    cube = j * j * j
    cube_list = cube_list + [cube]

print("Original List:", numbers)
print("Cube List:", cube_list)