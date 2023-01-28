#problem on  items and their price in a particular storep
print("$12 for 1 to 9 items.\n$10 for 10 to 99 items.\n$7 for 100 or more items")
items=int(input("Enter number of items:"))
if(items<=0):
    print("Please enter a valid detail.")
elif(items > 0) and (items < 10):
    price=items*12
    print(f"The price is ${price}")
elif(items >= 10) and (items < 100):
    price=items*10
    print(f"The price is {price}")
else:
    price=items*7
    print(f"The price is {price}")



