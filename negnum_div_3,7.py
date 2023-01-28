#Write a program to print first 15 negative numbers divisible by 3 and 5
num=0
i=0
while i<15:
    if num % 3 == 0 and num % 5 == 0:
        print(num)
        i+=1
    num+=1