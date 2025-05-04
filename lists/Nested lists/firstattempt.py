matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for column in range (3):
    print (matrix[column][2])


matrix=[]
rows=int(input('Please enter your number of rows'))
columns=int(input("Please enter your number of columns"))

for row in range(rows):
    nested_list=[]
    for column in range(columns):
        n=(input('please enter your desired element for'))
        nested_list.append(n)
    matrix.append(nested_list)
print(matrix)
