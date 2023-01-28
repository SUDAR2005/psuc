#Write a python script to copy alternate files
f = open("C:\\Users\\SUDAR\\OneDrive\\Documents\\employee.txt","r+")
g = open("C:\\Users\\SUDAR\\Downloads\\Telegram Desktop\\21-09-2022 Data Types.txt","w+")
for i in f:
    g.write(i)
g.seek(0)
print(g.read())
g.close()
f.close()
