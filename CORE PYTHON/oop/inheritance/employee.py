class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

    def getid(self):
         return(self.id)
    def setid(self,nid):
         self.id=nid

    def getname(self):
         return(self.name)
    def setname(self,nname):
         self.name=nname 
         

    def calSal(self):
         print(f"final sal of employee{self.sal}")
              
    def display(self):
      print(f"ID={self.id}\tName={self.name}\tSal={self.sal}")

#Empolyee end here........................

class Hr(Employee):
    def __init__(self, id, name, sal,com):
         super().__init__(id, name, sal)
         self.com=com
    def getCom(self):
         return self.com
    def setCom(self,ncom):
         self.com=ncom
    def calSal(self):
         print(f"final sal of HR{self.sal+self.com}")
    def display(self):
         
         print(f"ID={self.id}\tName={self.name}\tSal={self.sal}\tCom={self.com}")
         super().display

  #class Hr ends here...............            
class devloper(Employee):
    def __init__(self, id, name, sal,bonus):
         super().__init__(id, name, sal)
         self.bonus=bonus
    def getbonus(self):
         return self.bonus
    def setbouns(self,nbouns):
         self.bonus=nbouns
    def calSal(self):
         print(f"final sal of DEVELOPER{self.sal+self.bonus}")
         
    def display(self):
         
         print(f"ID={self.id}\tName={self.name}\tSal={self.sal}\tBonus={self.bonus}")
         super().display

   #classs devloper ends here 

e1=Employee(1,"rahul",3333)
h1=Hr(7,"harman",8438,1500)
d1=devloper(63,"surya",8956,563)
d1.calSal()
h1.calSal()
e1.calSal()