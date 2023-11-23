#16. Check if all elements in a list are unique.
list1= [10, 22, 23, 13, 42, 5,22,7]
result= len(list1) == len(set(list1))
print("List has unique elements:", result)