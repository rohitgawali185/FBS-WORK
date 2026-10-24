from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = defaultdict(list)

for word in words:
    key = "".join(sorted(word))
    groups[key].append(word)

result = list(groups.values())

print("Original Words:", words)
print("Grouped Anagrams:")

for group in result:
    print(group)