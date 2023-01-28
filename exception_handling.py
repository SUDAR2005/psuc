#Python script to know about exception handling
def exceptionHandling(a):
    l=0
    try:
            b=a/l
            return(b)
    except ZeroDivisionError:
           print("Enter a valid input")
    except TypeError:
            print("Enter a valid argument")
    except NameError:
            print("Check for qotation")
