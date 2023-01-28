# Write a python script using exception to find the salary for extra hours worked
try:
    hrs=float(input())
    rate=float(input())
    if hrs<40:
        a=hrs*rate
        print(a)
    elif hrs>=40:
        a=(hrs*rate)+((hrs-40)*rate*1.5)
        print(a)
    elif hrs<0 or rate<0:
        raise Exception(ValueError)
except ValueError :
    print("Kindly check the input")