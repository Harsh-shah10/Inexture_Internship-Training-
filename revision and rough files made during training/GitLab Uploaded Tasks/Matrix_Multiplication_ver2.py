# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

# For getting range
def createList(start, end):
    lists = []
    while start < end:
        lists+= [start]
        start+=1
    return lists
    
m1_row=int(input("Enter row of matrix1: "))
m1_col=int(input("Enter column of matrix1: "))
m2_row=int(input("Enter row of matrix2: "))
m2_col=int(input("Enter column of matrix2: "))

if m1_col==m2_row:

    #for getting range for matrix-1 & m2
    range_p = createList(0,m1_row)  #row m1
    range_q = createList(0,m2_col) # col m2
    range_n = createList(0,m1_col) #m1 col & m2 row

    print("\nEnter number in Matrix-1 : ")
    #m1 -> matrix1  
    m1=[[int(input()) for i in range_n] for j in range_p]
    print("Matrix-1 : ",m1)
    for i in range_p:
        for j in range_n:
            print(format(m1[i][j],"<4"),end="")
        print()

    print("\nEnter number in Matrix-2 : ")
    # m2 -> matrix2
    m2=[[int(input()) for i in range_q] for j in range_n]
    print("Matrix-2 : ",m2)
    for i in range_n:
        for j in range_q:
            print(format(m2[i][j],"<4"),end="")
        print()

    # resultsant matrix

    result=[]
    #assigning zero on all the index of result list to overcome array index out of bound.
    result=[[0 for i in range(0,m2_col)] for j in range(0,m1_row)]
    # iterating by row of m1

    for i in range_p:
        # iterating by column by m2
        for j in range_q:
            # iterating by rows of m2
            for k in range_n:
                result[i][j] += m1[i][k] * m2[k][j]
     
    print()
    print("\nResultant Matrix is : ",result)
    for i in range_p:
        for j in range_q:
            print(format(result[i][j],"<4"),end="")
        print()
else:
    print("Column of matrix-1 & Row of matrix-2 must be equal")

