def rectangle(length, breadth):
    area = length * breadth
    return area


length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

print("Area of Rectangle =", rectangle(length, breadth))