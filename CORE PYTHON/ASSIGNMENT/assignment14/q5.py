strings = ["flower", "flow", "flight"]

common_prefix = ""

for j in range(min(len(word) for word in strings)):
    characters = set(word[j] for word in strings)

    if len(characters) == 1:
        common_prefix += strings[0][j]
    else:
        break

print("Strings:", strings)
print("Longest Common Prefix:", common_prefix)