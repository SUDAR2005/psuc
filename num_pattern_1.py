#To print a combination of increasing and decreasing number pattern.
n=int(input("Enter the number of rows:"))

for i in range(1,n+1):
    m=1
    k =5
    for j in range(1,n+1):
        if (i>n-j):
            print(k,end= " ")
            k-=1
        else:
            print(m,end =" ")
            m+=1
    print()

