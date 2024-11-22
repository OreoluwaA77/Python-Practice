total=0 
price=0

while True:
    age= int(input("Enter the age of the visitor (or -1 to finish)"))
    if 0<age < 12:
        price= 5
        total=total + price
        print ("Child ticket", total)
    elif 12<=age<=17:
        price=8    
        total=total + price
        print("Teenager ticket", total)
    elif 18<=age<=59:
        price=12
        total=total + price
        print("Adult ticket", total)
    elif age>60:
        price=6
        total=total + price
        print("Senior ticket", total)
    elif age==-1:
        break
