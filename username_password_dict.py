#Python script to valilditate the user name and password
d={"Sudar":"Sudar","Siddhik":"Selva","jenif":"Deck"}
for i in range(4):
    for j in d:
        product=input("Enter the user name:")
        if product==j:
             key=input("Enter the password:")
             if key == d[j]:
                print("logging in")
                break
             else:
                print("Enter valid password")
else:
    print("Enter valid user id")


