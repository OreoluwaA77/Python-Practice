number=int(input("Please enter an integer value"))
for i in range (1,number+1):
    if number % i == 0:
        print("The factors of this number is",i)
count=0
for i in range(1,number+1):
    if number % i == 0:
        count=count+1
print("The total count of the factors are",count)
total=0
for i in range(1,number+1):
    if number % i == 0:
        total=total+i
print("The total of the factors are",total)

