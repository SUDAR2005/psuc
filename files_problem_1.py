#Write a python script to copy the content of one file to another
f=open("employee.txt","r+")
g=open("Copy_employee","w+")
for i in f.read():
    g.write(i)
g.seek(0)
print(g.read())
f.close()
g.close()