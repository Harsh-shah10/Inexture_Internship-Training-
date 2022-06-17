'''
"          1
         1   1
       1   2   1
     1   3   3    1
   1  4    6   4   1
 1  5   10   10  5   1"
 '''

while True:
    n = input("Enter number of rows : ")
    if n.isnumeric()==True:
        n = int(n)
        break
    else:
        print('Sorry ! Only integers Accepted')

lst = []
# generating a list consisting of numbers as per pattern
for i in range(n):
    tmp = []
    for j in range(i+1):
        if(j==0 or j==i):
          tmp.append(1)
        else:
            tmp.append(lst[i-1][j] + lst[i-1][j-1])
    lst.append(tmp)
                

for i in range(n):
    # for blank space at the start of each line
    for space in range(n-i-1):
        print("  ", end = "") 
    # printing the pattern
    for j in range(i+1):
        print(lst[i][j], end="   ")
    print()   
    
