# For getting range
def createList(start, end):
    lists = []
    while start < end:
        lists+= [start]
        start+=1
    return lists


def det_3x3matrix(m1):
    a = m1[0][0]
    b = m1[0][1]
    c = m1[0][2]

    a_det1=(m1[1][1]*m1[2][2])-(m1[1][2]*m1[2][1])
    b_det2=(m1[1][0]*m1[2][2])-(m1[1][2]*m1[2][0])
    c_det3=(m1[1][0]*m1[2][1])-(m1[1][1]*m1[2][1])

    det= a*(a_det1)-b*(b_det2)+c*(c_det3)
    print("determinant of Matrix is : ",det)


# taking 3x3 matrix as input 
print("Enter number in Matrix-1 : ")
#m1 -> matrix

#for getting range
listsx = createList(0,3)  

m1=[[int(input()) for i in listsx] for j in listsx]
print("Matrix-1 : ",m1)
for i in listsx:
    for j in listsx:
        print(format(m1[i][j],"<4"),end="")
    print()

print()

# using method
det_3x3matrix(m1)

