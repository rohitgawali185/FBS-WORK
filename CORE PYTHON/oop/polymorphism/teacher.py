class teacher:
    def __init__(self,name,subject,sal):
        self.name=name
        self.subject=subject
        self.sal=sal


    def getName(self):
            return self.name   
    def setName(self,newid):
            self.name = newid

    def getSubject(self):
            return self.subject
    def setSunject(self,newid):
            self.subject=newid

    def getSal(self):
           return self.sal
    def setSal(self,newid):
           self.sal=newid

    def display(self):
      print(f"Name={self.name}\t subject={self.subject}\tSal={self.sal}")


#teacher end here.....

class Professor(teacher):
    def __init__(self,name,subject, sal,exp):
      super().__init__(name,subject, sal)
      self.exp=exp


    def getExp(self):
          return self.exp
    def setExp(self,nexp):
          self.exp=nexp

    def display(self):
          print(f"Name={self.name}\t subject={self.subject}\tSal={self.sal}\tExperience={self.exp}\t")
          super().display 

#professor class end here...


class Founder(teacher):
      def __init__(self, name, subject, sal,fees):
            super().__init__(name, subject, sal)
            self.fees=fees
      def getFees(self):
            return self.fees 
      def setFees(self,nfees):
            self.fees=nfees

      def display(self):
            print(f"Name={self.name}\t subject={self.subject}\tSal={self.sal}\tFees={self.fees}\t")
            super().display
            
t1=teacher("kunal","python",454540)
p1=Professor("rohit","java",1234567,5)
f1=Founder("tejas","oop",150,56000)

t1.display()
p1.display()
f1.display()
