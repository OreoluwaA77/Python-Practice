matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for column in range (3):
    print (matrix[column][2])
for column in range (3):
    print (matrix[1][column])
(matrix[1][1])=100
print(matrix)

for row in range (len(matrix)):
    print((matrix[row]))

for row in range (len(matrix)):
    for column in range (len(matrix)):
        print(matrix[column][row])

