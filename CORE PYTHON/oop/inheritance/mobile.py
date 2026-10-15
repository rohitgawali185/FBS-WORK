class Mobile:
    def __init__(self,name,com,ver):
        self.name=name
        self.com=com
        self.ver=ver

    def getname(self):
        return self.name
    def setname(self,newid):
        self.name=newid

    def getcom(self):
        return self.com
    def setcom(self,newid):
        self.com=newid

    def getver(self):
        return self.ver
    def setver(self,newid):
        self.ver=newid

    def display(self):
        print(f"Name={self.name}\tCompany={self.com}\tVersion={self.ver}")

#mobile class end here...


class Iphone(Mobile):
    def __init__(self, name, com, ver,model):
        super().__init__(name, com, ver)
        self.model=model

    def getmodel(self):
        return self.model
    def setmodel(self,nmodel):
        self.model=nmodel

    def display(self):
       print(f"Name={self.name}\tCompany={self.com}\tVersion={self.ver}\tModel={self.model}")
       
#iphone class end here 

class Android(Mobile):
    def __init__(self, name, com, ver,bat):
        super().__init__(name, com, ver)
        self.bat=bat

    def getbat(self):
        return self.bat
    def setbat(self,nbat):
        self.bat=nbat

    def display(self):
        print(f"Name={self.name}\tCompany={self.com}\tVersion={self.ver}\tBattery={self.bat}")
        



# android class end here...

M1=Mobile("TY","nokia",12)
I1=Iphone("iphonepro","Apple","ios",2016)
A1=Android("S25","Samsung",26,7000)

M1.display()
I1.display()
A1.display()
