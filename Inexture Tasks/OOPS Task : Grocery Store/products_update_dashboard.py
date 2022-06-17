from validation import *
from product_update import PUpdateMethods
from admin import AdminMethods

class Product_update:
    # for customer functionality
    def __init__(self,usr_name,c_id,p_id):
        self.usr_name = usr_name
        self.c_id = c_id
        self.p_id = p_id

    def pUpdate_dashboard(self):
        print(f" --| {self.p_id} selected Suceessfully |-- ")
        while True:
            
            print("\n*Product Update Dashboard*")
            print('  Enter 1: Update Product Name')
            print('  Enter 2: Update Product Price')
            print('  Enter 3: Update Product Details [kg/gm]')
            print('  Enter 4: Update Available Quantity')
            print('  Enter 5: Update Available Brand')
            print('  Enter 6: Update Category id')
            print('  Enter 7: For Exit')

            while True:
                user_choice = input("Enter your choice : ")
                if user_choice.isnumeric() == True:
                    user_choice=int(user_choice)
                    break
                else:
                    print('Invalid Choice')

            if user_choice==1:

                update_product_name = PUpdateMethods(self.usr_name)
                p_name = input("Enter new product name : ")
                while not validate_string(p_name):
                    print("Invalid Input!!")
                    p_name = input("Enter new product name : ")
                update_product_name.update_Pname(p_name.lower(),self.c_id,self.p_id)
                print(f"!! {p_name}, Product name updated Successfully !! ")

                           
            elif user_choice==2:

                update_product_price = PUpdateMethods(self.usr_name)
                p_price = input("Enter new price : ")
                while not validate_int(p_price):
                    print("Invalid Input!!")
                    p_price = input("Enter new price : ")
                update_product_price.update_Pprice(p_price,self.c_id,self.p_id)
                print(f"!! {p_price}, Price updated Successfully !! ")



            elif user_choice==3:

                update_p_details = PUpdateMethods(self.usr_name)
                p_details = input("Enter new product details [kg] [gm]: ")
                while not validate_empty(p_details):
                    print("Invalid Input!!")
                    p_details = input("Enter new product details [kg] [gm]: ")
                update_p_details.update_Details(p_details,self.c_id,self.p_id)
                print(f"!! {p_details}, Details updated Successfully !! ")

                    
            elif user_choice==4:
                
                update_quantity = PUpdateMethods(self.usr_name)
                p_quantity = input("Available Quantity [STOCK] : ") 
                while not validate_int(p_quantity):
                    print("Invalid Input!!")
                    p_quantity = input("Available Quantity [STOCK] : ")
                update_quantity.update_Pquanity(p_quantity,self.c_id,self.p_id)
                print(f"!! {p_quantity}, Quantity updated Successfully !! ")


            elif user_choice==5:
                
                update_brand_details = PUpdateMethods(self.usr_name)
                p_brand = input("Enter new brand name : ")
                while not validate_string(p_brand):
                    print("Invalid Input!!")
                    p_brand = input("Enter new brand name : ")
                update_brand_details.update_Brand(p_brand.lower(),self.c_id,self.p_id)
                print(f"!! {p_brand}, Brand Name updated Successfully !! ")

              
            elif user_choice==6:
                update_product_category = PUpdateMethods(self.usr_name)

                vew_cat = AdminMethods(self.usr_name)
                c_ids = vew_cat.view_categories()
                c_id = input("Select the category : ")
                while not validate_int(c_id) or not (c_id in c_ids):
                    print("Invalid Input!!")
                    c_id = input("Select the category : ")

                update_product_category.update_Pcategory(c_id,self.c_id,self.p_id)
                print(f"!! {c_id}, Category updated Successfully !! ")


            elif user_choice==7:
                break

            else:
                print("Invalid Choice. PLease Try Again")     
