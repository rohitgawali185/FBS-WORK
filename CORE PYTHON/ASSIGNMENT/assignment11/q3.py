# List of sublists
sublists = [[1, 5], [4, 2], [3, 9], [2, 1], [5, 4]]

# Sort using key parameter with lambda function
sublists.sort(key=lambda x: x[1])

print("Sorted List by 2nd element:", sublists)