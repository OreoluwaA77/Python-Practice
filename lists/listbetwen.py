def list_between (num_1,num_2,numbers):
    new_list=[]
    for i in range (len(numbers)):
        if num_1<numbers[i]<num_2:
            new_list.append(numbers[i])
    print(new_list)

list_between(3, 8, [1, 5, 95, 0, 4, 7])
list_between(1, 10, [1, 10, 25, 8, 11, 6])