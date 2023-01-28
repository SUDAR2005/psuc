#Wroite a python script to print the combination of given number
s=[1,2,3]
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i!=j and j!=k and i!=k:
                print(s[i],s[j],s[k])
