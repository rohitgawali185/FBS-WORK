
class Shirt:
    size_percentage = {
        "small": 0,
        "medium": 10,
        "large": 20,
        "xlarge": 30
    }

    def __init__(self, sid=0, sname="Not Available",
                 type="Casual", price=0.0, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size.lower()

    def calculate_price(self):
        percentage = Shirt.size_percentage.get(self.size, 0)
        return self.price + (self.price * percentage / 100)

    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Size:", self.size.capitalize())
        print("Base Price:", self.price)
        print("Final Price:", self.calculate_price())
        print("-" * 30)

    def __del__(self):
        print("Shirt object destroyed:", self.sid)


# Parameterless constructor
s1 = Shirt()

# Parameterized constructors
s2 = Shirt(101, "Cotton Shirt", "Formal", 1000, "small")
s3 = Shirt(102, "Cotton Shirt", "Formal", 1000, "medium")
s4 = Shirt(103, "Cotton Shirt", "Formal", 1000, "large")
s5 = Shirt(104, "Cotton Shirt", "Formal", 1000, "xlarge")

# Display shirt details
s1.ShowBook()
s2.ShowBook()
s3.ShowBook()
s4.ShowBook()
s5.ShowBook()
