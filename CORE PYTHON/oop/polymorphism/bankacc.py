class Bankaccount:
    def __init__(self,acc,name, bal):
        self.acc=acc
        self.name=name
        self.bal=bal


    def getacc(self):
        return self.acc
    def setacc(self,newid):
        self.acc=newid


    def getname(self):
        return self.name
    def setname(self,newid):
        self.name=newid

    def getbal(self):
        return self.bal
    def setbal(self,newid):
        self.bal=newid

    def calBal(self):
        print(f"final balance of {self.bal} ")
    def display(self):
        print(f"Account={self.acc}\t Name={self.name}\tBalance={self.bal}")

#BankAccount end here 

class Savingaccount(Bankaccount):
    def __init__(self, acc, name, bal,interest):
        super().__init__(acc, name, bal)
        self.interest=interest

    def getinterest(self):
        return self.interest
    def setinterest(self,ninterest):
        self.interest=ninterest
    def calBal(self):
            print(f"final balance of {self.bal+self.interest} ")
    def display(self):
        print(f"Account={self.acc}\t Name={self.name}\tBalance={self.bal}\tInetrest={self.interest}")
        
#Savingaccount end here 


class CurrentAccount(Bankaccount):
    def __init__(self, acc, name, bal,businessname):
        super().__init__(acc, name, bal)
        self.businessname=businessname


    def getbusinessname(self):
        return self.businessname
    def setbusinessname (self,nbusinessname):
        self.businessname=nbusinessname

    def display(self):
     print(f"Account={self.acc}\tName={self.name}\tBalance={self.bal}\tBusinessName={self.businessname}\t")
     
#CurrentAccount end here ...


B1=Bankaccount(123,"rohit",70809089)
S1=Savingaccount( 234,"kunal",567897,12 )
C1=CurrentAccount(345,"vaibhav",123445678,"harvestmachine")

S1.calBal()
B1.calBal()

