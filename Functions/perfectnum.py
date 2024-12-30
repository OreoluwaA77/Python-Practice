def sum_of_divisors(number):
    total=0
    for i in range(1, number):
        if number % i == 0:
            total=total+i
    return(total)
    
def is_perfect(number):
    if sum_of_divisors(number)== number:
        return(True)
    else:
        return(False)
    
def main():
    number=int(input("PLease enter an integer value"))
    perfect_number=is_perfect(number)
    if perfect_number:
        print(number, "is a percet number")
    else:
        print(number, "is NOT a perfect number")

main()