class Mobile:
    def __init__(self, id, model, price):
        self.__id = id
        self.__model = model
        self.__price = price

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getModel(self):
        return self.__model

    def setModel(self, model):
        self.__model = model

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def display(self):
        print("ID:", self.__id,
              "Model:", self.__model,
              "Price:", self.__price)


m1 = Mobile(101, "Samsung", 25000)
m2 = Mobile(102, "iPhone", 60000)

m1.display()
m2.display()

m1.setPrice(27000)
m1.display()