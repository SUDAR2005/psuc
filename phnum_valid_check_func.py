#Check whether the phone number is valid or not by using valid() func:
def valid(s):
    a=s[0:3]+s[4:7]+s[8:13]
    if ( (len(a) == 10) and a.isnumeric()) and (s[3] == "-" and s[7] == "-"):
        if s[0] in "9876":
            return True
    else:
        return False
i=0
l=[]
s=[]
while i<5:
    b = input()
    c = valid(b)
    if c is True:
        s.append(b)
        i+=1
for j in range(len(s)):
    if s[j][1] in "9":
        l.append(s[j])
print(set(s))
print(l)
