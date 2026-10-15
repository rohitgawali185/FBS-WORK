userid = "admin"
password = "1234"

for i in range(3):
    user = input("Enter User ID: ")
    pwd = input("Enter Password: ")

    if user == userid and pwd == password:
        print("Login Successful")
        break
    else:
        print("Invalid User ID or Password")

else:
    print("3 attempts completed. Program terminated.")