'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

while True:
    n = input("Enter number of rows : ")
    if n.isnumeric()==True:
        n = int(n)
        break
    else:
        print('Sorry ! Only integers Accepted')

for i in range(n):
    # for blank space 8,6,4,2 in start of line
    print("  "*(n-i-1),end ="") 
    # for left piramid
    for j in range(i+1):
        print("*",end = " ")
    # for right piramid
    for j in range(i):
        print("*",end = " ")
    print()
