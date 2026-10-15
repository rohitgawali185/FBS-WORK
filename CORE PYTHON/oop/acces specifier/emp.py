class Emp:
    def __init__(self,id,name,sal):
        self.__id=id
        self.__name=name
        self.__sal=sal

    def getid(self):
        return self.__id
    def setid(self,nid):
        self.__id=nid
        def __str__(self):
            return f"Id={self.__id}Name={self.__name}sal={self.__sal}"
class Hr (Emp):
    def __str__(self):
        print(self.__id)
        return super().__str__()
e1=Emp(12,"RG",45677)
print(e1.getid)
e1.setId(19)
print(e1.getid)
h1=Hr(1,"KS",150)
