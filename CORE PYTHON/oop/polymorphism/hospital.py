class Hospital:
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee

    def display(self):
        print(f"Doctor={self.name}\tFee={self.fee}")


class Doctor(Hospital):
    def __init__(self, name, fee, bonus):
        super().__init__(name, fee)
        self.bonus = bonus

    def getBonus(self):
        return self.bonus

    def setBonus(self, nbonus):
        self.bonus = nbonus

    def calFee(self):
        print(f"Final Fee = {self.fee + self.bonus}")


h1 = Hospital("Dr. Rahul", 500)
d1 = Doctor("Dr. Amit", 1000, 200)

h1.display()
d1.calFee()