'''
Enter the height of Diamond : 7

      * 
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 

'''

def check_inp():
    global n
    while True:
        n = input("Enter the height of Diamond : ")
        if n.isnumeric()==True:
            n = int(n)
            break
        else:
            print('Sorry ! Only integers Accepted')

    if n == 0:
        print("Height of Diamond must be greater than 0. Try Again !")
        check_inp()
    else:
        pass

check_inp()

t = n 
n = n //2 + 1
# upper piramid
for i in range(n):
    for j in range(n, i, -1):
        print("  ", end="")
    print(" ", end = '')    
    for k in range(i*2+1):
        print("* ", end="")
    print()

t = t//2 
# lower piramid
for i in range(t):
    for j in range(i+1):
        print("  ", end="")
    print("   ", end = '')     
    for k in range(i*2, t*2-1):
        print("* ", end="")
    print()
