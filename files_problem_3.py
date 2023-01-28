#Python script to find the number of words
f=open("employee.txt","r+")
w=f.read()
w=w.split()
print(w)
print(len(w))
f.close()