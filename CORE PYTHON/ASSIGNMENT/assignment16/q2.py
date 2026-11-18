
class Product:
    discount = 10  # Static discount in percentage

    def __init__(self, pid=0, pname="Not Available",
                 price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def apply_discount(self):
        discount_amount = self.price * Product.discount / 100
        self.price = self.price - discount_amount

    def ShowBook(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("-" * 30)

    def __del__(self):
        print("Product object destroyed:", self.pid)


# Parameterless constructor
p1 = Product()

# Parameterized constructor
p2 = Product(101, "Laptop", 50000, 2)

print("Before Discount:")
p2.ShowBook()

p2.apply_discount()

print("After Discount:")
p2.ShowBook()

p1.ShowBook()

print("Discount Percentage:", Product.discount, "%")
