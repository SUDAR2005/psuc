#Add a tuple to list and viceversa
#Adding tuple to list
list_1= [1,2,3,4]
tuple_1= (7,6,7,8,9,0)
print(f"The new list after introducing the tuple is {(list(tuple_1)+list_1)}")
#Adding list to tuple
print(f"The new tuple after adding the list is{tuple(list_1)+tuple_1}")
#The below line is to keep in mind that no list or tuple or string or any different datatype can be concatinated
print(f"The new tuple is :"+str(list_1))
list_1.extend(tuple_1)    #Extend methos adds the items of tuple or another list to the end of list
print(list_1)