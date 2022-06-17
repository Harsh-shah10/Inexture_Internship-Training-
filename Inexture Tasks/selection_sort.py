# For getting range
def createList(start, end):
    lists = []
    while start < end:
        lists+= [start]
        start+=1
    return lists


# method for seelction sort
def selectn_sort(num, size):
    i = 0
    while i<size: 
        minposn = i
        j = i
        while j < size: 
            if num[j] < num[minposn]:
                minposn = j
            j += 1
        tmp = num[i]
        num[i] = num[minposn]
        num[minposn] = tmp
        i+=1
num = []

# Method for checking the size can't be a -ve number
def get_size():
    while True:
        global size
        ssize=int(input("Enter the size of the list : "))
        try:
            size = int(ssize)
            if size >= 0 and size!= -0:
                break
            else:
                print("size can't be negative, try again")
        except ValueError:
            print("size must be a number, try again")
    return size

size = get_size()
 

# for getting range for unsorted list
listsx2 = createList(0, size)

# for unsorted list 
for i in listsx2:
    item=int(input("Enter item: "))
    num[:] = num[:] + [item]
print("Unsorted List :",num)

selectn_sort(num, size)

print("Sorted List :",num)
