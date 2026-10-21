student = {
    "name": "Rohit",
    "age": 21,
    "city": "Pune",
    "course": "Python"
}

key = input("Enter key to remove: ")

if key in student:
    del student[key]
    print("Updated Dictionary:", student)
else:
    print("Key not found in dictionary.")