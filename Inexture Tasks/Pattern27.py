'''
1   2   3   4
12  13  14  5
11  16  15  6
10  9   8   7
'''

def check_inp():
    global n
    while True:
        n = input("\nEnter no of rows : ")
        if n.isnumeric() == True:
            n = int(n)
            break
        else:
            print('Sorry ! Only integers Accepted')

    if n == 0:
        print("No of rows must be greater than 0. Try Again !")
        check_inp()
    else:
        pass

check_inp()

# for creating nested list with size n
# to store our matrix inside it
s_matrix = []
for i in range(n):
    s_matrix.append([])
    for j in range(n):
        s_matrix[i].append('#')

r1 = 0 # row 1
c1 = 0 # col 1
r2 = n # row 2
c2 = n # col 2
num = 1
while num <= n**2:
    for i in range(c1, c2):
        s_matrix[r1][i] = num
        num += 1
    if num > n**2:
        break
    for i in range(r1+1, r2):
        s_matrix[i][c2-1] = num
        num += 1
    if num > n**2:
        break
    for i in range(c2-2, c1-1, -1):
        s_matrix[r2-1][i] = num
        num += 1
    if num > n**2:
        break
    for i in range(r2-2, r1, -1):
        s_matrix[i][c1] = num
        num += 1
    r1 += 1
    r2 -= 1
    c1 += 1
    c2 -= 1

# for printing the final Matrix
for i in range(n):
    for j in range(n):
        print(s_matrix[i][j], end="\t")
    print()
