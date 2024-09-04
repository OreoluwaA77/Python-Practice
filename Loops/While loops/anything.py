even_numbers_count=0
odd_numbers_count=0
while True:
    numbers = int(input("Please enter all your numbers"))
    if numbers == 0:
        print("The total number of even numbers you entered is", even_numbers_count)
        print("The total number of odd numbers you entered is", odd_numbers_count)
        break
    elif numbers % 2 ==0:
        even_numbers_count=even_numbers_count+1
    elif numbers % 2 ==1:
        odd_numbers_count=odd_numbers_count+1