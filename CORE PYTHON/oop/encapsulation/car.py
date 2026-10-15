class Car:
    def __init__(self, no, brand, price):
        self.__no = no
        self.__brand = brand
        self.__price = price

    def getNo(self):
        return self.__no

    def setNo(self, no):
        self.__no = no

    def getBrand(self):
        return self.__brand

    def setBrand(self, brand):
        self.__brand = brand

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def display(self):
        print("No:", self.__no, "Brand:", self.__brand, "Price:", self.__price)


c1 = Car(1, "Toyota", 800000)
c2 = Car(2, "Honda", 900000)

c1.display()
c2.display()

c1.setPrice(850000)
c1.display()