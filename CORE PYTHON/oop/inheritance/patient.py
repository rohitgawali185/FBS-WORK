class Patient:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

    def getid(self):
        return self.id
    def setid(self,newid):
        self.id=newid

    def getname(self):
        return self.name
    def setname(self,nname):
        self.name=nname

    def getname(self):
        return self.age
    def setname(self,nage):
        self.age=nage

    def display(self):
        print(f"ID={self.id}\tNAME={self.name}\tAGE={self.age}")

#patient class end here 


class Denatlpatient(Patient):
    def __init__(self, id, name, age,doctorname):
        super().__init__(id, name, age)
        self.doctorname=doctorname

    def getdoctorname(self):
        return self.doctorname
    def setdoctorname(self,ndoctorname):
        self.doctorname=ndoctorname

    def display(self):
        print(f"ID={self.id}\tNAME={self.name}\tAGE={self.age}\tDoctorname={self.doctorname}")
        
# Denatlpatient class end here 



class Childpatient(Patient):
    def __init__(self, id, name, age,schoolname):
        super().__init__(id, name, age)
        self.schoolname=schoolname

    def getschoolname(self):
        return self.schoolname
    def setschoolname(self,nschoolname):
        self.schoolname=nschoolname

    def display(self):
        print(f"ID={self.id}\tNAME={self.name}\tAGE={self.age}\tSchoolname={self.schoolname}")
        


#Child patient end here ... 



P1=Patient(1,"tejas",21)
D1=Denatlpatient(2,"Shekhar",23,"DR:Vaibhav")
C1=Childpatient(3,"kunal",14,"nvp")

P1.display()
D1.display()
C1.display()