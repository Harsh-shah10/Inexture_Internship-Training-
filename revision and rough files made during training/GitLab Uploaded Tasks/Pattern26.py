'''
1
2 3
4 5 6
7 8 9 10"'''

while True:
    n = input("Enter number of rows : ")
    if n.isnumeric()==True:
        n = int(n)
        break
    else:
        print('Sorry ! Only integers Accepted')

v = 1
for i in range(n):
    for j in range(i+1):
        print(v,end=" ")
        v+=1
    print()