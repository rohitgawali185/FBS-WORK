class Patient:
    def __init__(self, id, name, age):
        self.__id = id
        self.__name = name
        self.__age = age

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def display(self):
        print("ID:", self.__id,
              "Name:", self.__name,
              "Age:", self.__age)


p1 = Patient(101, "Rohit", 22)
p2 = Patient(102, "Amit", 25)

p1.display()
p2.display()

p1.setAge(23)
p1.display()