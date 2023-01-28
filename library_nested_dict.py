#Write a python script to show the book details from it's title as input
data_structure={"Title":"Data Structure",
                           "Author":"Lipschute",
                           "Subject":"DS","Publisher":
                           "McGraw","Quantity":4,"Price":117}
dos_guide={"Title":"DOS Guide",
                           "Author":"NORTRON",
                           "Subject":"OS","Publisher":
                           "PHI","Quantity":3,"Price":175}
turbo_c={"Title":"Turbo C++",
                           "Author":"Sobort Lafore",
                           "Subject":"Prog","Publisher":
                           "Galgoti","Quantity":5,"Price":270}
library={"Data Structure":data_structure,
         "DOS Guide":dos_guide,
         "Turbo C++":turbo_c}
for i in library:
    if library[i]["Author"][0].upper()=="S":
        print(library[i]["Author"])
for i in library:
    if library[i]["Price"]<200 and library[i]["Quantity"]>3:
        print(library[i]["Title"])
