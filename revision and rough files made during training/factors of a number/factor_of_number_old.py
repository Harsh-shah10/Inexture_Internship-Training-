n = int(input("Enter the number : "))

def createList(start, end):
    lists = []
    while start < end:
        lists+= [start]
        start+=1
    return lists
        

def factors(n1):
    # method for finding factors
    l1 = []
    
    # factors of n1
    range_n1 = createList(1,n1+1)
    for i in range_n1:
        if n1%i==0:
          l1 = l1 + [i]

    # printing factors of n1 
    print(f"Factors of {n1} is : ",l1)
    
# Calling the Factors Method
factors(n)
