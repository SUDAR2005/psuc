#program to enter the conditions for given celcius value
a=float(input("Enter the value in celcius:"))
if a<-273.15:
    print("The temprature is invalid it is less tha absolute zero")
elif a==-273.15:
    print("The temprature is equal to absolute zero")
elif(a>-273.15) and (a<0):
    print("The temprature is below freezing point")
elif(a==0):
    print("The temprature is at freezing ppoint")
elif(a>0) and(a<100):
    print("The temprature is in normal range")
elif(a==100):
    print("The temprature is at boiling point")
else:
    print("The temprature is above boiling point")
