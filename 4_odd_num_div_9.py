# write a program to print 4 odd numbers divisible by 9
num=0
i=num
while i<4:
    if num%2!=0:
        if num%9==0:
            print(num)
            i+=1
    num+=1

