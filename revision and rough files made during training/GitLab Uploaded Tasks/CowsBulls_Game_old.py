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
    for i in range(4):
        x = random.randrange(0,9)
        num_lst = num_lst+[x] # adding items to num_lst
    if len(num_lst)>len(set(num_lst)): # here set will remove the duplicate items 
        # deleting list using *= 0 if the 4 items are not unique in the list
        num_lst *= 0
        MakeRandomNumber()

MakeRandomNumber()

# for converting the no. generated inside the lst to a single integer
 
no2 = '' # using string concatenation 
for i in num_lst: 
    no2 += str(i) #number generated in the form of string


# cow bull method
def cowbull():
    global no2

    #for getting range
    listsx = createList(0,4)  

    cow=0 #  Correct number guessed at correct place - COW
    bull=0 #  Correct number guessed at wrong place - BULL
    for x in listsx:
        if guess[x]==no2[x]:
            cow+=1
        elif guess[x] in no2:
            bull+=1
        x+=1
    print(f"Cow: {cow} and Bull: {bull}")

tries=0

while True:
    tries+=1
    #print("generated no2 : ",no2)
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
