'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
# for validation of taking numbers as inputs are Integers
while True:
    n = input("Enter number of rows : ")
    if n.isnumeric()==True:
        n = int(n)
        break
    else:
        print('Sorry ! Only integers Accepted')

for i in range(0,n): # for no of rows
    for j in range(0,i+1): # for no of coloumns
        print(j+1, end=" ") # modifying the end 
    print() # for new line


