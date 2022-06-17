# For getting range
def createList(start, end):
    lists = []
    while start < end:
        lists+= [start]
        start+=1
    return lists

# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter


def get_cofactor(matrix, count):
    # for getting range for getting for factor
    cofactor_range = createList(1, findLen(matrix[1:]) + 1)

    new_matrix = list()
    for i in cofactor_range:
        #print("i",i)
        new_row = matrix[i][:count] + matrix[i][count+1:]
        new_matrix = new_matrix+[new_row]
        #print("new matrix ",new_matrix)
    return new_matrix


def determinant(matrix):
    if findLen(matrix) == 1:
        return matrix[0][0]
    if findLen(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    sum_cofactors = 0

    # for getting range for determinant 
    det_range = createList(0,findLen(matrix[0]))

    for column in det_range:
        sign = (-1) ** (column + 2)
        sub_determinant = (determinant(get_cofactor(matrix, column)))
        sum_cofactors += (sign * matrix[0][column] * sub_determinant)
    return sum_cofactors

# initially
row,col = 0,0

def get_matrix(row,col):
    while True:
        
        row = int(input("Enter the size of row of matrix : "))
        col = int(input("Enter the size of col of matrix : "))

        while row != col:
            print("Dimensions are incorrect. Re-enter row & col of matrix.")
            row = int(input("\nEnter the size of row of matrix : "))
            col = int(input("Enter the size of col of matrix : "))

        print(f"\nThe size of matrix is {row}x{col}")
        
        print('Enter matrix:')
        
        # range for col
        row_range = createList(0,row)
        # range for row
        col_range = createList(0,row)

        matrix = [[int(input()) for x in col_range] for y in row_range]

        print("Input Matrix : ",matrix)

        check_col = [findLen(matrix[x]) for x in range(findLen(matrix))]
        # is this the best way to check length?
        
        return row, col, matrix
      

while True:

    row, col, matrix = get_matrix(row,col)
    if row == col:
        print("Determinant of given matrix is :",determinant(matrix))
        print()

        #print(get_cofactor(matrix, count))
        break
    else:
        print("Must be a square matrix.\n")
        continue