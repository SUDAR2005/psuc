#python script to encode the given matrix by replacind the odd and even positions
def encode(s):
    a=""
    b=""
    for i in range(len(s)):
        if i%2==0:
            a+=s[i]
        else:
            b+=s[i]
    return a+b
def decode(s=str):
    s_odd=s[:len(s)//2+1]
    s_even=s[len(s)//2+1:]
    s_org=""
    s=""
    if len(s_odd)>len(s_even):
        s_even+="~"
    for i in range(len(s_odd)):
        s_org+=(s_odd[i]+s_even[i])

    for j in s_org:
        if j!="~":
            s+=j
    return s
Input=encode("message")
print(Input)
output=decode(Input)
print(output)