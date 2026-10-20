numbers = [1, 2, 3, 4, 5]

square_list = []
cube_list = []

for j in numbers:
    square = j * j
    cube = j * j * j

    square_list = square_list + [square]
    cube_list = cube_list + [cube]

print("Numbers List:", numbers)
print("Squares List:", square_list)
print("Cubes List:", cube_list)