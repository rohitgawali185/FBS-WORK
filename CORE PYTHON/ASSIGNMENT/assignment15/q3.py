class Shirt:
    def __init__(
        self, sid=None, sname=None,
        type=None, price=0, size=None
    ):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Shirt Type:", self.type)
        print("Shirt Price:", self.price)
        print("Shirt Size:", self.size)

    def __del__(self):
        print("Shirt object destroyed")


# Parameterless constructor
s1 = Shirt()
print("Shirt 1 Details:")
s1.ShowBook()

print()

# Parameterized constructor
s2 = Shirt(101, "Cotton Shirt", "Formal", 1200, "Large")
print("Shirt 2 Details:")
s2.ShowBook()