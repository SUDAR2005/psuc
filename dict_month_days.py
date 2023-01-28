#Python script to find the months having 31 days using dict
a={"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,
   "October":31,"November":30,"December":31}
l_1 = []
end_y=[]
for i in a:
   if a.get(i)==31:
      l_1.append(i)
   if i[len(i)-1].lower()=="y":
      end_y.append(i)
print(l_1)
print(end_y)