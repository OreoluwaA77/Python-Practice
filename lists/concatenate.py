def concat (number,number_2):
    
    new_list=number+number_2
    print(new_list)

concat([1,2,3],[4,5,6])


def get_sum_of_elements(number):
    total=0
    for i in range (len(number)):
        total=total+number[i]
    print (total)

get_sum_of_elements([1,2,3,4])