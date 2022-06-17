arr =[]

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

# list consisting numbers from [0 to arr_size]
allowed_no = []
for i in range(0,arr_size):
    allowed_no.append(i)
    #print("allowed_no : ",allowed_no)

# for appending/adding numbers in the original array
def append_number(arr,allowed_no):

    while True:
        n = input("Enter number : ")
        if n.isnumeric()==True:
            n = int(n)
            break
        else:
            print('Sorry ! Only integers Accepted')

    if n not in allowed_no and arr_size==1:
        print(f"Input must be 0")
        append_number(arr,allowed_no)
    elif n not in allowed_no:
        print(f"Inputs must be between 0 to {arr_size-1}")
        append_number(arr,allowed_no)
    elif n not in arr:
        arr+=[n]   
    else:
        print(f"{n} is already taken!. Please Enter another number")
        append_number(arr,allowed_no)  

for i in range(0,arr_size):
    print(f"\nEnter A[{i}]")
    append_number(arr,allowed_no)

print("\nArray is : ",arr)

# filling none in the resulatant array
res = []
for i in range(0,arr_size):
    res+=["none"]
#print("Resulatant array : ",res)

# rearranging the array
i = 0
for j in arr:
    res[j]=i
    i+=1

# updating the values in the Original Array
i = 0    
for j in res:
    arr[i]=j
    i+=1
print("Output array : ",arr)
