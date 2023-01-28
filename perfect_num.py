#Write a python script to find the perfect numbers
def findPerfect(n=int()):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        return True
    return False
print(findPerfect(8128))

def fibonnaciSumCheck(num):
    if num==1 or num==0:
        return num
    else:
        return num*fibonnaciSumCheck(num-1)
print(fibonnaciSumCheck(5))