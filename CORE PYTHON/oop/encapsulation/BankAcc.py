class BankAccount:
    def __init__(self, accno, name, balance):
        self.__accno = accno
        self.__name = name
        self.__balance = balance

    def getAccno(self):
        return self.__accno

    def setAccno(self, accno):
        self.__accno = accno

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def display(self):
        print("Account No:", self.__accno,
              "Name:", self.__name,
              "Balance:", self.__balance)


a1 = BankAccount(101, "Rohit", 50000)
a2 = BankAccount(102, "Amit", 60000)

a1.display()
a2.display()

a1.setBalance(70000)
a1.display()