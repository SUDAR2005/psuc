#To search an element in a list of given function
def searchList(l,ele):      #l=list,ele=search element
    a=ele
    if not a.isalpha() and a not in ('''!@#$%^&*()_+=-{}[]
    :";'<>,.?/'''):
        if float(ele)/(float(ele)//1)!=0:
            ele = float(ele)
    if a.isnumeric():
        ele = int(ele)
    for i in l:
        b = ele in l
        if b == True:
            return b
    else:
        return b
l_1=[1,2,4,5,5.9,"a","#"]
x=input()
print(searchList(l_1,x))
