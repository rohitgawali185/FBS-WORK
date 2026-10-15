class Teacher:
    def __init__(self, id, name, salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getSalary(self):
        return self.__salary

    def setSalary(self, salary):
        self.__salary = salary

    def display(self):
        print("ID:", self.__id,
              "Name:", self.__name,
              "Salary:", self.__salary)


t1 = Teacher(101, "Raj", 40000)
t2 = Teacher(102, "Amit", 45000)

t1.display()
t2.display()

t1.setSalary(50000)
t1.display()