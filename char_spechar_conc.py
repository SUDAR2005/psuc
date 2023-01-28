#To concatinate the given chararcter with a special chararcter
a = input()
b =""
for i in a:
    if i== a[len(a)-1]:
         b+=i
    else:
        b+=i+"-"
print(b)