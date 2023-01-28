#cylindrical Water tank problem
import math as m
radius=float(input("Enter the height(in m):"))
height=float(input("Enter the radius (in m):"))
if radius<=0 or height<=0:
    print("The given tank can't be cylindrical in shape")
    exit()
else:
    volume= m.pi*(radius**2)*height
    print(f"The volume os tank is:{volume}")
volume=round(volume,3)
a=volume *1000/2
a=round(a,0)
print(f"Number of persons benefited by {volume}m^3 of water is {a}")


