number=int(input("Please enter an integer value"))
count=0
for i in range(1,number+1):
    if number % i == 0:
        count=count+1
if count==2:
    print(number,"IS a prime number")
else:
    print(number,"is NOT a prime number")