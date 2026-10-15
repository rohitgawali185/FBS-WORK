# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# sum=num1+num2
# print(f"sum of num1 + num2:",sum)


# num1=float(input("enter first number:"))
# num2=float(input("enter second number:"))
# sum=num1+num2
# print(f"sum of num1 + num2:",sum)


# str1=input("enter first string:")
# str2=input("enter second string:")
# result=str1+str2
# print(f"result of str1+str2:",result)



# list1=[1,2,3]
# list2=[4,5,6]
# combine_list=list1+list2
# print(f"combine list:",combine_list)


# class Time:
#     def __init__(self,hr,min,sec):
#         self.hr=hr
#         self.min=min
#         self.sec=sec
#     def __str__(self):
#         return f"{self.hr}:{self.min}:{self.sec}"
#     def __add__(self, other):
#         thr=self.hr+other.hr
#         tmin=self.min+other.min
#         tsec=self.sec+other.sec
#         return Time(thr,tmin,tsec)
# t1=Time(12,33,47)
# t2=Time(7,33,56)
# print(t1+t2)


class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
    def __add__(self, other):
        
        tsec=self.sec+other.sec
        emin=tsec//60
        tsec=tsec%60
        tmin=self.min+other.min+emin
        ehr=tmin//60
        tmin=tmin//60
        thr=self.hr+other.hr+ehr
        return Time(thr,tmin,tsec)
t1=Time(12,33,47)
t2=Time(7,33,56)
print(t1+t2) 
