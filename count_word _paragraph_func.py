#To print the total number of words in the string
def countwords(stri):
    count = 1
    for i in stri:
        if i ==" " or i=="\n":
            count+=1
        elif i==None:
            count = 0
    return count
s=input()
print(countwords(s))
