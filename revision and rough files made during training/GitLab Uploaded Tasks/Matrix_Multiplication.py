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

#("HINT ! : For 3x3 matrix p,q,r=3")
# p,q,n = 3,3,3
    
#for getting range
range_p = createList(0,3)  
range_q = createList(0,3)  
range_n = createList(0,3)


print("Enter number in Matrix-1 : ")
#m1 -> matrix1  
m1=[[int(input()) for i in range_n] for j in range_p]
print("Matrix-1 : ",m1)
for i in range_p:
    for j in range_n:
        print(format(m1[i][j],"<4"),end="")
    print()

print("Enter number in Matrix-2 : ")
# m2 -> matrix2
m2=[[int(input()) for i in range_q] for j in range_n]
print("Matrix-2 : ",m2)
for i in range_n:
    for j in range_q:
        print(format(m2[i][j],"<4"),end="")
    print()

# resultsant matrix
result = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
# iterating by row of m1

len_m1 = createList(0,3)  
len_m2 = createList(0,3)  
len_m1 = createList(0,3)  

len_m2[0] = createList(0,3)  

# for getting range for resulatant matrix
range_res_i = createList(0,(findLen(len_m1)))
range_res_j = createList(0,(findLen(len_m2[0])))
range_res_k = createList(0,(findLen(len_m2)))

for i in range_res_i:
    # iterating by column by m2
    for j in range_res_j:
        # iterating by rows of m2
        for k in range_res_k:
            result[i][j] += m1[i][k] * m2[k][j]
 
print()
print("Resultant Matrix is : ",result)
for i in range_p:
    for j in range_q:
        print(format(result[i][j],"<4"),end="")
    print()
