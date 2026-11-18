
class Book:
    count = 0

    def __init__(self, bid=0, bname="Not Available",
                 price=0.0, author="Not Available"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

        Book.count += 1

    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)
        print("-" * 30)

    def __del__(self):
        print("Book object destroyed:", self.bid)


# Parameterless constructor
b1 = Book()

# Parameterized constructor
b2 = Book(101, "Python Programming", 500, "Guido")

b1.ShowBook()
b2.ShowBook()

print("Total objects created:", Book.count)
