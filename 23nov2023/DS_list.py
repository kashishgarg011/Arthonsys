#LIST

#append()
list1= ['Kashish', 'Garg', 19, 2000]
list1.append(11)
print(list1)


#insert()
list2=['Kashish','Garg',19,2000]
list2.insert(2,"nov")
print(list2)

#extend()
list11=[1, 2, 3]
list22=[2, 3, 4, 5]
list11.extend(list22)
print(list11)
list22.extend(list11)
print(list22)


#sum()
list3=[11, 72, 30, 14, 25]
print(sum(list3))


#count()
list4= [10, 52, 3, 10, 27, 10, 27, 3, 27, 10]
print(list4.count(27))


#len()
list5= [10, 5, 35, 11, 52, 11, 2, 35, 12, 61]
print(len(list5))


#index()
list6= [11, 24, 23, 61, 24, 18, 32, 43, 29, 10]
print(list6.index(11))


#min()
list6= [11, 24, 23, 61, 24, 18, 32, 43, 29, 10]
print(min(list6))


#max()
list6= [11, 24, 23, 61, 24, 18, 32, 43, 29, 10]
print(max(list6))


#reverse and sort()
list7= [11, 24, 23, 61, 24, 18, 32, 43, 29, 10]
list7.sort(reverse=True)
print(list7)


#pop()
list8= [11, 24, 23, 61, 24, 18, 32, 43, 29, 10]
print(list8.pop())
print(list8.pop(0))


#del
list9= [11, 24, 23, 61, 24, 18, 32, 43, 29, 10]
del list9[0]
print(list9)


#remove()
list10= [11, 24, 23, 61, 24, 18, 32, 43, 29, 10]
list10.remove(24)
print(list10)