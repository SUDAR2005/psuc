#Note-To use max() an min() functions we need to have all the items as integer
tuple=[]
for i in range(5):       #Here loop is used to reduce the continuous addition of items to list
    tuple.append(i)
print(max(tuple))
print(min(tuple))
#To find max & min using user defined function

tuple_1=[]
Len = 0
for k in range(98):
    tuple_1.append(k)
for a in tuple_1:                     #To find the length without using an inbuilt
    Len+=1
if(Len==0):
    print(f"The entered {type(tuple_1)} is empty")
Max = tuple_1[0]                        #consider the initial values as max and min initially initially the initial value can be any
Min = tuple_1[0]
for b in range(Len):
    if tuple_1[b]>Max:
        Max=tuple_1[b]
    elif tuple_1[b]<Min:
        Min=Tuple_1[b]
print(Max)
print(Min)

