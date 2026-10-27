class Product:
    def __init__(self, pid=None, pname=None, price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def ShowBook(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Product Price:", self.price)
        print("Product Quantity:", self.quantity)

    def __del__(self):
        print("Product object destroyed")


# Parameterless constructor
p1 = Product()
print("Product 1 Details:")
p1.ShowBook()

print()

# Parameterized constructor
p2 = Product(101, "Laptop", 50000, 2)
print("Product 2 Details:")
p2.ShowBook()