#Write a program to guess a number
import random as r
j=1
while j<=3:
    a = input("Enter a number:")
    if a.isalpha() or a.isspace() or int(a) > 100:
        print("Enter a valid input")
        j-=1
        continue
    a = int(a)
    if a == r.randint(1,100):
         print("Your guess is correct")
         break
    else:
        if j<=2:
          print(f"Try again!You have {3-j} more chances")
          j+=1
          continue
        else:
            print("better luck next time")
            j+=1