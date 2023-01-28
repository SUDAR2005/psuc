#Python script using file handling methods
f = open("employee.txt","r")
f.seek()
print(f.readlines())
for i in f:
    c=i.split()
    if int(c[1])>50:
        print(i)
f.close()
