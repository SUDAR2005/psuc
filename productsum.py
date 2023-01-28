#To write a python program to print the sum and product of nuber in such a way that it llooks like n+nn+nnn....
number = int(input("Enter any number"))
i = 1
sum = 0
while i <= number:
    product = number ** i
    sum += product
    i += 1
print(sum)