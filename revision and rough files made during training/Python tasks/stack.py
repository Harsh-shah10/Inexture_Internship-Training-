def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False
        
def pop(stack):
    if isEmpty(stack):
        print("Stack is EMPTY Dude you can't POP any element")
    else:
        print("Deleted element is : ",stack.pop())
        
def peep(stack):
    if isEmpty(stack):
        print("Stack is EMPTY Dude you can't PEEK any element")
    else:
        print("Element present at Top of Stack is : ",stack[-1])  

stack = []

while True:
    print("--> Stack Operations <--")
    print("\t1. Push\n\t2. POP\n\t3. Peek\n\t4. Exit")

    try:
        choice = int(input("Enter your choice from 1-4 : "))
        
    except ValueError: # for value invalid characters as input
        print("Invalid choice. Please enter your choice from 1-4 : ")
        choice = int(input("Enter your choice from 1-4 : "))

    if choice==1:
        element= int(input("Enter the element you want to PUSH into stack : "))
        stack.append(element)
        print("Stack =",stack)
    elif choice==2:
        pop(stack) # no need to pass element so only one argument Stack
        print("Stack =",stack)
    elif choice==3:
        peep(stack) # no need to pass element so only one argument Stack
        print("Stack =",stack)
    elif choice==4:
        break


