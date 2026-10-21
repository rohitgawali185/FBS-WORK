student = {
    "name": "Rohit",
    "age": 21,
    "city": "Pune"
}

key = input("Enter key to search: ")

if key in student:
    print("Key exists in dictionary.")
else:
    print("Key does not exist in dictionary.")