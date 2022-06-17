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
#no2 = input("Enter the random no : ")

# taking no2 as an input and converting it into a list
no_2 = []
no_2.extend(no2)
#print("no2 list : ",no_2)

cow=0 #  Correct number guessed at correct place - COW
bull=0 #  Correct number guessed at wrong place - BULL

def cowbull(cow,bull):
    tmp = []
    for i in range(4):
        tmp.append(no_2[i])
    
    # -----cow code-----
    for i in range(4):
        if guess[i]==no_2[i]:
            cow+=1
            tmp[i]='#'
            guess[i] = '*'

    # removing the duplicaate values from the list
    x = list(set(tmp))

    # ------bull code----
    for i in range(4):
        if guess[i] in tmp:
            tmp.remove(guess[i])
            bull+=1
            #print(f"cow {cow}, bull :  {bull}")
    print(f"cow {cow}, bull :  {bull}")
    
tries=0
while True:
    #print("generated no2 : ",no2)

    # for validation of taking numbers as inputs are Integers
    while True:
        # taking guess no as an input and converting it into a list
        guess_no = input("Enter the number : ")
        if guess_no.isnumeric()==True:
            break
        else:
            print('Sorry ! Only integers Accepted')

    if len(guess_no)!=4 :
        print("Please enter 4 digit no.")
    else:
        if guess_no==no2:
            tries+=1
            print("You have guessed the Number Correctly")
            print(f"you WON in {tries} tries")
            break
        else:
            tries+=1
            guess = []
            guess.extend(guess_no)
            #print("Guess list : ",guess)
            cowbull(cow,bull)




