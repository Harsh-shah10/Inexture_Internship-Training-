'''
* * * * *
* * * *
* * * 
* *
*
'''
# for validation of taking numbers as inputs are Integers
while True:
    n = input("Enter number of rows : ")
    if n.isnumeric()==True:
        n = int(n)
        break
    else:
        print('Sorry ! Only integers Accepted')

for i in range(n):
	print("* "*n)
	n = n-1
