#To print thhe combinations of given numbers
a=input("Enter number 1:")
b=input("Enter number 2:")

c=input("Enter number 3:")
d=[a,b,c]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if i!=j and j!=k and k!=i:
                 print(d[i],d[j],d[k])
