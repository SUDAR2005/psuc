#python script to copy alternate lines of files
f=open("employee.txt","r+")
g=open("new_employee","w+")
j=1
for i in f.readlines():
    if j%2!=0:
       g.write(i)
    j+=1
g.seek(0)
f.seek(0)
print("old file")
print(f.read())
print()
print("new file")
print(g.read())
f.close()
g.close()