#To Write a program to print two digit numbers that end with 3,6 and 9
num = 10
i = num
print("The numbers ending with 3,6 & 9 are:")
while i < 100:
    if i % 10 == 3 or i % 10 == 6 or num % 10  == 9:
        print(num)
    i += 1
print("           End             ")

