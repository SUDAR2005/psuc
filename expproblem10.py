#To print the sum of cube of 3 consecutive numbers
num=float(input("Enter the the number:"))
sum=0
i=num
num_1=num
index=1
while i<num+3:
    num_cube=num_1**3
    sum=sum+num_cube
    print(f"Number {index} is {num_1} whose cube is:{num_cube}")
    num_1 += 1
    i += 1
    index+=1


print(f"The sum of three consecutive cubes is:{sum}")
