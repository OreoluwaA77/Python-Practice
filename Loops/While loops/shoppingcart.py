total=0
count=0

while True:
    item_name=str(input("Enter the name of the item (or 'done' to finish)"))
    if item_name=='done':
        if count==0 or total==0:
            print("You have an empty shopping cart")
        else:
             print("You have a total of", count, "items in your basket")
             print("Your total cost is", total) 
        break
    item_price=float(input("Enter the price of the item"))
    round(item_price, 3) 
    if item_price>0:
        total=total+item_price
        count=count+1
        print("Added",item_name,"£",item_price,)
    elif item_price<0:
        print("Invalid Price. Please enter a positive number for", item_name)
    