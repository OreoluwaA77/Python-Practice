def is_pandigital (number):
    all_numbers="0123456789"
    flag=True
    for i in range (len(number)):
        if all_numbers[i]  not in number:
           flag=False
    if flag:
        print(True)
    else:
        print(False)
    
is_pandigital("0123456789")