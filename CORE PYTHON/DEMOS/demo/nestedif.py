

""""Nested if means an if statement
 inside another if statement. It is used to check another
 condition only when the first condition is true."""


gender = input("Enter your gender (Female/Male): ")
age = int(input("Enter your age: "))

if gender == "Female":
    if age >= 18:
        print("Girl is Eligible for marriage")
    else:
        print(" pehle padai karo")

else:
    if gender == "Male":
        if age >= 21:
            print(" Boy is Eligible for marriage")
        else:
            print("adhi kaam shodh")