text = input("Enter a string: ")
result = ""

for j in range(len(text)):
    if j % 2 == 0:
        result += text[j]
print("Modified string:", result)