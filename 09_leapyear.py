#To find whether the given year is leap year or not
yr=int(input("Enter any year"))
if yr%400==0:
    print(f"The year {yr} a leap year")
elif  yr%4==0 and yr%100!=0:
    print(f'''The year {yr} is a leap year''')
else:
    print("The year is not a leap year")
