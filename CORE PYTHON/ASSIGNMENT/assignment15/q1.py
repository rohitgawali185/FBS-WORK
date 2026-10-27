class Book:
    def __init__(self, bid=None, bname=None, price=0, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Book Price:", self.price)
        print("Book Author:", self.author)

    def __del__(self):
        print("Book object destroyed")


# Parameterless constructor
b1 = Book()
print("Book 1 Details:")
b1.ShowBook()

print()

# Parameterized constructor
b2 = Book(101, "Python Programming", 450, "Guido van Rossum")
print("Book 2 Details:")
b2.ShowBook()