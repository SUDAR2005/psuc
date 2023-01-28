def FindFibbSeq(count):
    a=0
    b=1
    n=" "
    print(a)
    print(b)
    for i in range(count):
        if i == count-1:
            return n
        else:
            c=a+b
            a,b=b,c
            print(c)

Count=int(input())
print(FindFibbSeq(Count))
