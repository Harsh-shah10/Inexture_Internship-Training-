'''
1 2 3 4 5
1 2 3 4 
1 2 3
1 2
1
'''

while True:
    n = input("Enter number of rows : ")
    if n.isnumeric()==True:
        n = int(n)
        break
    else:
        print('Sorry ! Only integers Accepted')
 
for i in range(n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()
        