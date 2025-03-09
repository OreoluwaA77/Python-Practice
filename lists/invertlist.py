def invert_list (numbers):
    new_list=[]
    for i in range (len(numbers)):
        new_list.append(numbers[i]*-1)

    print(new_list)

invert_list([1,2,3,4])


def double_list (numbers):
    for i in range (len(numbers)):
        numbers[i]=numbers[i]*2
    print(numbers)

double_list([2,4,6,8])
double_list([1,2,3,4])