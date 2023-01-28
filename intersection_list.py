#Write a program to print the intersection of lists
l_1=[2,7,9,6]
l_2=[3,5,4]
l=[]
for i in l_2:
    if i in l_1:
        l.append(i)
print(l)
