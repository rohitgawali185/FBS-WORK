class Library:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Book={self.name}\tPrice={self.price}")


class Book(Library):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def getDiscount(self):
        return self.discount

    def setDiscount(self, ndiscount):
        self.discount = ndiscount

    def calPrice(self):
        print(f"Final Price = {self.price - self.discount}")


l1 = Library("Python", 500)
b1 = Book("Java", 800, 100)

l1.display()
b1.calPrice()