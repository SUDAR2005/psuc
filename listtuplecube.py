#create a list of tuple that contains cube of each item inside the list in tuple
#eg [1,2,3,4,5]  =>   [(1,1),(2,4),(3,9),...]
list = [2,5,6,7,8]
newlist = []
tuple_1 = []              #Since tuple is immutable we use lisdt and do typecoversion
for i in list:
    tuple_1.append(i)
    tuple_1.append(i ** 3)
    newlist.append(tuple(tuple_1))
    tuple_1.clear()
print(newlist)

#user defined function for append
l =[]
for i in range(5):
    b = input()
    if b.isnumeric():                    #Need  to develope further
            b = int(b)
    l+=[b]
print(l)
