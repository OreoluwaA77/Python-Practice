def count_factors(number):
    count=0
    for i in range(1, number+1):
        if number % i==0:
            count=count + 1
    return(count)

def is_prime(number):
    if count_factors(number) == 2:
        return(True)
    else:
        return(False)

def main():
    number=int(input("enter a number"))
    prime=is_prime(number)
    if prime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")

main()

