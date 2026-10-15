"""even number

for  i in range(100):
    if i % 2 == 0:
         print(i)
"""


"""odd number
for  i in range(100):
    if i % 2 != 0:
         print(i)
"""

"""square 
for  i in range(1,11):
          print(f"{i}={i*i}")
"""



"""cube
for  i in range(1,100):
          print(f"{i}={i*i*i}")


          """


"""multiplication table
n=int(input("enter your number:"))
for i in range (1,11):
    print(f"{n}*{i}={i*n}")
    """

"""for i in range (3,100,3):

    if i<11:
         print(i)
         i+=1"""
for i in range(1,6,-1):
    for j in range(1,i+1):
        print('j',end ='')
        print()