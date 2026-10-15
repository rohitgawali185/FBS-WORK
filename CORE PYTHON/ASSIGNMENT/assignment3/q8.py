import random

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":

    num = random.randint(1000, 9999)
    print("Your number is:", num)

    user_num = int(input("Enter same number: "))

    if user_num == num:
        print("Success")
    else:
        print("Failed")

else:
    print("Invalid User ID or Password")