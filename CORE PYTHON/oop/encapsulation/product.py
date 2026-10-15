class Product:
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def display(self):
        print("ID:", self.__id, "Name:", self.__name, "Price:", self.__price)


p1 = Product(101, "Laptop", 50000)
p2 = Product(102, "Mobile", 25000)

p1.display()
p2.display()

p1.setPrice(55000)
p1.display()