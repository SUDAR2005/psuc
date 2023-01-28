#Program to print union of two list
l_1=[1,2,3,4]
l_2=[5,6,4,2]
for i in l_2:                   #for l_1 U l_2
    if i not in l_1:
        l_1.append(i)
for j in l_1:                   # for l_2 U l_1
    if j not in l_2:
        l_2.append(j)
print(l_1,l_2)