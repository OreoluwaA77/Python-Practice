def get_discounts (numbers, discount):
    multiplier=discount[0:-1:]
    multiplier=int(multiplier)
    for i in range(len(numbers)):
        applied_dicounts=numbers[i]*(multiplier/100)
        print(applied_dicounts)

get_discounts([100,20,40],"50%")
get_discounts([100,20,40],"1%")