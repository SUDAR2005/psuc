#book,profit and GST problem
price=float(input("Enter the price of the book:"))
cgst=0.09*price                 #SGST=CGST
profit=0.12*price
org_price=price-profit-2*(cgst)
cgst=round(cgst,3)
profit=round(profit,3)
org_price=round(org_price,3)
print(f'''The orginal price of book is Rs.{org_price}.\nThe profit of shopkeeper is Rs.{profit}.\nThe CGST is Rs.{cgst}.
The SGSTis Rs.{cgst}.''')
print("Bill Ends ")