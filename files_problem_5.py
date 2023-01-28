#python script to  search and replace a word in a file
f = open("employee.txt","r+")
rep_txt="manager"
m=f.read()
s=m.replace("manager","servant")
print(s)
f.close()