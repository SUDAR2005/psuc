#Python script to print sans clock
def SandClock(height):
    try:
        if height%2==0:
            raise Exception(ValueError)
        row=height//2+1
        for i in range(row):
            for j in range(row):
                if i>j:
                    print(end=" ")
                else:
                    print("*",end=" ")
            print()
        for i in range(1,row):
            for j in range(row):
                if i+j<row-1:
                    print(end=" ")
                else:
                    print("*",end=" ")
            print()
    except ValueError:
        print("The height value should be only even")
    except:
        print("There is an issue in your input")
    finally:
        print("The End")
SandClock(9)