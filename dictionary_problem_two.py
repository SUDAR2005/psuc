'''Write a program that repeatedly asks the user to enter product names and prices. Store all of these in a dictionary
            whose keys are the product names and whose values are the prices. Perform the following:
   a) List the product names
   b) List the prices
   c) Display the product name that are >200 price
   d) Display the price details of the product name starts with 'a'
'''
i=0
print("If you have to quit the process of entering give 0 in both inputs")
d={"item":[],"price":[]}
while i==0:
    a=input("Enter the prdt name: ").upper()
    b=int(input("Enter the prdt price:  "))
    if a=="0" and b==0:
        break
    d["item"].append(a)
    d["price"].append(b)
#To list products and items
a=d["item"]
b=d["price"]
print("The product with price >200 is:")
for i in b:
    if i>200:
        pos=b.index(i)
        print(a[pos])
print("The product that starts with a is ")
for j in a:
    if j[0]=="A":
        print(j)
