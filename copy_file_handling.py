f = open("C:\\Users\\SUDAR\\OneDrive\\Documents\\employee.txt","r+")
g = open("C:\\Users\\SUDAR\\Downloads\\Telegram Desktop\\21-09-2022 Data Types.txt","w+")
c=0
print(f.readlines())
f.seek(0)
for i in f.readlines():
    if i[len(i)-1]=="\n" or i[len(i)-1]!="\n":
        c+=1
        if c%2!=0:
            g.write(i)
g.seek(0)
print(g.read())
g.close()
f.close()
