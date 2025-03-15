def find_none(numbers):
        if None in numbers:
            print(numbers.index(None))
        else:
            print("-1")

find_none([1,2,3,4,None])
find_none([1,2,3,4])