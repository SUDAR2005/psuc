'''In a cinema theatre 30 roows & 20 seats are there.first 15 rows cost 120 rs and rest cost 150 rs.if housefull
        how much will be collected ?if x% of type1 &y%' of seats are filled how wuch will be collected     '''
print('Type "1" if housefull else type "0"')
a=int(input("Is the theatre housefull :"))
if(a!=0 or a!=1):
    exit()
    if a == 0:
        x=int(input("Enter the percentage of queen seats filled:\t "))
        y=int(input("Enter the percentage of king seats filled:\t "))
        if(x>100 or y>100):
            print("Invalid entry!")
            exit()
        else:
            amount_2=3*((x*120)+(y*150))
            print(f"THe amount collected is {amount_2}")
    else:
        amount_1=15*20*(150+120)
        print(f"THe total amount collected during housefull is:\t{amount_1}")
