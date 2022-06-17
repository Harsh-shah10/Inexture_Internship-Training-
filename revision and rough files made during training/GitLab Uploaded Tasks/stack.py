stack = []

# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

# Method for checking the size can't be a -ve number
def get_stack_size():
    while True:
        global stack_size
        ssize=int(input("Enter the size of the stack : "))
        try:
            stack_size = int(ssize)
            if stack_size >= 0 and stack_size!= -0: # for also handling division by 0 error
                break
            else:
                print("size can't be negative, try again")
        except ValueError:
            print("size must be a number, try again")
    return stack_size

get_stack_size()

while True:
    global stack_size


    print("--> Stack Operations <--")
    print("\t1. Push\n\t2. POP\n\t3. Peek\n\t4. Exit")

    try:
        choice = int(input("Enter your choice from 1-4 : "))
        
    except ValueError: # for value invalid characters as input
        print("Invalid choice. Please enter your choice from 1-4 : ")
        choice = int(input("Enter your choice from 1-4 : "))

    if choice==1:
        if findLen(stack)<= (stack_size-1):
            element= input("Enter the element you want to PUSH into stack : ")
            stack = stack+[element]
            print("Stack =",stack)
        else:
            print("**[Overflow]**Stack if FULL Dude")
            print("Stack =",stack)

    elif choice==2:
         # no need to pass element so only one argument Stack
        if findLen(stack)==0:
            print("**[Underflow]**Stack is EMPTY Dude you can't POP any element")
        else:
            print("Deleted element is : ",stack[-1])
            stack = stack[:-1]

        print("Stack =",stack)
        
    elif choice==3:
        if findLen(stack)==0:
            print("Stack is EMPTY Dude you can't PEEK any element")
        else:
            print("Element present at Top of Stack is : ",stack[-1]) 

        print("Stack =",stack)
        
    elif choice==4:
        break
