new_grovery_basket_list=[]
grocery_basket=(input("Enter your grocery list"))
grocery_basket_list=grocery_basket.split(",")
for i in range (len(grocery_basket_list)):
    grocery_basket_list[i]=grocery_basket_list[i].replace(" ","")
    if grocery_basket_list[i] not in new_grovery_basket_list:
        new_grovery_basket_list.append(grocery_basket_list[i])
new_grovery_basket_list.sort()
print(new_grovery_basket_list)
search=(input("What item are you looking for in your basket?"))
if search in new_grovery_basket_list:
    print ("Your item is in good hands")
else:
    print("Uh oh we can't find your item")
    
def remove_duplicates_and_sort (stringlist):
    stringlist_list=stringlist.split(",")
    final_list=[]
    for i in range (len(stringlist_list)):
        stringlist_list[i]=stringlist_list[i].replace(" ","")
        if stringlist_list[i] not in final_list:
            final_list.append(stringlist_list[i])
    final_list.sort()
    print(final_list)
    return(final_list)

def search(final_list):
    search=(input("What item are you looking for in your basket?"))
    if search in final_list:
        print ("Your item is in good hands")
    else:
        print("Uh oh we can't find your item")

def main ():
    stringlist=(input("Enter your list"))
    final_list=remove_duplicates_and_sort(stringlist)
    search(final_list)



main()