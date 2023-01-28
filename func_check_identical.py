#Write a python program to check whether the given string is identical or not using functions
def first_diff(str1,str2):
    l_1=[]                              #Instead of this use split method
    l_2=[]
    for i in str1:
        l_1.append(i)
    for j in str2:
        l_2.append(j)
    if len(l_1)>len(l_2):
        Min = len(l_2)
    else:
        Min = len(l_1)
    for k in range(Min):
        if l_1[k]!=l_2[k]:
            return k
    return -1
a =input()
b =input()
print(first_diff(a,b))