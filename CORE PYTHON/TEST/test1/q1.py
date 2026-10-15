length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

rectangle_area = length * breadth
rectangle_perimeter = 2 * (length + breadth)

circle_area = 3.14 * radius * radius
circle_perimeter = 2 * 3.14 * radius

print("Area of Rectangle =", rectangle_area)
print("Perimeter of Rectangle =", rectangle_perimeter)

print("Area of Circle =", circle_area)
print("Perimeter of Circle =", circle_perimeter)