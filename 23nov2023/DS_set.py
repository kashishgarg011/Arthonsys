#SET

# add Method
s={'a','k','h','s','h','i','s','h'}
print(s)
s.add('g')
print(s)

# union Method
s1={11,2,23,46}
s2={46,5,46,23}
print(s1.union(s2))

s3={11,32,63,47}
s4={32,54,63,4}
s5={74,8,19,47}
l=s3.union(s4).union(s5)
print(l)



# Update Method

l1=[1,2,3,4]
l2=[6,7,8]
print(l1+l2)

s6=set(l1)
ss=set(l2)
s6.update(ss)
print(s6)


# pop method
s7={1,2,3,4,5}
s7.pop()
print(s7)


# intersection Method

s8={13,62,53}
s9={62,53}
a=s8.intersection(s9)
print(a)


#  copy Method

s11={10,21,45,14}
print(s11)
s22=s11.copy()
print(s22)