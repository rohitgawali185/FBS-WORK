text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

count1 = 0
count2 = 0

for char in text1:
    count1 += 1

for char in text2:
    count2 += 1

if count1 > count2:
    print("Larger string:", text1)
elif count2 > count1:
    print("Larger string:", text2)
else:
    print("Both strings have equal length")