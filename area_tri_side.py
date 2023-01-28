#determine area of triangle when all sides are given
a=float(input("Enter the length of side1:"))
b=float(input("Enter the length of side2:"))
c=float(input("Enter the length of side3:"))
if(a<0) or (b<0) or (c<0):
    print("Invalid entry!")
else:
    s=(a+b+c)/2
    if (s<a) or (s<b) or (s<c):
        exit()
    else:
        area=(s*(s-a)*(s-b)*(s-c))**(0.5)
        area=round(area,3)
        print(f"The area of triangle with lengths {a} , {b} & {c} is {area}")