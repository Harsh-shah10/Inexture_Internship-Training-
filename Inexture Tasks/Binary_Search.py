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


# Implementing Insertion Sort to sort the Unsorted list 

def insertion_sort(List):

    # for getting range for unsorted list
    listsx2 = createList(1,findLen(List))
    
    for i in listsx2: #we assume in InsertnSort that our 1st ele is sorted
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
 
#global size


# for getting range for unsorted list
listsx3 = createList(0, size)
for i in listsx3:
    item=int(input("Enter item: "))
    List[:] = List[:] + [item]

#using insertion_sort method    
insertion_sort(List)

print("Sorted List :",List)

# Input to Binary Search should always be a sorted list
# binary search Implementation

def binary_search(num_search):
    result = False
    beg = 0
    end = findLen(List)-1
    while beg <= end:
        mid = (beg+end)//2  #index to array cannot be a float so // we can also use type casting here
        if List[mid] == num_search:
            print("Item is found at postiton : ",mid)
            result = True
            break
        elif num_search>List[mid]:
            beg = mid + 1
        else:
            end = mid - 1
    if result == False:
        print("Item not found")


num_search = int(input("Enter the item you want to search : ")) 
#num_search = input("Enter the item you want to search : ")

#using binary_search method
binary_search(num_search)
