#6. Remove duplicates from a list while preserving the order of elements.
list1=[1,3,89,7,4,3,1,5]
print("Original list is:",list1)
without_dup=list(set(list1))
print('List after removing duplicates:',without_dup)