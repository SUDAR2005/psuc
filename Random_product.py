#Random product between x and y any print x,y
import random
i=0
j=0
while i<2:
    x=random.randint(0,51)
    i+=1
while j<2:
    y=random.randint(0,51)
    j+=1
print(f"The product of {x} and {y} is {x*y}")

