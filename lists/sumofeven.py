def sum_of_evens (numbers_1,numbers_2,numbers_3):
    total=0
    total_1=0
    total_2=0
    total_3=0
    for i in range (len(numbers_1)):
        if numbers_1[i]%2==0:
           total_1=total_1+numbers_1[i]
        elif numbers_2[i]%2==0:
           total_2=total_2+numbers_2[i]
        elif numbers_3[i]%2==0:
           total_3=total_3+numbers_3[i]         
    total=total_1+total_2+total_3
    print(total)

sum_of_evens([1,2,3],[4,5,6],[7,8,9],)