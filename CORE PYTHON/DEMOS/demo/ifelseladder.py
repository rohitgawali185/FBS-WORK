"""If-elif-else ladder is used to check multiple conditions
one by one and execute the block of the first True condition.
 Marathi Meaning :=
जेव्हा आपल्याला एकापेक्षा जास्त conditions check करायच्या असतात,
 तेव्हा if-elif-else ladder वापरतो."""

#syntax 
"""if condition1:
    statement
elif condition2:
    statement
elif condition3:
    statement
else:
    statement"""



num=int(input('enter number:'))
if(num==0):
    print('the number is neutral.')
elif(num>0):
    print('the number is positive.')
else:
    print('the number is negative.')
