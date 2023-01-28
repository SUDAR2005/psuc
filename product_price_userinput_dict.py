#Python script to get input from the user repetedly and store it in dict
count=int(input(("Enter the number of times the input has to be given:")))
d = {}
for i in  range(count):
    item =input("Enter the item:")
    price=int(input("enter the price:"))
    d.update({item:price})
print(f"{d},\n{d.keys()},\n{d.values()}")
print("The products with price greater than $200 is:")
for j in d:
    if d[j]>200:
        print(j)
print("The name of products that starts with 'a' is:")
for k in d:
    if k[0]=="a":
        print(k)
        continue