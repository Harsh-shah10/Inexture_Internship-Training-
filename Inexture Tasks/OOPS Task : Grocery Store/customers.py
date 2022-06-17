from regex import P
from query import Query
from validation import *

class CustomerMethods:
    def __init__(self,usr_name):
        self.usr_name = usr_name
   
    def get_user_info(self):
            query = Query()
            row = query.select_where(sql=None, table_name='user_data_table', cols='*',condn='user_name', inp=self.usr_name)
            return row

    def edit_profile_fname(self,fn):
        query = Query()

        #fetch user id 
        row1 = query.select_where(sql=None, table_name='user_data_table', cols='*',condn='user_name', inp=self.usr_name)
        fetches_usr_id = row1[0][0]
        #print("fetches_usr_id : ",fetches_usr_id)

        query.update_string(sql=None, table_name='user_data_table', cols=['user_first_name'], set=[fn], condn='user_name', inp=self.usr_name)
    
    def edit_profile_lname(self,ln):
        query = Query()

        #fetch user id 
        row1 = query.select_where(sql=None, table_name='user_data_table', cols='*',condn='user_name', inp=self.usr_name)
        fetches_usr_id = row1[0][0]
        #print("fetches_usr_id : ",fetches_usr_id)

        query.update_string(sql=None, table_name='user_data_table', cols=['user_last_name'], set=[ln], condn='user_name', inp=self.usr_name)
        
    def edit_profile_address(self,address):
        query = Query()

        #fetch user id 
        row1 = query.select_where(sql=None, table_name='user_data_table', cols='*',condn='user_name', inp=self.usr_name)
        fetches_usr_id = row1[0][0]
        #print("fetches_usr_id : ",fetches_usr_id)

        query.update_string(sql=None, table_name='user_data_table', cols=['user_address'], set=[address], condn='user_name', inp=self.usr_name)
        
    def edit_profile_email(self,email):
        query = Query()

        #fetch user id 
        row1 = query.select_where(sql=None, table_name='user_data_table', cols='*',condn='user_name', inp=self.usr_name)
        fetches_usr_id = row1[0][0]
        #print("fetches_usr_id : ",fetches_usr_id)

        query.update_string(sql=None, table_name='user_data_table', cols=['user_email'], set=[email], condn='user_name', inp=self.usr_name)
        
    
    def update_password(self,password):
        query = Query()
        query.update_string(sql=None, table_name='user_data_table', cols=['user_pass'], set=[password], condn='user_name', inp=self.usr_name)
        
    # for fetching the user_id
    def fetch_usr_id(self):
        query = Query()
        row1 = query.select_where(sql=None, table_name='user_data_table', cols='*',condn='user_name', inp=self.usr_name)
        usr_id = row1[0][0]
        return usr_id

    def get_wallet_balance(self):
        query = Query()
        # fetch user id
        row1 = query.select_where(sql=None, table_name='user_data_table', cols='*',condn='user_name', inp=self.usr_name)
        fetches_usr_id = row1[0][0]

        row = query.select_where(sql=None, table_name='wallet', cols='*',condn='user_id_fk', inp=fetches_usr_id)
        
        bal = row[0][1]
        return bal

    
    def check_wallet_balance(self):
        query = Query()
        # fetch user id
        row1 = query.select_where(sql=None, table_name='user_data_table', cols='*',condn='user_name', inp=self.usr_name)
        fetches_usr_id = row1[0][0]

        row = query.select_where(sql=None, table_name='wallet', cols='*',condn='user_id_fk', inp=fetches_usr_id)
      
        bal = row[0][1]
        return bal


    def add_wallet_balance(self,balance_input):
        query = Query()
         # fetch user id
        row1 = query.select_where(sql=None, table_name='user_data_table', cols='*',condn='user_name', inp=self.usr_name)
        fetches_usr_id = row1[0][0]

        # old wallet balance
        old_bal = query.select_where(sql=None, table_name='wallet', cols='*',condn='user_id_fk', inp=fetches_usr_id)
      
        old_wallet_bal = old_bal[0][1]
       
        x = True
        while True:
            # taking guess no as an input and converting it into a list
            # balance_input = input("Enter cash : ")
            if balance_input.isnumeric()==True:
                balance_input = int(balance_input)
                if balance_input>0:
                    # add balance to wallet
                    updated_balance =   old_wallet_bal + balance_input
                    query.update(sql=None, table_name='wallet', cols=['wallet_balance'], set=updated_balance, condn='user_id_fk', inp=fetches_usr_id) 
                break
            else:
                x = False
                break
        # updated wallet balance
        new_bal = query.select_where(sql=None, table_name='wallet', cols='*',condn='user_id_fk', inp=fetches_usr_id)
        updated_bal= new_bal[0][1]
        return old_wallet_bal,updated_bal,x


    def view_order_details(self):
        query = Query()
        row1 = query.select_where(sql=None, table_name='user_data_table', cols='*',condn='user_name', inp=self.usr_name)
        fetches_usr_id = row1[0][0]
        #print("fetches_usr_id ",fetches_usr_id)
        
        # fetching the order_id from the from  orders_data_table belong to user_id
        row_order = query.select_where(sql=None, table_name='orders_data_table', cols=['order_id'],condn='user_id_fk', inp=fetches_usr_id)
                
        if len(row_order)!=0:
            #fetches_order_id = row_order[0][0]
            #print("fetches_order_id ",fetches_order_id)
        
            # using the user_id to fetch the order_details
            row2 = query.select_where(sql=None, table_name='orders_data_table', cols='*',condn='user_id_fk', inp=fetches_usr_id)
            print("\n--| ALL Orders |--")
            order_ids = []
            for i in row2:
                print("\nOrder Id : ",i[0])
                order_ids.append(i[0])
                print("Total Cost : ",i[2])

            
            while True:
                get_order_id = input("\nEnter Order_Id to get to get detail info : ")
                if get_order_id.isnumeric()==True:
                    get_order_id = int(get_order_id)
                    if get_order_id in order_ids:
                        break
                    else:
                        print('Enter valid input')
                else:
                    print('Sorry ! Only integers Accepted')
                    
            
            print("\n          --| Order Details |--")

            # fetching product id from ordered_product  
            p_id_row = query.select_where(sql=None, table_name='ordered_products', cols=['product_id_fkey'],condn='order_id_fk', inp=get_order_id)

            p_id = []
            for i in p_id_row:
                p_id.append(i[0])

            for od_id in p_id:
                
                
                #fetching the product_details belonging to specific order id from order_details table
                sql = f"select *from order_details_save where product_id = {od_id} and order_id = {get_order_id}"
                product_data  = query.select_where(sql=sql)

                #print("product_data",product_data)
                print("-"*40) 
                for i in product_data: 
                    print("\nProduct ID : ",i[0])
                    print("Product Name : ",i[1])
                    print("Product Details : ",i[2])
                    print("Brand Name : ",i[4])
                    print("Price (per item) : ",i[3])
                    # fetching the quanity
                    sql = f"select product_quantity from ordered_products where order_id_fk = {get_order_id} and product_id_fkey = {i[0]}"
                    p_quan = query.select_where(sql=sql)
                    print("Quantity : ",p_quan[0][0])
                    
                
            # fetching the order id, cost and address
            print("-"*40)
            sql = f"select *from orders_data_table where user_id_fk = {fetches_usr_id} and order_id = {get_order_id} "
            product_data  = query.select_where(sql=sql)

            #print("product_data : ",product_data)
            print("          Order Id : ",product_data[0][0])
            print("          Address : ",product_data[0][1])
            print("          Total Cost : ",product_data[0][2])
            print("-"*40) 
            
        else:
            print(" -- No orders Placed -- ")
        

    def find_product(self,search_product):
        query = Query()
        product_name = query.search(sql=None, table_name='product_table', cols='product_name', find=search_product.lower())
        if len(product_name)==0:
            return product_name
        else:
            for i in product_name:
                product_details = query.select_where(sql=None, table_name='product_table', cols='*',condn='product_name', inp=i[0])
             
            return product_name,product_details