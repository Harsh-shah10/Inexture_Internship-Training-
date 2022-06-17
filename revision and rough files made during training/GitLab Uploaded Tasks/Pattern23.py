'''
"       1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5"
'''

while True:
    n = input("Enter number of rows : ")
    if n.isnumeric()==True:
        n = int(n)
        break
    else:
        print('Sorry ! Only integers Accepted')

for i in range(1,n+1):
    # for blank space at the start of each line
    for j in range(n-i):
        print(end= "  ") 
    # for printing starting no. of one side of pattern
    for k in range(i,2*i):
        print(k,end= " ")
    # for printing ending no. of other side of pattern
    for l in range(2*(i-1),i-1,-1):
        print(l, end= " ")
    print()