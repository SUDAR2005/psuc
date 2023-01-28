#count the occurance of words in a file
f=open("employee.txt","r+")
str="0"
count=0
for i in f.read():
    if i==str:
       count+=1
f.seek(0)
print(f.read())
print(count)