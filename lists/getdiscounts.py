def get_discounts (numbers, discount):
    for i in range(len(numbers)):
        applied_dicounts=numbers[i]*(discount/100)
        print(applied_dicounts)

get_discounts([100,20,40],50)