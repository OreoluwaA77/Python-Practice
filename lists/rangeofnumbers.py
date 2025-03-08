def range_of_num (start,end):
    new_list=[]
    for i in range (start+1,end):
        new_list.append(i)
    print(new_list)


range_of_num(5, 9) #➞ [6, 7, 8] 
 

def list_less_than_100(number):
    total=0
    for i in range (len(number)):
        total=total+number[i]
    print(total)
    if total<100:
        print(True)
    else:
        print(False)

list_less_than_100([1,2,3,4,5,6,7])
list_less_than_100([95,10,12])
