# for importing Products class
from products import Products
from admin import AdminMethods
from validation import *
from products_update_dashboard import Product_update
from query import Query

class Admin_Dashboard:
    def __init__(self,usr_name):
        self.usr_name = usr_name
        
    # for admin menu
    def admin_menu(self):
        while True:
            print("\n*Welcome to ADMIN Dashboard*")
            print('  Enter 1: View all available products')
            print('  Enter 2: Add new Products')
            print('  Enter 3: Delete Products')
            print('  Enter 4: View all Registered users')
            print('  Enter 5: Delete users')
            print('  Enter 6: View Profile')
            print('  Enter 7: View All Orders')
            print('  Enter 8: Add new category')
            print('  Enter 10: Check Wallet balance')
            print('  Enter 11: Updating product details')
            print('  Enter 12: Search Products')
            print('  Enter 13: Delete category')
            print('  Enter 14: For Exit')


            while True:
                user_choice = input("Enter your choice : ")
                if user_choice.isnumeric() == True:
                    user_choice=int(user_choice)
                    break
                else:
                    print('Invalid Choice')

            if user_choice==1:
                view_product_obj = Products(self.usr_name)
                x = view_product_obj.view_all_products_admin()
                print("\nAvailable list of products are : ")
                for i in x:
                    print("\nProduct ID : ",i[0])
                    print("Product Name : ",i[1])
                    print("Details : ",i[2])
                    print("Price : ",i[3])
                    print("Available Quantity [STOCK]: ",i[4])
                    print("Brand Name : ",i[5])
                    print("Category Id : ",i[6])
                    print()

            elif user_choice==2:
                add_new_pro_obj = AdminMethods(self.usr_name)

                # inserting new product into the product table
                # validation of products input
                p_name = input("Enter the product name : ").lower()
                while not validate_string(p_name):
                    print("Invalid Input!!")
                    p_name = input("Enter the product name : ").lower()
         
                p_details = input("Enter the product details : ")
                while not validate_empty(p_details):
                    print("Invalid Input!!")
                    p_details = input("Enter the product details : ")
                
                p_price = input("Enter the price : ")
                while not validate_int(p_price):
                    print("Invalid Input!!")
                    p_price = input("Enter the price : ")

                p_quantity = input("Enter quantity : ")
                while not validate_int(p_quantity):
                    print("Invalid Input!!")
                    p_quantity = input("Enter quantity : ")
                
                p_brand = input("Enter the brand name : ")
                while not validate_string(p_brand):
                    print("Invalid Input!!")
                    p_brand = input("Enter the brand name : ")
                
                # method to select a category 
                x = add_new_pro_obj.view_categories()

                print("\nAvailable list of Product Categories are : ")
                c_ids = []
                for i in x:
                    print("\nCategory ID : ",i[0])
                    c_ids.append(str(i[0]))
                    print("Category Name : ",i[1])

                c_id = input("Select the category : ")
                while not validate_int(c_id) or not (c_id in c_ids):
                    print("Invalid Input!!")
                    c_id = input("Select the category : ")

                add_new_pro_obj.add_new_Product(p_name,p_details,p_price,p_quantity,p_brand,c_id)
                print(f"- {p_name} : has been added successfully ! -")

            elif user_choice==3:
                del_pro_obj = AdminMethods(self.usr_name)

                # selecting the category
                x = del_pro_obj.view_categories()
                print("\nAvailable list of Product Categories are : ")
                c_ids = []
                for i in x:
                    print("\nCategory ID : ",i[0])
                    c_ids.append(str(i[0]))
                    print("Category Name : ",i[1])

                c_id = input("Select the category : ")
                while not validate_int(c_id) or not (c_id in c_ids):
                    print("Invalid Input!!")
                    c_id = input("Select the category : ")
                
                # selecting the product_id
                x = del_pro_obj.view_products(c_id)

                p_ids = []
                # fetching the data 
                print("\nAvailable list of products are : ")
                for i in x:
                    print("\nProduct ID : ",i[0])
                    p_ids.append(str(i[0]))
                    print("Product Name : ",i[1])
                    print("Quantity : ",i[2])
                    print("Product Price : ",i[3])
                    print("Available Quantity [STOCK]: ",i[4])
                    print("Brand Name : ",i[5])
                    print()


                p_id = input("Select the product ID : ")
                while not validate_int(c_id) or not (p_id in p_ids):
                    print("Invalid Input!!")
                    p_id = input("Select the product ID : ")

                del_pro_obj.delete_Product(p_id)
                print("Product deleted successfully ! -")

            elif user_choice==4:
                view_all_cust_obj = AdminMethods(self.usr_name)
                x = view_all_cust_obj.view_all_customers()
                c_ids = []
                print("\nList of Registered Customers are : ")
                for i in x:
                    print("------------------------------------------------")
                    print("\nCustomer ID : ",i[0])
                    c_ids.append(str(i[0]))
                    print("Customer First Name : ",i[3])
                    print("Customer Last Name : ",i[4])
                    print("Customer Address : ",i[5])
                    print("Customer Email : ",i[6])
                    print()
                print("------------------------------------------------")
                   
                


            elif user_choice==5:
                delete_customers_obj = AdminMethods(self.usr_name)

                # selecting the customer id
                c_ids = delete_customers_obj.view_all_customers()                
                c_id = input("Select the Customer_ID : ")
                while not validate_int(c_id) or not (c_id in c_ids):
                    print("Invalid Input!!")
                    c_id = input("Select the Customer_ID : ")

                delete_customers_obj.delete_customers(c_id)
                print("user/customer deleted successfully ! -")
               
            elif user_choice==6:
                get_details_obj = AdminMethods(self.usr_name)
                x = get_details_obj.get_user_info()

                print("\n: Admin Profile : ")
                for i in x:
                    print("\nAdmin Name : ",i[0])
                    print("Admin user_ID : ",i[3])

            elif user_choice==7:
                view_all_orders_obj = AdminMethods(self.usr_name)
                view_all_orders_obj.view_all_orders()


                
            elif user_choice==8:
                add_new_category_obj = AdminMethods(self.usr_name)
                
                x = add_new_category_obj.view_categories_name()

                print("\nAvailable list of Product Categories are : ")
                c_name = []
                for i in x:
                    print("\nCategory ID : ",i[0])
                    print("Category Name : ",i[1])
                    c_name.append(i[1])
                print()

                new_cat = input("\nEnter the new category name : ").lower()
                while not validate_string(new_cat) or (new_cat in c_name):
                    print("Invalid Input!!")
                    new_cat = input("\nEnter the new category name : ").lower()

                y = add_new_category_obj.add_category(new_cat)
                if y==True:
                    print("Category already exist !!")
                else:
                    print(f"Category {new_cat} : has been added successfully ! -")


  
            elif user_choice==10:
                wallet_balance_obj = AdminMethods(self.usr_name)
                x = wallet_balance_obj.get_wallet_balance()
                print("\nUser Wallet : ")
                print("Wallet Balance : ",x[0][0])

            
            elif user_choice==11:
                update_product_obj = AdminMethods(self.usr_name)
            
                # selecting the category
                x = update_product_obj.view_categories()
                print("\nAvailable list of Product Categories are : ")
                c_ids = []
                for i in x:
                    print("\nCategory ID : ",i[0])
                    c_ids.append(str(i[0]))
                    print("Category Name : ",i[1])
            

                c_id = input("Select the category : ")
                while not validate_int(c_id) or not (c_id in c_ids):
                    print("Invalid Input!!")
                    c_id = input("Select the category : ")
                
                x = update_product_obj.view_products(c_id)
                # selecting the product_id
                if len(p_ids)!=0:
                    p_ids = []
                    # fetching the data 
                    print("\nAvailable list of products are : ")
                    for i in x:
                        print("\nProduct ID : ",i[0])
                        p_ids.append(str(i[0]))
                        print("Product Name : ",i[1])
                        print("Quantity : ",i[2])
                        print("Product Price : ",i[3])
                        print("Available Quantity [STOCK]: ",i[4])
                        print("Brand Name : ",i[5])
                        print()

                    p_id = input("Select the product ID : ")
                    while not validate_int(c_id) or not (p_id in p_ids):
                        print("Invalid Input!!")
                        p_id = input("Select the product ID : ")

                    pupdate = Product_update(self.usr_name,c_id,p_id)
                    

                    pupdate.pUpdate_dashboard()
                   
                else:
                    print("!! No products available in category !!")

               
            elif user_choice==12:
                query = Query()
                search_product = AdminMethods(self.usr_name)
                
                p_name = input("Enter the product name : ")
                while not validate_string(p_name):
                    print("Invalid Input!!")
                    p_name = input("Enter the product name : ")

                x = search_product.find_product(p_name)

                print("\n --|: Search Results :|-- ")
                if len(x)==0:
                    print("product not found")
                else:
                    for i in x:
                        product_details = query.select_where(sql=None, table_name='product_table', cols='*',condn='product_name', inp=i[0])
                        for i in product_details:
                            print("\nProduct ID : ",i[0])
                            print("Product Name : ",i[1])
                            print("Details : ",i[2])
                            print("Price : ",i[3])
                            print("Available Quantity [STOCK]: ",i[4])
                            print("Brand Name : ",i[5])
                            print("Category Id : ",i[6])
                            print()

       

            elif user_choice==13:
                print()
                
                del_category_obj = AdminMethods(self.usr_name)
                print("--| Select the category ID you wanna Delete |--")
                x = del_category_obj.view_categories()
                
                print("\nAvailable list of Product Categories are : ")
                c_ids = []
                for i in x:
                    print("\nCategory ID : ",i[0])
                    c_ids.append(str(i[0]))
                    print("Category Name : ",i[1])


                c_id = input("\nSelect the category ID : ")
                while not validate_int(c_id) or not (c_id in c_ids):
                    print("Invalid Input!!")
                    c_id = input("Select the category ID : ")

                x = del_category_obj.delete_category(c_id)
                if len(x)==0:
                    print("!! Category Deleted Successfully !!")
                else:
                    print("Cannot delete category. As its consist of products!!")
            

            elif user_choice==14:
                break
            else:
                print("Invalid Choice. PLease Try Again")     