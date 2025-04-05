def numbers_sum (integer):
    total=0
    for i in range (len(integer)):
        if isinstance(integer[i],int):
            total=total + integer[i]
    print(total)

numbers_sum([1, 2, "13", "4", "645"])