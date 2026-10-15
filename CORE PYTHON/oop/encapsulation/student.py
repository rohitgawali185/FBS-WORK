class Student:
    stCount=0
    def __init__(self,frn,name,bname):
        self.frn=frn
        self.name=name
        self.batch=bname
        Student.stCount+=1
    def display(self):
      print(f"Frn={self.frn}\tNAme={self.name}\tBatch={self.batch}")

      #Employee end here............................

class PlaceStudent(Student):
   def __init__(self, frn, name, bname,cName):
      super().__init__(frn, name, bname)
      self.cName=cName
      def setCame(self,cName):
         self.cName=cName
      def getCname(self,cName):
         return self.cName
      def display(self):
         print(f"cNAme={self.c}")
         super().display
s1=Student(12,"Garav","April")  
s2=Student(1,"Atrav","july/aug")     
s3=Student(53,"ruika","july/aug")  
s4=PlaceStudent(37,"shivraj","july/aug","tcs")  
s5=PlaceStudent(37,"shivraj","july/aug","one8") 
print(Student.stCount)