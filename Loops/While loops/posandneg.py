count=0
negative_count=0
while True:
    number= int(input("Enter all your numbers"))
    if number == 0:
        print("The total number of postive numbers is",count)
        print("The total number of negative numbers is",negative_count)
        break

    elif number>0:
        count=count+1
    
    elif number<0:
        negative_count=negative_count+1


