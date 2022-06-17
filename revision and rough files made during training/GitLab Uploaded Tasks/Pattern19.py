'''
A
B B
C C C
D D D D
E E E E E
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
        print(chr(64+i+1), end=" ") # modifying the end 
    print() # for new line




