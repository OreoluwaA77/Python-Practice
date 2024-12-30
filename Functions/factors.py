def factor (number):
    total=0
    for i in range(1, number+1):
        if number % i == 0:
            total=total+i
    return(total)

print(factor(9))