text = input("Enter a string: ")

words = len(text.split())
characters = 0

for char in text:
    characters += 1

print("Number of words:", words)
print("Number of characters:", characters)