#Write a python script to find the digital root
def findDigitalRoot(n):
    if n<10:
        return n
    else:
        return findDigitalRoot(sum(int(i) for i in str(n)))
print(findDigitalRoot(45893))