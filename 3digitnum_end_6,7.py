#Write a program to print 3 digit numbers ending with  6,7
num = 100
print("The numbers ending with 6 and 7 are:")
while num<1000:
    if num %10 == 6  or num %10 == 7:
        print(num)
    num += 1
print("   The end   ")
