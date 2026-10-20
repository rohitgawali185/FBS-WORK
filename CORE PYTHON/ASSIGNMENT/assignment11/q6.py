list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Method 1: Using set operations
union_list = list(set(list1).union(set(list2)))

print("Union of Lists:", sorted(union_list))