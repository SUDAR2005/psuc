#Print 5 numbers that are divisible by by 11 (Get input from the user)
num=int(input("Enter any number:"))
i=0
while i< 11:
    if num % 11 == 0:
        print(num)
        i+=1
    num+=1