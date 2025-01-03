def num_of_digits(number):
    count=0
    while number != 0:
        digit=number % 10
        number=number // 10
        count=count+1
    return(count)


def sum_of_powers(number):
    total=0
    power=num_of_digits(number)
    while number != 0:
        digit=number % 10
        number=number // 10
        total=total+ digit ** power
    return(total)

def is_armstrong(number):
        if number == sum_of_powers(number):
            return(True)
        else:
            return(False)
 

def main():
    number=int(input("Please input an integer value"))
    armstrong_number=is_armstrong(number)
    if armstrong_number:
        print(number, "is an armstrong number")
    else:
        print(number, "is NOT an armstrong number")

main()