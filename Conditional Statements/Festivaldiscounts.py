money_spent=float(input("Please type how much money you spent at todays festival"))
money_spent= round(money_spent,2)
if money_spent>1000:
    print(money_spent,"Amount to be paid after discount:",money_spent*0.5)
elif 1000>=money_spent>=501:
    print(money_spent,"Amount to be paid after discount:",money_spent*0.35)
elif 501>=money_spent>=201:
    print(money_spent,"Amount to be paid after discount:",money_spent*0.25)
elif money_spent<200:
    print(money_spent,"Amount to be paid after discount:",money_spent*0.05)
    
