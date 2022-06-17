def isEmpty(queue):
    if len(queue)==0:
        return True
    else:
        return False
   
def Dequeue(queue):
    if isEmpty(queue):
        print("Queue is EMPTY Dude you can't Dequeue it")
    else:
        print("Deleted element is : ",queue.pop(0)) #Dequeue: Removes an item from the queue FIFO


        
def peep(queue):
    if isEmpty(queue):
        print("queue is EMPTY ")
    else:
        print("Element present at Top of queue is : ",queue[0])
         # peep() method : returns the element at the front 
        
queue = [] # uses FIFO

while True:
    print("--> Queue Operations <--")
    print("\t1. Enqueue\n\t2. Dequeue\n\t3. Peek\n\t4. Exit")

    try:
        choice = int(input("Enter your choice from 1-4 : "))
        
    except ValueError: # for value invalid characters as input
        print("Invalid choice. Please enter your choice from 1-4 : ")
        choice = int(input("Enter your choice from 1-4 : "))

    if choice==1:
        element= int(input("Enter the element you want to insert into queue : "))
        queue.append(element)
        print("queue =",queue)
        
    elif choice==2:
        Dequeue(queue) # no need to pass element so only one argument Stack
        print("queue =",queue)
        
    elif choice==3:
        peep(queue) # no need to pass element so only one argument Stack
        print("queue =",queue)
        
    elif choice==4:
        break

   
