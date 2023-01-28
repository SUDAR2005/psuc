#write a program to merge and sort two list
l_1 = [1,2,3,4]
l_2 = [3,5,8,9]
for i in range(len(l_2)):
    l_1.append(l_2[i])
print(sorted(l_1))