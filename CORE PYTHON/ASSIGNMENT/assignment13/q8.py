text = input("Enter a string: ")

words = text.lower().split()
frequency = {}

for j in words:
    if j in frequency:
        frequency[j] = frequency[j] + 1
    else:
        frequency[j] = 1

print("Word Frequency:", frequency)