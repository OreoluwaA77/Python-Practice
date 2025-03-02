def can_alternate(number):
    count_0=0
    count_1=0
    for i in range (len(number)):
        if number[i] == "0":
            count_0=count_0+1
        elif number[i] == "1":
            count_1=count_1+1

    if count_0==count_1-1:
        print("True")
    elif count_1==count_0-1:
        print(True)
    else:
        print("False")

can_alternate("1010101")
can_alternate("1111")
can_alternate("010001")