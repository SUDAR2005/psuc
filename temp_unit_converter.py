#fahrenheit & celcius converter
a=int(input("Enter '0' for fahrenheit to celcius & '1' for celcius to fahrenheit:"))
if(a==0):
    fahren=float(input("Enter the value:"))
    if fahren<-459.67:
        print("The temprature is less tham absolute zero")
        exit()
    else:
        celcius= (fahren - 32) * 5 / 9
        celcius=round(celcius,3)
        print(f"The value in celcius for given input {fahren}F is:{celcius}")
elif(a==1):
    celcius=float(input("Enter the value:"))
    if celcius<-273.15:
        print("The temprature is less than absolute zero")
    else:
        fahren= (celcius * 9 / 5) + 32
        print(f"The value in fahrenheit for given input {celcius}C is:{fahren}")
else:
    print("Invalid input!")