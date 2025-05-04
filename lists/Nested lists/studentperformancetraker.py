matrix=[]
rows=int(input('Please enter number of marks'))
columns=int(input("Please enter number of subjects"))

for row in range(rows):
    nested_list=[]
    for column in range(columns):
        n=(input('please enter your scores/marks'))
        nested_list.append(n)
    matrix.append(nested_list)
print(matrix)

for row in range (len(matrix)):
    student_average=0
    for column in range (len(matrix[row])):
        student_average=student_average+(matrix[row])
    print(student_average)