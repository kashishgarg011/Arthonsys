#DICTIONARY

#clear()
my_dict = {'Name': 'Kashish', 'Roll_no': 4, 'Age': 22}
my_dict.clear()
print(my_dict)


#get()
d ={'Name': 'Kashish', 'Roll_no': 4, 'Age': 22}
print(d.get('Name'))
print(d.get('Age'))


#items()
d1={'Name': 'Kashish', 'Roll_no': 4, 'Age': 22}
print(d1.items())
print(list(d1.items())[2][0])


#keys()
d ={'Name': 'Kashish', 'Roll_no': 4, 'Age': 22}
print(d.keys())


#values()
d ={'Name': 'Kashish', 'Roll_no': 4, 'Age': 22}
print(d.values())


#update
d3 ={'Name': 'Kashish', 'Roll_no': 4, 'Age': 22}
d4= {'Name': 'Kratika', 'Age': 23}
d3.update(d4)
print(d3)


#pop()
d5 ={'Name': 'Kashish', 'Roll_no': 4, 'Age': 22}
d5.pop('Age')
print(d5)


#popitem()
d6={'Name': 'Kashish', 'Roll_no': 4, 'Age': 22}
d6.popitem()
print(d6)

d6.popitem()
print(d6)