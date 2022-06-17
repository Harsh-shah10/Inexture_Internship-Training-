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

# for generating 4 digit random number 
import random

num_lst = []
def MakeRandomNumber():
    global num_lst

    # for getting range for the random number
    listx1 = createList(0,4)
 
    for i in listx1:
        x = random.randrange(0,9)
        num_lst = num_lst+[x] # adding items to num_lst

MakeRandomNumber()
# for converting the no. generated inside the lst to a single integer
 
no2 = '' # using string concatenation 
for i in num_lst: 
    no2 += str(i) #number generated in the form of string

#no2 = "5116" #sample input [Test Case]
#print("no2 : ",no2)

# cow bull method
def cowbull():
    global no2

    listsx = createList(0,4)

    cow=0 #  Correct number guessed at correct place - COW
    bull=0 #  Correct number guessed at wrong place - BULL
    tmp = []
    for x in listsx:
        if guess[x]==no2[x]:
            cow+=1
            tmp+=[x]
    
    # adding each number of string as a single item into the no2l list
    no2l = []
    for i in no2:
        no2l+=i
    

    # for replacing the numbers with # which is indentified as Cow in the generated number
    for i in tmp:
        no2l[i]="#"

    for x in listsx:
        if guess[x] in no2l:
            bull+=1
    #print("no2 : ",no2)
    print(f"Cow: {cow} and Bull: {bull}")

tries=0

while True:
    tries+=1
    print("generated no2 : ",no2)
    guess=input("Enter ur guess:")
    if len(guess)!=4 :
        print("Please enter 4 digit no.")
    else:
        if guess==no2:
            print("You have guessed the Number Correctly")
            print(f"you WON in {tries} tries")
            break
        else:
            cowbull()