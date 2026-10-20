list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Method 1: Using set operations
intersection_list = list(set(list1).intersection(set(list2)))

print("Intersection of Lists:", sorted(intersection_list))