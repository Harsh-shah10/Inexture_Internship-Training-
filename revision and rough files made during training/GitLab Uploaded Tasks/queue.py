queue = [] # uses FIFO

# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

# Method for checking the size can't be a -ve number
def get_queue_size():
    while True:
        global queue_size
        ssize=int(input("Enter the size of the Queue : "))
        try:
            queue_size = int(ssize)
            if queue_size >= 0 and queue_size!= -0: # for also handling division by 0 error
                break
            else:
                print("size can't be negative, try again")
        except ValueError:
            print("size must be a number, try again")
    return queue_size

get_queue_size()

while True:

    global queue_size

    print("--> Queue Operations <--")
    print("\t1. Enqueue\n\t2. Dequeue\n\t3. Peek\n\t4. Exit")

    try:
        choice = int(input("Enter your choice from 1-4 : "))
        
    except ValueError: # for value invalid characters as input
        print("Invalid choice. Please enter your choice from 1-4 : ")
        choice = int(input("Enter your choice from 1-4 : "))

    if choice==1:
        if findLen(queue)<= (queue_size-1):
            element= input("Enter the element you want to insert into queue : ")
            queue = queue+[element]
            print("queue =",queue)
        else:
            print("**[Overflow]**Queue if FULL Dude")
            print("Queue =",queue)
            
    elif choice==2:
        if findLen(queue)==0:
            print("**[Underflow]**Queue is EMPTY Dude you can't Dequeue it")
        else:
            print("Deleted element is : ",queue[0]) #Dequeue: Removes an item from the queue FIFO
            queue = queue[1:]
        
        print("queue =",queue)
        
    elif choice==3:
        if findLen(queue)==0:
            print("queue is EMPTY ")
        else:
            print("Element present at Top of queue is : ",queue[0])
         # peep() method : returns the element at the front 

        print("queue =",queue)
        
    elif choice==4:
        break
