def factors(n):    
    l1 = [] 
    l2 = []
    sq_root = int(n**0.5) # for getting sqaure root as whole number
    for i in range(1,sq_root+1): 
        quotient = n//i # for getting quotient as whole number.
        rem = n%i # for getting remainder    
        if rem == 0:
            l1.append(i) 
            l2.append(quotient)    

    return sorted(set(l1+l2)) # using set to remove duplicate value ex. 16

while True:
    n = input("Enter the no. : ")
    if n.isnumeric()==True:
        n = int(n)
        break
    else:
        print('Sorry ! Only integers Accepted')

print(factors(n))
