#Write a Python script to find the sum of elements in nested list
def addNestedList(n):
    Sum=0
    for i in n:
        if type(i)==type([]):
            Sum+=addNestedList(i)
        else:
            Sum+=i
    return Sum
s=[1,2,[3,4,5],[9,4,2]]
print(addNestedList(s))