#Python program to find the longest word
f=open("employee.txt","r+")
m=f.read()
print(m,"\n")
m=m.split()
max=len(m[0])
for i in m:
    if len(i)>=max:
        max=i
print(max)
#Limitations are if more than one string are same length we will get the last one