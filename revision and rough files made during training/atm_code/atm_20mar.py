import random

user_data_base = {	
    1:{
        "cc":10,"Bank":1,"name":"Harsh","balance":10000,"Transacn_Count":0,"dailyTransnLimit":40000,"ccpin":0000
    },
    2:{
        "cc":11,"Bank":2,"name":"Piyush","balance":10000,"Transacn_Count":0,"dailyTransnLimit":40000,"ccpin":1234
    }
}

admin_data_base = {
    1:{
        "cc":33334444,"name":"super-admin","ccpin":1010
    }
}

atm_data_base = {
    1:{
        'Bank_ID':1,'Location': 'Iscon','balance': 10000
    },
    2:{
        'Bank_ID':2,'Location': 'Vastrapur','balance': 10000
    },
}
bank_data_base = {
    1:{
        'Name': 'UCO Bank','ATM': [1],'user': [1]
    },
    2:{
        'Name': 'AXIS Bank','ATM': [2],'user': [2]
    }
}

TransnLimit = 10000

# method for checking cc
def cc_check():
    global card, user_id, admin_id,pin
    x = True 
    while x:

        while True:
            card = input("Enter your ATM card number : ")
            pin = input("Enter the ATM pin : ")
            if card.isnumeric() == True and pin.isnumeric()==True:
                card=int(card)
                pin=int(pin)
                break
            else:
                print('Sorry ! Only integers Accepted')

        for user_id in user_data_base:
            if user_data_base[user_id]['cc'] == card and user_data_base[user_id]['ccpin'] == pin:
                print(f"\nWelcome {card} {user_data_base[user_id]['name']}")
                x = False
                user_menu()
                break
    
        for admin_id in admin_data_base:
            if admin_data_base[admin_id]["cc"] == card and admin_data_base[admin_id]["ccpin"] == pin:
                print(f"Welcome {card} Admin")
                x = False
                admin_menu()
                break
    
        if x==True:
            print("Incorrect Details Entered. Please Try again")
            break

def list_atm():
    for i in atm_data_base:
        print(f'{i} {bank_data_base[atm_data_base[i]["Bank_ID"]]["Name"]}   ATM : {atm_data_base[i]["Location"]}')

def list_banks():
    for i in bank_data_base:
        print()
        print(str(i)+"\t"+ bank_data_base[i]['Name'])

def list_users():
    for i in user_data_base:
        print()
        print(str(i)+"\t"+ user_data_base[i]['name'])

# user menu
def user_menu():
    # checking cc and pin

    if user_data_base[user_id]['cc'] == card and user_data_base[user_id]['ccpin'] == pin:
        while True:
            print("\n*Available Operations are*")
            print('\nEnter 1: For Account Info')
            print('Enter 2: For PIN Change')
            print('Enter 3: For Withdrawal')
            print('Enter 4: For Deposit')
            print('Enter 7: Exit')

            while True:
                user_choice = input("Enter your choice : ")
                if user_choice.isnumeric() == True:
                    user_choice=int(user_choice)
                    break
                else:
                    print('Invalid Choice')


            if user_choice==1:
                get_user_details()
                
            elif user_choice==2:
                update_pin()
        
            elif user_choice==3:
                Withdraw()
    
            elif user_choice==4:
                deposit()
            elif user_choice==7:
                break
            else:
                print("Invalid Choice. PLease Try Again")     
    else:
        print("Invalid login details")

# for getting user details
def get_user_details():
    for i in user_data_base[user_id]:
        if i == 'Bank':
            print("{} : {}".format(i, bank_data_base[user_data_base[user_id][i]]['Name']))
        else:
            print("{} : {}".format(i, user_data_base[user_id][i]))

# updating the user Pin
def update_pin():
    user_data_base[user_id]['ccpin'] = int(input("Enter New ATM Pin : "))
    print("ATM Pin Updated Successfully!")


# method for deposting money through ATM
def deposit():
    if user_data_base[user_id]['Transacn_Count'] >= 4 or user_data_base[user_id]["dailyTransnLimit"]<0:
        print("\nDaily transcation limit reached")
        return
    list_atm()

    while True:
        SelectedATM = input("\nSelect ATM : ")
        deposit_amount = input("Enter amount : ")
        if SelectedATM.isnumeric() == True and deposit_amount.isnumeric() == True:
            SelectedATM=int(SelectedATM)
            deposit_amount=int(deposit_amount)
            break
        else:
            print('Invalid Choice & Invalid Input')
    
    if atm_data_base[SelectedATM]['Bank_ID'] != user_data_base[user_id]['Bank']:
        print("Sorry You cannot diposit money through this ATM")
        return

    if deposit_amount <= TransnLimit:
        user_data_base[user_id]['balance'] = user_data_base[user_id]['balance'] + deposit_amount
        print("Transcation successful")
        print("Balance : {}".format(user_data_base[user_id]['balance']))
        # updating trasn count
        user_data_base[user_id]["Transacn_Count"]+=1
        # updating dailyTransnLimit
        user_data_base[user_id]["dailyTransnLimit"]-=deposit_amount
    else:
        print("\nSorry ! Your request cannot be Processed.")
        print("One time Transaction Limit is : ", TransnLimit)

# method for withdrawing money through ATM
def Withdraw():
    if user_data_base[user_id]['Transacn_Count'] >= 4 or user_data_base[user_id]["dailyTransnLimit"]<0:
        print("\nDaily transcation limit reached")
        return
    
    list_atm()
    
    while True:
        SelectedATM = input("\nSelect ATM : ")
        if SelectedATM.isnumeric() == True:
            SelectedATM=int(SelectedATM)
            break
        else:
            print('Invalid Choice')

    
    withdraw_amount = int(input("Enter amount : "))
    if withdraw_amount > TransnLimit:
        print("\nSorry ! Your request cannot be Processed.")
        print("One time Transaction Limit is : ", TransnLimit)
        return
    elif withdraw_amount >= user_data_base[user_id]['balance']:
        print("\nInsufficient Account balance !!")
    elif withdraw_amount > atm_data_base[SelectedATM]['balance']:
        print("\nNot enough money in ATM")

        # for withdrawing money through user primary ATM
    elif atm_data_base[SelectedATM]['Bank_ID'] == user_data_base[user_id]['Bank']:
        user_data_base[user_id]['balance'] = user_data_base[user_id]['balance'] - withdraw_amount
        atm_data_base[SelectedATM]['balance'] -= withdraw_amount
        print(f"\n{withdraw_amount} Amount Withdrawn successfully")
        print(f"Remaining Account Balance : {user_data_base[user_id]['balance']}")

        # updating trasn count
        user_data_base[user_id]["Transacn_Count"]+=1

        # updating dailyTransnLimit
        user_data_base[user_id]["dailyTransnLimit"]-=withdraw_amount

        # for withdrawing money from different ATM  
    elif atm_data_base[SelectedATM]['Bank_ID'] != user_data_base[user_id]['Bank']:
        transactionFee = withdraw_amount*5/100
        if (withdraw_amount + transactionFee) <= user_data_base[user_id]['balance']:
            user_data_base[user_id]['balance'] = user_data_base[user_id]['balance'] - withdraw_amount - transactionFee
            atm_data_base[SelectedATM]['balance'] -= withdraw_amount
            print(f"\n{withdraw_amount} Amount Withdrawn successfully")
            print(f"\nTransaction Fee : {transactionFee}")
            print(f"Remaining Account Balance : {user_data_base[user_id]['balance']}")

        # updating trasn count
        user_data_base[user_id]["Transacn_Count"]+=1

        # updating dailyTransnLimit
        user_data_base[user_id]["dailyTransnLimit"]-= (withdraw_amount + transactionFee)

# admin menu
def admin_menu():
    # checking cc and pin

    if admin_data_base[admin_id]["cc"] == card and admin_data_base[admin_id]["ccpin"] == pin:
        while True:
            print("\n*Available Operations are*")
            print('Enter 1: For Account Info')
            print('Enter 2: Add New User to Bank')
            print('Enter 3: ADD New Bank')

            print('Enter 4: ADD Money to ATM')
            print('Enter 5: Insert New ATM')
            print('Enter 6: Update ATM')
            print('Enter 7: Delete ATM')

            print('Enter 8: For deleting Users from Database')
            print('Enter 9: Update User Details') 
            print('Enter 10: for exit')

         
            while True:
                user_choice=input("Enter your choice : ")
                if user_choice.isnumeric() == True:
                    user_choice=int(user_choice)
                    break
                else:
                    print('Invalid Choice')

          
            if user_choice==1:
                get_admin_details()

            elif user_choice==2:
                add_user()

            elif user_choice==3:
                add_New_bank()
                
            elif user_choice==4:
                admin_deposit()

            elif user_choice==5:
                Insert_ATM()

            elif user_choice==6:
                Update_ATM()

            elif user_choice==7:
                Delete_ATM()

            elif user_choice==8:
                delete_users()

            elif user_choice==9:
                Update_user_details()

            elif user_choice==10:
                break
            else:
                print("Invalid Choice. PLease Try Again")
    else:
        print("Invalid details")


# admin user details
def get_admin_details():
    for admin_id in admin_data_base:
        print(admin_data_base[admin_id])


# total no of users in user_data_base
def total_users():
    global total_user_id
    total_user_id = 0
    for i in user_data_base:
        total_user_id+=1

# add new user to bank 
def add_user():
    total_users()
    user_id = total_user_id + 1
    user_data_base[user_id] = {}
    user_data_base[user_id]['cc'] = random.randint(100, 999) 

    list_banks()
    user_data_base[user_id]['Bank'] = int(input("Select the bank : "))
    user_data_base[user_id]['name'] = input("Enter the name : ")
    user_data_base[user_id]['balance'] = int(input("Enter the Balance : "))
    user_data_base[user_id]['Transacn_Count'] = 0
    user_data_base[user_id]['dailyTransnLimit'] = 50000
    user_data_base[user_id]['ccpin'] = random.randint(1000, 9999)
    
    bank_data_base[user_data_base[user_id]['Bank']]['user'].append(user_id)
    print()
    for i in user_data_base[user_id]:
        print("{} : {}".format(i, user_data_base[user_id][i]))
    print(f"\nUser {user_data_base[user_id]['name']} Added Successfully")

def admin_deposit():
    list_atm()


    while True:
        SelectedATM = input("\nSelect ATM : ")
        amount = input("Enter amount : ")
        if SelectedATM.isnumeric() == True and amount.isnumeric() ==True:
            SelectedATM=int(SelectedATM)
            amount=int(amount)
            break
        else:
            print('Invalid Choice')

    atm_data_base[SelectedATM]['balance'] += amount
    print(f"\n{amount} Added Successfully")
    print("Available ATM Balance is : ",atm_data_base[SelectedATM]['balance'])


# total no of banks in bank_data_base
def total_banks():
    global total_bank
    total_bank = 0
    for i in bank_data_base:
        total_bank+=1

def add_New_bank():
    total_banks()
    bank_id = total_bank + 1
    newBank = input("Enter bank name : ")

    bank_data_base[bank_id] = {}
    bank_data_base[bank_id]['Name'] = newBank
    bank_data_base[bank_id]['ATM'] = []
    bank_data_base[bank_id]['user'] = []

def user_login():
    pass

def delete_users():
    list_users()

    while True:
        user_id = input("Enter the User Id : ")
        if user_id.isnumeric() == True:
            user_id=int(user_id)
            break
        else:
            print('Invalid Choice')


    if user_id not in user_data_base:
        print("No User found")
        return
    else:
        print(f" User { user_data_base[user_id]['name'] } ! Deleted Successfully")
        del user_data_base[user_id]
        

# total no of ATM in atm_data_base
def total_atms():
    global total_atm
    total_atm = 0
    for i in atm_data_base:
        total_atm+=1

# Inserting/Adding ATM to existing Banks
def Insert_ATM():

    list_banks()

    InpBankId = int(input("Enter bank ID : "))
    
    total_atms()

    atm_id = total_atm + 1
    atm_data_base[atm_id] = {}
    atm_data_base[atm_id]['Bank_ID'] = InpBankId
    atm_data_base[atm_id]['Location'] = input("Enter the Branch Name : ")
    atm_data_base[atm_id]['balance'] = int(input("Enter initial amount in ATM : "))
    bank_data_base[InpBankId]['ATM'].append(atm_id)
    print("ATM Added Successfully !")

# Deleting the existing ATM's
def Delete_ATM():
    list_atm()
    
    while True:
        AtmId = input("Enter ATM ID : ")
        if AtmId.isnumeric() == True:
            AtmId=int(AtmId)
            break
        else:
            print('Invalid Choice')


    if AtmId not in atm_data_base:
        print(f"No ATM found with ATM ID : {AtmId}")
        return
    else:
        bank_data_base[atm_data_base[AtmId]['Bank_ID']]['ATM'].remove(AtmId)
        del atm_data_base[AtmId]
        print("ATM Deleted Successfully")

# Updating The Existing ATM Balance
def Update_ATM():
    list_atm()
    
    while True:
        AtmId = input("Enter ATM ID : ")
        if AtmId.isnumeric() == True:
            AtmId=int(AtmId)
            break
        else:
            print('Invalid Choice')

    if AtmId not in atm_data_base:
        print(f"No ATM found with ATM ID : {AtmId}")
        return
    else:
        print("Change Existing ATM Balance")
        atm_data_base[AtmId]['balance'] = input("Enter New Balance : ")
        print("\nUpdation Completed Successfully !")
        print(f"New ATM Balance is {atm_data_base[AtmId]['balance']}")

# Update user details in the bank db
def Update_user_details():
    list_users()

    while True:
        user_id = input("Enter the User Id : ")
        if user_id.isnumeric() == True:
            user_id=int(user_id)
            break
        else:
            print('Invalid Choice')

    if user_id not in user_data_base:
        print("No User found")
        return
    else:    
        while True:
            print("Available Options : ")
            print("1. Update Old User Name")
            print("2. Update Bank")
            print("3. Update CC/ATM Pin")
            print("4. Update Transactions Count")
            print("5. Update Daily Transaction Limit")
            print("6. Exit")

            while True:
                userInput = input("Enter choice : ")
                if userInput.isnumeric() == True:
                    #userInput=int(userInput)
                    break
                else:
                    print('Invalid Choice')

            if userInput == "1":
                user_data_base[user_id]['name'] = input("Enter New Name : ")
            elif userInput == "2":
                bank_data_base[user_data_base[user_id]['Bank']]['user'].remove(user_id)
                list_banks()
                user_data_base[user_id]['bank'] = int(input("Enter New Bank ID : "))
                bank_data_base[user_data_base[user_id]['Bank']]['user'].append(user_id)
            elif userInput == "3":
                user_data_base[user_id]['ccpin'] = int(input("Enter New ATM Pin : "))
            elif userInput == "4":
                user_data_base[user_id]['Transacn_Count'] = int(input("Enter Transactions Count : "))
            elif userInput == "5":
                user_data_base[user_id]['dailyTransnLimit'] = int(input("Enter dailyTransnLimit : "))
            else:
                break        
while True:
    cc_check()