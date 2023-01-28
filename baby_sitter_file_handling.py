# Use file handling mechanism to solve the baby sitter problem
try:
    print("Starting time")
    starthrs=int(input("Enter the time in hours: "))
    startmin=int(input("Enter the time in minutes: "))
    period1=input("AM or PM:").upper()
    print("Ending Time")
    endhrs=int(input())
    endmin=int(input())
    period2=input("AM or PM:").upper()
    starttime= starthrs+(endhrs/60)
    endtime=endhrs+(endmin/60)
    if starthrs<0 or startmin<0 or endhrs<0 or endmin<0:
        raise Exception(ValueError)
    if (period1!="AM" or period1!="PM") and (period2!="AM" or period2!="PM"):
        raise Exception("Enter the correct data")
except:
    print("There is an error!")
finally:
    print("End")
    


