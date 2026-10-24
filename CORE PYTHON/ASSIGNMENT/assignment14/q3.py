strings = [
    "python is easy",
    "python is powerful",
    "programming is fun"
]

words = []

for line in strings:
    words.extend(line.lower().split())

unique_words = set(words)

print("Unique Words:", unique_words)
print("Word Frequencies:")

for word in sorted(unique_words):
    print(word, ":", words.count(word))