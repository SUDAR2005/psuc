# Write a python script to find FLAMES
a = input().upper()
b = input().upper()
if len(a)>len(b):
    b+=" "*(len(a)-len(b))
elif len(b)>len(a):
    a+=" "*(len(b)-len(a))
for i in a:
    for j in b:
        if i==j and not(i.isspace() and j.isspace()):
            c=a.find(i)
            d=b.find(j)
            if c!=-1 and d!=-1:
                a=a[:c]+a[c+1:]
                b=b[:d]+b[d+1:]
newstr=(a+b).replace(" ","")
print(newstr)
l=len(newstr)%6
print(l)
if l==1:
    print("Friend")
elif l==2:
    print("Love")
elif l==3:
    print("Affection")
elif l==4:
    print("Marriage")
elif l==5:
    print("Enemy")
elif l==0:
    print("Sister")