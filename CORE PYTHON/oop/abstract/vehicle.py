from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, cNo, color):
        self.cno = cNo
        self.color = color

    def getCno(self):
        return self.cno

    def setCno(self, newno):
        self.cno = newno

    def getColor(self):
        return self.color

    def setCol(self, nCol):
        self.color = nCol

    @abstractmethod
    def brake(self):
        pass

    def __str__(self):
        return f"Car No = {self.cno}, Color = {self.color}"


class Car(Vehicle):

    def brake(self):
        print("This is the Brake of Car")


# Store Vehicle objects in a list
vehicles = []

c1 = Car(12, "White")
c2 = Car(13, "Black")
c3 = Car(14, "Red")

vehicles.append(c1)
vehicles.append(c2)
vehicles.append(c3)

# Display all Vehicle objects
for v in vehicles:
    print(v)
    v.brake()