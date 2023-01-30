'''Write a function called first_diff that is given two strings and returns the first location in which the strings
                        differ. If the strings are identical, it should return -1.                                  '''
def first_diff(str1,str2,i=0):
    if str1==str2:
        return -1
    elif str1[0]==str2[0]:
        i+=1
        return i
    else:
        i+=1
        return first_diff(str1[1:],str2[1:],i)
s="Hello"
t="HEllo"
print(first_diff(s,t))
print(first_diff(s.lower(),t.lower()))