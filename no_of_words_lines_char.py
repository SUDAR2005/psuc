#Write a python script to find the numer of words in a python file
f =open("C:\\Users\\SUDAR\\Downloads\\Telegram Desktop\\21-09-2022 Data Types.txt")
l=[]
words=0
for i in f:
    data=i.split()
    l.append(data)
print(l)
print("Number of lines:")
print(f"{len(l)}")
print("No of words:")
for i in range(len(l)):
    for j in range(len(l[i])):
        words+=1
