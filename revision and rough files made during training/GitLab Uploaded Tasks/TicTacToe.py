import random

# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

def selectRandom(lst):
    r = random.randrange(0,findLen(lst))
    return lst[r]
    
# printing the tic tac toe board
def printBoard(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[1], board[2], board[3]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[4], board[5], board[6]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[7], board[8], board[9]))
    print("\t     |     |")
    print("\n")

# checking if the space is free on the board or not
def free_space(posn):
    if board[posn] == ' ':
        return True
    else:
        return False

# For checking whether X or O can be inserted at the specific position or not
# mark : refers to "X" or "O" on the board
def insert_Mark(mark, posn):
    print()
    if free_space(posn):
        board[posn] = mark
        printBoard(board)
    else:
        print("Place already occupied")   
        posn = input("Please enter new posn:  ")
        if posn.isnumeric() == True:
            posn = int(posn)
            if posn>=1 and posn<=9:
                insert_Mark(mark, posn)
            else:    
                print("Invalid positions")
        else:
            print('Sorry ! Only integers Accepted')

# taking all the place on the board to check for the winning condition
def check_win():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def check_draw():
    for i in board:
        if (board[i] == ' '):
            return False
    return True

def player_move(player):
    while True:
        posn = input("Enter the posn for '{}':  ".format(player))
        if posn.isnumeric() == True:
            posn = int(posn)
            if posn>=1 and posn<=9:
                insert_Mark(player, posn)
                break
            else:
                print("Invalid positions")
        else:
            print('Sorry ! Only integers Accepted')

def cmp_move():
    possible_move = []
    for x in board:
        if board[x] == ' ': # if space empty add the mark
            possible_move+=[x]
    ## print("avail spaces : ",possible_move) # available moves
    move = 0

    for option in ['O', 'X']: 
    # both '0' and 'X' will be checked here
        for i in possible_move:
            board[i] = option
            if check_win():
                board[i] = ' '
                move = i
                return move
            board[i] = ' '

    # 5th position will be taken automatically if empty
    if 5 in possible_move:
        move = 5
        return move

    corner = []
    for i in possible_move:
        if i in [1,3,7,9]:
            corner+=[i]
            
    if findLen(corner) > 0:
        move = selectRandom(corner)
        return move

    edge = []
    for i in possible_move:
        if i in [2,4,6,8]:
            edge+=[i]
            
    if findLen(edge) > 0:
        move = selectRandom(edge)
    return move


board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

printBoard(board)
print("All the available Positions on Board are as follows: ")
print("1, 2, 3 \n4, 5, 6 \n7, 8, 9\n")
player = 'X'
bot = 'O'

global firstComputerMove
# for choosing Who will go first the Computer/Bot or the Player(Human)
firstComputerMove = True

print("-----------------------------------------")
print("For 2 player game : Press 1")
print("For playing against Computer : Press 2")
print("-----------------------------------------")

def menu():
    n = input("\nEnter your choice 1 or 2 : ")
    set = n.isnumeric()  
    while not check_win(): 
        if set==True:
            n = int(n)   

            if n == 1:

                player_move("X")
                if check_win():
                    print('X won')
                    break
                if (check_draw()):
                    print("--Match has been Draw--")
                    break

                player_move("O")
                if check_win():
                    print('O won')
                    break
                if (check_draw()):
                    print("--Match has been Draw--")
                    break
            
            elif n == 2:
                # firstComputerMove : for who will take the chance first the user or computer 
                if firstComputerMove:
                    board[cmp_move()] = 'O'

                    printBoard(board)
                    if check_win():
                        print('O won')
                        break
                    if (check_draw()):
                        print("--Match has been Draw--")
                        break

                    player_move(player)
                    if check_win():
                        print('X won')
                        break
                    if (check_draw()):
                        print("--Match has been Draw--")
                        break
                else:

                    player_move(player)
                    if check_win():
                        print('X won')
                        break
                    if (check_draw()):
                        print("--Match has been Draw--")
                        break
                    
                    # for priniting the board
                    board[cmp_move()] = 'O'
                    printBoard(board)
                    if check_win():
                        print('O won')
                        break
                    if (check_draw()):
                        print("--Match has been Draw--")
                        break
            else: 
                print("Invalid Input. Choose between option 1 or option 2")
                menu()           
        else:
            print("Sorry ! Only integers Accepted")
            menu()

# calling the menu 
menu()