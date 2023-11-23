#18. Rotate elements in a list by a specified number of positions.
list1=[11,92,34,54,59,68]
print('Original list:',list1)
pos=int(input('Enter position where you want to rotate:'))
list1=list1[pos:]+list1[:pos]
print('Output of list after left rotate by',pos,list1)
list1=list1[-pos:]+list1[:-pos]
print('Output of list after right rotate by',pos,'back to original list',list1)