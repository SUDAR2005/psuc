from operator import mod
tuple_1=(2,1,9,8,7,6)
tuple_2=(4,5,6,7,5,6)
sam_tup=[]           #empty tuple to perform last looping operation
print(tuple(map(mod,tuple_1,tuple_2)))      #map is inbuild funtion that applis a methos to the interable/es given after that

if len(tuple_1)<=len(tuple_2):          #same program bvut it will take the second tup if if first is smaller than 2
    for i in range(len(tuple_1)):
        Mod = tuple_1[i]%tuple_2[i]
        sam_tup.append(Mod)
else:
     for i in range(len(tuple_2)):
         Mod = tuple_2[i]%tuple_1[i]
         sam_tup.append(Mod)
print(tuple(sam_tup))


