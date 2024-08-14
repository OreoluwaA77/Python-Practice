total=0
sum=0
for i in range (0,10):
    number=int(input("Enter a number"))
    if 10<=number<100:
        total=total+number
    if 100<=number<1000:
        sum=sum+number
print("The total of all your two digit numbers is",total)
print("The total of all your three digit numbers is",sum)