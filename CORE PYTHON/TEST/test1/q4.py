area = float(input("Enter area of one wall: "))
interior_cost = float(input("Enter interior painting cost per sq.ft: "))
exterior_cost = float(input("Enter exterior painting cost per sq.ft: "))

total_area = area * 6

interior_total = total_area * interior_cost
exterior_total = total_area * exterior_cost

total_cost = interior_total + exterior_total

print("Total Interior Cost =", interior_total)
print("Total Exterior Cost =", exterior_total)
print("Total Painting Cost =", total_cost)