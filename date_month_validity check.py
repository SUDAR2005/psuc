# Write ap program to check the validity of the given inputs
try:
    date=int(input())
    month=int(input())
    year=int(input())
    if date<=0 or month<=0 or year<=0 or month>12:
        raise Exception(ValueError)
    elif month==1 or (month<2 and month>=7):
        if month%2==0 and date>30:
            raise Exception(ValueError)
        elif month%2!=0 and date>31:
            raise Exception(ValueError)
    elif month>7 and month<=12:
        if month%2==0 and date>31:
            raise Exception(ValueError)
        elif month%2!=0 and date<30:
            raise Exception(ValueError)
    elif month==2 and year%4==0:
        if date>29:
            raise Exception(ValueError)
    elif month==2 and year%4!=0:
        if date>28:
            raise(Exception)(ValueError)
    print(f"{month}/{date}/{year}")
except ValueError:
    print("Please enter the data correctly")
