text = input("Enter a string: ")
result = ""

for char in text:
    if char == " ":
        result += "-"
    else:
        result += char

print("Modified string:", result)