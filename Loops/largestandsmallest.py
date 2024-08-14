number=int(input("Enter a number  "))
largest=number
smallest=number
for i in range(0,10):
    number=int(input("Enter a number  "))
    if largest<number:
        largest=number
    if smallest>number:
        smallest=-number
print("The largest number is ", largest)
print("The smallest number is ", smallest)