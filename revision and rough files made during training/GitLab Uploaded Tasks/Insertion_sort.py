# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

# For getting range
def createList(start, end):
    lists = []
    while start < end:
        lists+= [start]
        start+=1
    return lists


# method for Insertion Sort
def insertion_sort(List):

    #for getting range
    listsx = createList(1,findLen(List))  

    # start of insertion sort method
    for i in listsx: #we assume in InsertnSort that our 1st ele is sorted
        k = List[i]
        j = i-1
        while j>=0 and k<List[j]:
            List[j+1]=List[j]
            j=j-1
        else:
            List[j+1]=k #swapping 

List = []

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

get_size()
 
# for getting range for unsorted list
listsx2 = createList(0, size)

# unsorted list
for i in listsx2:
    item=int(input("Enter item: "))
    List[:] = List[:] + [item]
print("Unsorted List :",List)

insertion_sort(List)

print("Sorted List :",List)
    
