class Employee():
    def _init_(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def display(self):
        print(f"ID = {self.id}\tName = {self.name}\tSalary = {self.sal}")



e1 = Employee(101, "Rahul", 25000)
e2 = Employee(102, "Amit", 30000)
e3 = Employee(103, "Rohit", 35000)

employees = [e1, e2, e3]

for e in employees:e.display()