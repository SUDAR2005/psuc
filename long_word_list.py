#Write a program to print the longest word from the list
l_1 = ["siddik","pranav","vignesh","aswath","mathu","Jenif","branav"]
l_2 =[]
for i in range(len(l_1)):
    l_2.append(len(l_1[i]))
b = l_2.index(max(l_2))
Max = l_1[b]
print(Max)