# for importing Signup class 
from signup import Signup

# for importing Login class
from login import Login
from validation import *

class GStore:
    # for customer functionality
    def gstore_dashboard(self):
        while True:
            print("\n*Welcome to Grocery Store*")
            print('  Enter 1: For Signup')
            print('  Enter 2: For Login')
            print('  Enter 3: For Exit')

            while True:
                user_choice = input("Enter your choice : ")
                if user_choice.isnumeric() == True:
                    user_choice=int(user_choice)
                    break
                else:
                    print('Invalid Choice')

            if user_choice==1:
                signup_obj = Signup()
                usr_name = input("Enter User Name : ")
                while not validate_user_name(usr_name):
                    print("Invalid Input!!")
                    print("Username Jai_singh is invalid\nUsername Jai@5 is invalid\nUsername jai12345 is valid\nUsername jai_singh is valid\n")
                    usr_name = input("Enter User Name : ")
                if signup_obj.check_user_name(usr_name):
                    # validate usr pass
                    usr_pass = input("Create password : ")
                    while not validate_password(usr_pass):
                        print("Invalid Input!!")
                        print("""Password should contain at least 1 lower case letter
                        Password should contain at least 1 Upper case letter
                        Password should contain at least 1 character case letter
                        Password should be minimum 4 characters long""")
                        usr_pass = input("Create password : ")
                     # validating first name
                    fn = input(f"Enter your first name : ")
                    while not validate_name(fn):
                        print("Invalid Input!! first name should always be a string")
                        fn = input(f"Enter your first name : ")
                    # validation last name
                    ln = input("Enter your last name : ")
                    while not validate_name(ln):
                        print("Invalid Input!! last name should always be a string")
                        ln = input("Enter your last name : ")
                    
                    # validate address
                    address = input("Enter your address : ")
                    while not validate_address(address):
                        print("Invalid Input!! Address should always be a string")
                        address = input("Enter your address : ")
                        
                    # validate email
                    email = input("Enter your email_id : ")
                    while not validate_email(email):
                        print("Invalid Input!! Enter a valid email Address")
                        email = input("Enter your email_id : ")

                    signup_obj.signup(usr_name,usr_pass,fn,ln,address,email)

            elif user_choice==2:
                login_obj = Login()

                # validating urername inp
                usr_name = input("Enter your user name : ")
                while not validate_empty(usr_name):
                    print("Invalid Input!!")
                    usr_name = input("Enter your user name : ")

                # validate usr pass inp
                usr_pass = input("Enter your password : ")
                while not validate_empty(usr_pass):
                    print("Invalid Input!!")
                    usr_pass = input("Enter your password : ")

                login_obj.user_login(usr_name,usr_pass)

            elif user_choice==3:
                break

            else:
                print("Invalid Choice. PLease Try Again")     

if __name__ == '__main__':
    g = GStore()
    g.gstore_dashboard()
