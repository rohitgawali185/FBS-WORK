class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price 

    def getid(self):
        return self.id
    def setid(self,newid):
        self.id=newid

    def getname(self):
            return self.name
    def setname(self,newname):
            self.name=newname

    def getprice(self):
            return self.price
    def setprice(self,newprice):
            self.price=newprice

    def display(self):
          print(f"ID={self.id}\tNAME={self.name}\tPRICE={self.price}")


# prodect class end here 

class Electronic(Product):
      def __init__(self, id, name, price,brand):
            super().__init__(id, name, price)
            self.brand=brand

      def getbrand(self):
              return self.brand
      def setid(self,newbrand):
              self.brand=newbrand

      def display(self):
            print(f"ID={self.id}\tNAME={self.name}\tPRICE={self.price}\tBRAND={self.brand}")


#electronic class end here ..


class Mobile(Product):
      def __init__(self, id, name, price,ram):
            super().__init__(id, name, price)
            self.ram=ram 
      def getram(self):
                    return self.ram
      def setram(self,newram):
                    self.ram=newram

      def display(self):
             print(f"ID={self.id}\tNAME={self.name}\tPRICE={self.price}\tRAM={self.ram}")

P1=Product(12,"as",67888)
E1=Electronic(23,"fridge",15000,"lG")
M1=Mobile(34,"iphone",164000,16)

P1.display()
E1.display()
M1.display()
    
            
    

    