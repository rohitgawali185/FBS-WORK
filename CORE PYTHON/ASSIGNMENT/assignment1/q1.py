python = float(input("Enter Python marks: "))
java = float(input("Enter Java marks: "))
dbms = float(input("Enter DBMS marks: "))
web = float(input("Enter Web Development marks: "))
data_analytics = float(input("Enter Data Analytics marks: "))


total = python + java + dbms + web + data_analytics
percentage = total / 5


print("Total Marks:", total)
print("Percentage:", percentage)