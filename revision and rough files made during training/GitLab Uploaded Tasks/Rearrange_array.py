# For getting range
def createList(start, end):
    lists = []
    while start < end:
        lists+= [start]
        start+=1
    return lists
arr = []

def array_size():
    global arr_size
    while True:
        arr_size = input("Enter the size of the array : ")
        if arr_size.isnumeric()==True:
            arr_size = int(arr_size)
            break
        else:
            print('Sorry ! Only integers Accepted')

    # for taking size of arrary >0
    if arr_size<=0:
        print("Minimum size of the array must be greater than 0")
        array_size()
    else:
        pass

array_size()

# for appending/adding numbers in the original array
def append_number(arr):
    tmp = []
    while True:
        n = input("Enter number : ")
        if n.isnumeric()==True:
            n = int(n)
            #arr+=[n]
            #print("inp_lst : ",inp_lst)
            break
        else:
            print('Sorry ! Only integers Accepted')
    
    for i in createList(0,arr_size):
        tmp+=[i]
    
    if n not in tmp and arr_size==1:
        print(f"Inputs must be 0")
        append_number(arr)
    elif n not in tmp:
        print(f"Inputs must be between 0 to {arr_size-1}")
        append_number(arr)
    else:
        arr+=[n]        

for i in range(0,arr_size):
    print(f"\nEnter A[{i}]")
    append_number(arr)

print("\nArray is : ",arr)

# filling none in the resulatant array
res = []
for i in createList(0,arr_size):
    res+=["none"]
#print("res : ",res)


# rearranging the array
i = 0
for j in arr:
    res[j]=i
    i+=1
#print("Sorted array is : ",res)

# updating the values in the original array
i = 0    
for j in res:
    arr[i]=j
    i+=1
print("Sorted array is : ",arr)