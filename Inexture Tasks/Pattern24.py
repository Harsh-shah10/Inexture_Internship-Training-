'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
        '''

while True:
    n = input("Enter number of rows : ")
    if n.isnumeric()==True:
        n = int(n)
        break
    else:
        print('Sorry ! Only integers Accepted')

for i in range(n):
    for j in range(i):
        print("  ", end="")
    for k in range(i*2, n*2-1):
        print("* ", end="")
    print()
