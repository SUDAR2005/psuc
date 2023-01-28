#Python script to print maximum from list
l = ["hello","cricket","dhoni","virat"]
max_len=len(l[0])
for i in l:
    if max_len<len(i):
        max_len=len(i)
        max_str=i
print(max_str)