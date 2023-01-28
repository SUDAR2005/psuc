#To find the intersection of two sets
print("Enter characters in set 1")
c={}
d={}
for i in range(0,5):
    c[i]=int(input())
print("Enter number in set 2")
for j in range(0,5):
    d[j]=int(input())
e=c.intersection(d)
print(f"The set obtained by c intersection d is:{e}")
