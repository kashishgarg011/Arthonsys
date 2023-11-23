#14. Find the intersection of two lists (common elements)
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = []
for value in list1:
    if value in list2:
        result.append(value)
print("Intersection of the two lists:",result)
