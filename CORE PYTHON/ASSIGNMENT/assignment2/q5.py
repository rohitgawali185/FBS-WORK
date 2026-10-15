cost_price = float(input("Enter cost price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = cost_price * discount / 100
selling_price = cost_price - discount_amount

print("Selling Price:", selling_price)