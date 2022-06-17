Cqueue=[]
front=-1
rear=0

# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

# Method for checking the size can't be a -ve number
def get_queue_size():
    while True:
        global len_queue
        ssize=int(input("Enter the size of the Circular Queue : "))
        try:
            len_queue = int(ssize)
            if len_queue >= 0 and len_queue!= -0:
                break
            else:
                print("size can't be negative, try again")
        except ValueError:
            print("size must be a number, try again")
    return len_queue

get_queue_size()


x = (rear+1)%len_queue
y = (front+1)%len_queue


def enqueue():
    global front, rear, Cqueue, len_queue
    if findLen(Cqueue)==len_queue:
        print("Circular Queue is full")
        
    elif front== -1:
        front=0
        rear=0
        element=input("enter an element:")
        Cqueue+=[element]
        print(Cqueue)
    else:
        rear=x
        element=input("enter an element:")
        Cqueue+=[element]
        print(Cqueue)

def dequeue():
    global front, rear, Cqueue, len_queue
    if findLen(Cqueue)==0:
        print("Circular Queue is empty")
    elif(front==rear):
        front=-1
        rear=-1
        print("deleted element is : ",Cqueue[0])
        Cqueue = Cqueue[1:]
        print(Cqueue)
    else:
        front=y
        print("deleted element is : ",Cqueue[0])
        Cqueue = Cqueue[1:]
        print(Cqueue)

def front():
    global Cqueue
    if findLen(Cqueue)==0:
        print("Circular Queue is empty")
    else:
        print(Cqueue[0])

def rearr():
    global Cqueue
    if findLen(Cqueue)==0:
        print("Circular Queue is empty")
    else:
        print(Cqueue[-1])


while True:

    
    print("--> CQueue Operations <--")
    print("\t1. Enqueue\n\t2. Dequeue\n\t3. Front\n\t4. Rear\n\t5. Exit")

    try:
        choice = int(input("Enter your choice from 1-5 : "))
        
    except ValueError: # for value invalid characters as input
        print("Invalid choice. Please enter your choice from 1-5 : ")
        choice = int(input("Enter your choice from 1-5 : "))

    if choice==1: # enqueue
        enqueue()

    elif choice==2: # dequeue
        dequeue()
            
    elif choice==3: # front
        front()
            
    elif choice==4: # rear
        rearr()
         
    elif choice==5:
        exit()
 
