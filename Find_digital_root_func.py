#Write a python program to obtain digital root using function
def findDigitalRoot(num):
    if num < 10:
        return num
    num = num%10 + findDigitalRoot(num//10)
    return findDigitalRoot(num)
n = 45893
print(findDigitalRoot(n))