#Python script to encode the given string without using string functions
def strEncode(s=str):
    Input1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    Input2=["!","2","#","$","%","$","^","&","*","(",")","_","+","-","=","{","}","[","]",":",";","<",">",",",".","?","/"]
    Input3=["1","2","3","4","5","6","7","8","9","0"]
    confNum=["A","S","E","D","Q","Z","X","W","O","P"]
    for i in s:
        if i in Input1:
            s=s.replace(i,Input2[Input1.index(i)])
        if i in Input2:
            s=s.replace(i,Input1[Input2.index(i)])
        if i in Input3:
            s=s.replace(i,confNum[Input3.index(i)])
    return s
def strDecode(s=str):
    Input1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"," "]
    Input2 = ["!", "2", "#", "$", "%", "$", "^", "&", "*", "(", ")", "_", "+", "-", "=", "{", "}", "[", "]", ":", ";","<", ">", ",", ".", "?","/"]
    confNum = ["1","2","3","4","5","6","7","8","9","0"]
    Input3 = ["A", "S", "E", "D", "Q", "Z", "X", "W", "O", "P"]
    for i in s:
        if i in Input3:
            s=s.replace(i,confNum[Input3.index(i)])
        if i in Input2:
            s=s.replace(i,Input1[Input2.index(i)])
        if i in Input1:
            s=s.replace(i,Input2[Input1.index(i)])
    return s
a=input().lower()
b=strEncode(a)
print(b)
c=strDecode(b)
print(c)