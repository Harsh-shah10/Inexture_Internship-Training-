from html2text import element_style
from products import Products
from customers import CustomerMethods
from cart import CartMethods
from validation import *


class Customer_Dashboard:
    # for customer menu
    def __init__(self,usr_name):
        self.usr_name = usr_name

    def customer_menu(self):
        while True:
            print("\n*Welcome to Customer Dashboard*")
            print('  Enter 1: View all available products')
            print('  Enter 2: Select product categories \n           [Select & add Product to cart]')
            print('  Enter 3: View Profile')
            print('  Enter 4: For viewing order details')
            print('  Enter 5: View Cart')
            print('  Enter 6: Place Order')
            print('  Enter 7: Add Wallet balance')
            print('  Enter 8: Check Wallet balance')
            print('  Enter 9: Edit Profile')
            print('  Enter 10: Update Password')
            print('  Enter 11: Search Product')
            print('  Enter 12: Del Items from cart')
            print('  Enter 13: For Exit')

            while True:
                user_choice = input("Enter your choice : ")
                if user_choice.isnumeric() == True:
                    user_choice=int(user_choice)
                    break
                else:
                    print('Invalid Choice')

            if user_choice==1:
                view_product_obj = Products(self.usr_name)
                x = view_product_obj.view_all_products()
                print("\nAvailable list of products are : ")
                for i in x:
                    print("\nProduct ID : ",i[0])
                    print("Product Name : ",i[1])
                    print("Details : ",i[2])
                    print("Price : ",i[3])
                    #print("Available Quantity [STOCK]: ",i[4])
                    print("Brand Name : ",i[5])
                    print("Category Id : ",i[6])
                    print()

            elif user_choice==2:
                view_category_obj = Products(self.usr_name)

                # for selecting the cat_id
                x = view_category_obj.view_categories()

                print("-------------------------------------------")
                print("\nAvailable list of Product Categories are : ")
                c_ids = []
                for i in x:
                    print("\nCategory ID : ",i[0])
                    c_ids.append(str(i[0]))
                    print("Category Name : ",i[1])
                print("-------------------------------------------")
                print("    Enter 'exit' to return to Dashboard")
                print("-------------------------------------------")
               
                c_id = input("Select the category : ")
                while not validate_int(c_id) or not (c_id in c_ids):
                    
                    if c_id=='exit':
                        break
                    print("Invalid Input!!")
                    c_id = input("Select the category : ")

                if c_id!='exit':
                    print(f"\n--|Do you want to place a order|--")
                    choice = input("Press 1 : For Yes\nPress Anything : For No \nchoice :")

                    y = view_category_obj.view_products(c_id)
                    p_ids = []
                    # fetching the data 

                    if choice == "1":
                        print("\nAvailable list of products are : ")
                        for i in y:
                            print("\nProduct ID : ",i[0])
                            p_ids.append(str(i[0]))
                            print("Product Name : ",i[1])
                            print("Quantity : ",i[2])
                            print("Product Price : ",i[3])
                            #print("Available Quantity [STOCK]: ",i[4])
                            print("Brand Name : ",i[5])
                            print()
                        print("\n--|Enter Product_id of products to Add to cart |--")
                        add_to_cart_obj = CartMethods(self.usr_name)
                        add_to_cart_obj.add_to_cart(c_id)

      

            elif user_choice==3:
                get_details_obj = CustomerMethods(self.usr_name)
                x = get_details_obj.get_user_info()
                print("\nUser Profile : ")
                for i in x:
                    print("\nUser Id : ",i[1])
                    print("First Name : ",i[3])
                    print("Last Name : ",i[4])
                    print("Address : ",i[5])
                    print("Email : ",i[6])


            elif user_choice==4:
                get_order_details_obj = CustomerMethods(self.usr_name)
                get_order_details_obj.view_order_details()

           
            elif user_choice==5:
                view_cart_obj = CartMethods(self.usr_name)
                print('\n-------|Cart|--------')
                view_cart_obj.view_cart()
            
            elif user_choice==6:
                place_order_obj = CartMethods(self.usr_name)
                place_order_obj.place_order()
            
            # add balance
            elif user_choice==7:
                add_wallet_balance_obj = CustomerMethods(self.usr_name)
                
                print("------------------------------------")
                print("Enter 'exit' to return to Dashboard")
                print("------------------------------------")
                balance_input = input("Enter cash : ")

                if balance_input!='exit':
                    x = add_wallet_balance_obj.add_wallet_balance(balance_input)

                    if x[2]==True:
                        print("\n     : User Wallet : ")
                        print("Old Wallet Balance : ",x[0])
                        print("Updated Wallet Balance : ",x[1])
                    else:
                        print('Sorry ! Only integers Accepted')


            # check balance
            elif user_choice==8:
                wallet_balance_obj = CustomerMethods(self.usr_name)
                x = wallet_balance_obj.get_wallet_balance()
                print("\n     : User Wallet : ")
                print("Wallet Balance : ",x)


            elif user_choice==9:
                edit_profile_obj = CustomerMethods(self.usr_name)

                print("\n --|Current Profile Details|-- ")
       
                view = CustomerMethods(self.usr_name)
                x = view.get_user_info()
                print("\nUser Profile : ")
                for i in x:
                    print("\nUser Id : ",i[1])
                    print("First Name : ",i[3])
                    print("Last Name : ",i[4])
                    print("Address : ",i[5])
                    print("Email : ",i[6])

                print("\n --| Profile Update Dashboard |-- ")
                print('  Enter 1: To update First Name')
                print('  Enter 2: To update Last Name')
                print('  Enter 3: To update Address')
                print('  Enter 4: To update Email ID')
                print('  Enter 5: To Exit')
                
                while True:
                    choice = input("Enter your choice : ")
                    if choice=='5':
                            break
                    if choice.isnumeric() == True:
                        choice=int(choice)
                        
                        if choice<5:
                            print("\n --|Enter New details|-- ")
                            break
                        else:
                            print("Invalid Input !!")
                    else:
                        print('Invalid Choice')

                

                if choice==1:
                        # validating first name
                    fn = input(f"Enter your first name : ")
                    while not validate_name(fn):
                        print("Invalid Input!! first name should always be a string")
                        fn = input(f"Enter your first name : ")

                    edit_profile_obj.edit_profile_fname(fn)
                    print(f"!! Dear {self.usr_name}, Your First Name updated Successfully !! ")

                elif choice==2:
                        # validation last name
                    ln = input("Enter your last name : ")
                    while not validate_name(ln):
                        print("Invalid Input!! last name should always be a string")
                        ln = input("Enter your last name : ")
                    
                    edit_profile_obj.edit_profile_lname(ln)
                    print(f"!! Dear {self.usr_name}, Your Last Name updated Successfully !! ")


                elif choice==3:
                    # validate address
                    address = input("Enter your address : ")
                    while not validate_address(address):
                        print("Invalid Input!! Address should always be a string")
                        address = input("Enter your address : ")
                    
                    edit_profile_obj.edit_profile_address(address)
                    print(f"!! Dear {self.usr_name}, Your address updated Successfully !! ")

                
                elif choice==4:
                    # validate email
                    email = input("Enter your email_id : ")
                    while not validate_email(email):
                        print("Invalid Input!! Enter a valid email Address")
                        email = input("Enter your email_id : ")

                    edit_profile_obj.edit_profile_email(email)
                    print(f"!! Dear {self.usr_name}, Your email updated Successfully !! ")

               
                    
                

            elif user_choice==10:
                change_pass = CustomerMethods(self.usr_name)

                # validate usr pass inp
                usr_pass = input("Enter your new password : ")
                while not validate_password(usr_pass):
                    print("Invalid Input!!")
                    print("""Password should contain at least 1 lower case letter
                    Password should contain at least 1 Upper case letter
                    Password should contain at least 1 character case letter
                    Password should be minimum 4 characters long""")
                    usr_pass = input("\nEnter your new password : ")

                change_pass.update_password(usr_pass)
                print(f"!! Dear {self.usr_name}, Your Password updated Successfully !! ")


            elif user_choice==11:
                search_product = CustomerMethods(self.usr_name)
                
                p_name = input("Enter the product name : ")
                while not validate_string(p_name):
                    print("Invalid Input!!")
                    p_name = input("Enter the product name : ")

                print("\n     --|: Search Results :|-- ")
                x = search_product.find_product(p_name)
                if len(x)==0:
                    print("\n        product not found")
                else:
                    if len(x[0])!=0:
                        for i in x[1]:
                            print("\nProduct ID : ",i[0])
                            print("Product Name : ",i[1])
                            print("Details : ",i[2])
                            print("Price : ",i[3])
                            print("Available Quantity [STOCK]: ",i[4])
                            print("Brand Name : ",i[5])
                            print("Category Id : ",i[6])
                            print()

            elif user_choice==12:
                del_item_cart = CartMethods(self.usr_name)
                del_item_cart.del_item_from_cart()

               

            elif user_choice==13:
                break

            else:
                print("Invalid Choice. PLease Try Again")     
