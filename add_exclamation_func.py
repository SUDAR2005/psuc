#Write a function that add ! at the end to the strings in the list
def addExclamatory(l):
    l_1=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
            if j == len(l[i])-1:
                l[i]+="!"
                l_1.append(l[i])
    return l_1
l =["wow","great","amazing"]
print(addExclamatory(l))