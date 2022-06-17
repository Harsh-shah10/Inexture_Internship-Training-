# For getting range
def createList(start, end):
    lists = []
    while start < end:
        lists+= [start]
        start+=1
    return lists


def bubble_sort(num, size):
    #2. outer-loop for repeating the loop 1.
    i = size-1
    while i >= 0:
        #1. for getting the biggest elemetn in the end
        j=0
        while j < i: 
            if num[j] > num[j+1]: # comparing the items 
                tmp = num[j]
                num[j] = num[j+1]
                num[j+1] = tmp
            j+=1
        i-=1
num = []

# Method for checking the size can't be a -ve number
def get_size():
    while True:
        global size
        ssize=int(input("Enter the size of the list : "))
        try:
            size = int(ssize)
            if size >= 0:
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

bubble_sort(num, size)

print("Sorted List :",num)
