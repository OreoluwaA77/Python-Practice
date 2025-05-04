

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in range (len(matrix)):
    total=0
    for column in range (len(matrix[row])):
        print(column,row,(matrix[column][row]))
        total=total+(matrix[column][row])
    print(total)

