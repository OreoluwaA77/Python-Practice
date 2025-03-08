def get_first_value (numbers):
    print(numbers[0])

get_first_value([1,2,3,4])
get_first_value([10,11,12])


def even_or_odd (number):
    total=0
    for i in range (len(number)):
        total=total+number[i]
    if total%2==0:
        print(True)
    else:
        print(False)

even_or_odd([1,2,3])
even_or_odd([1,2,3,4,5])
