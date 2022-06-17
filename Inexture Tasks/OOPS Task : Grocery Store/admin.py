from products import Products
from query import Query
from validation import *

class AdminMethods:
    def __init__(self,usr_name):
        self.usr_name = usr_name
   
    def add_new_Product(self,p_name,p_details,p_price,p_quantity,p_brand,c_id):
        query = Query()
        # cat id should be included into the set consisitng of carious catid
        store_data = (p_name,p_details,p_price,p_quantity,p_brand,c_id)
        cols = ('product_name','product_details','product_price','available_product_quantity','product_brand','category_id')
        table_name = 'product_table'
        query.insert(table_name, cols, store_data)
        

    def delete_Product(self,p_id):
        query = Query()

        # fetching the cart_id consisting of this p_id
        cart_id=query.select_where(sql=None, table_name='cart_products_table', cols=['cart_id_fk'],condn='product_id_fk', inp=p_id)
        if len(cart_id)!=0:
            #query.delete(sql=None, table_name='product_table', condn='product_id', inp=p_id)
            for cid in cart_id:
                query.delete(sql=None, table_name='cart_data_table', condn='cart_id', inp=cid[0])
          
        query.delete(sql=None, table_name='product_table', condn='product_id', inp=p_id)
        

    def view_all_customers(self):    
        query = Query()
        data = query.select(sql=None, table_name='user_data_table', cols='*')
        return data
     

    def view_categories(self):
        query = Query()
        data = query.select(sql=None, table_name='category_table', cols='*')
        return data

    def view_categories_name(self):
        query = Query()
        data = query.select(sql=None, table_name='category_table', cols='*')
        return data
        

    def view_products(self,c_id):
        query = Query()
        data = query.select_where(sql=None, table_name='product_table', cols='*', condn='category_id', inp=c_id)   
        return data


    def delete_customers(self,c_id):
        query = Query()
        query.delete(sql=None, table_name='user_data_table', condn='user_id', inp=c_id)

            
    def get_user_info(self):
        query = Query()

        data=query.select_where(sql=None, table_name='admin_data_table', cols='*',condn='admin_user_id', inp=self.usr_name)
        #sql = f'SELECT {cols} FROM {table_name} WHERE {condn} = {inp}'
        return data

    def get_wallet_balance(self):
        query = Query()
        # fetch user id
        row1 = query.select_where(sql=None, table_name='admin_data_table', cols='*',condn='admin_user_id', inp=self.usr_name)
        fetches_usr_id = row1[0][2]

        row = query.select_where(sql=None, table_name='admin_wallet', cols='*',condn='admin_id_fk', inp=fetches_usr_id)
        return row



    def view_all_orders(self):
    
        query = Query()
        row = query.select(sql=None, table_name='orders_data_table', cols='*')
        order_id = []
        print("\n         --| All Orders |--")
        for i in row:
            print(f"\n         Order Id : {i[0]}, User Id : {i[3]}")
            order_id.append(i[0])
            print("-"*40) 
            # fetching the customer data rtd to order
            sql = f'SELECT *FROM public.user_data_table WHERE user_id = {i[3]}'
            data=query.select_where(sql=sql)
            for j in data:
                print("Customer First Name : ",j[3])
                print("Customer Last Name : ",j[4])
                print("Customer Address : ",j[5])
                print("Customer Email : ",j[6])
            
        #** input the order id ::
        while True:
            get_order_id = input("\nEnter Order_Id to get to get detail info : ")
            if get_order_id.isnumeric()==True:
                get_order_id = int(get_order_id)
                if get_order_id in order_id:
                    break
                else:
                    print('Enter valid input')
                    return
            else:
                print('Sorry ! Only integers Accepted')
                return # to break the flow if invalid input is passed
        
        print("-"*40) 
        # fetching the user id using the order_id
        sql = f'SELECT user_id_fk FROM orders_data_table WHERE order_id = {get_order_id}'
        data=query.select_where(sql=sql)

        if len(data)!=0:
            u_id = data[0][0]
            print(f"\n       --| => Order Details <= |--")
            print("\n         Order Id : ",get_order_id)
            # fetching the customer data rtd to order
            sql = f'SELECT *FROM public.user_data_table WHERE user_id = {u_id}'
            data=query.select_where(sql=sql)
            for j in data:
                print("Customer First Name : ",j[3])
                print("Customer Last Name : ",j[4])
                print("Customer Address : ",j[5])
                print("Customer Email : ",j[6])
    
            # fetching the order items 
            sql = f"select product_id_fkey from ordered_products where order_id_fk = {get_order_id} "
            p_id_row=query.select_where(sql=sql)

            print("\n    --| Items List |--    ")
            total_cost = 0

            for od_id in p_id_row:
                
                sql = f"select * from order_details_save where product_id = {od_id[0]} and order_id = {get_order_id}" 
                product_data = query.select(sql=sql)
                #product_data = row[0][0]

                for k in product_data: 
                    print("\nProduct ID : ",k[0])
                    print("Product Name : ",k[1])
                    print("Detail: ",k[2])
                    print("Brand Name : ",k[4])
                    print("Price : ",k[3])
                    
                    # fetching the quanity
                    sql = f"select product_quantity from ordered_products where order_id_fk = {get_order_id} and product_id_fkey = {k[0]}"
                    p_quan = query.select_where(sql=sql)
                    print("Quantity : ",p_quan[0][0])
                    total_cost+=(k[3]*p_quan[0][0])
            
            print("\nTotal Cost : ",total_cost)

            print("+"*40) 
            print("\n             --         --")
        else:
            print("!! User does not exist !!")
            print("!! So no data is available regarding this order !!")


    def add_category(self,new_cat):
        self.view_categories()
        query = Query()
        data = query.select(sql=None, table_name='category_table', cols='*')
    
        x = False
        for i in data:
            if new_cat==i[1]:    
                x = True
                break
                
        
        if x==False:
            store_data = [new_cat]
            cols = ('category_name',)
            table_name = 'category_table'
            query.insert(table_name, cols, store_data)
            
        return x


    def delete_category(self,del_cat):
            self.view_categories()
            query = Query()
            
            data = query.select_where(sql=None, table_name='product_table', cols='*', condn='category_id', inp=del_cat)
        

            if len(data)==0:
                query.delete(sql=None, table_name='category_table', condn='category_id', inp=del_cat)

                # deleting the products with assigned del_cat id
                query.delete(sql=None, table_name='product_table', condn='category_id', inp=del_cat)

            return data
                

    def update_item_details(self,c_id,p_ids,p_id,p_name,p_details,p_price,p_quantity,p_brand):
        query = Query()
        if len(p_ids)==0:
            return
        
        # updating product details query
        query.update_string(sql=None, table_name='product_table', cols=['product_name','product_details','product_price','available_product_quantity','product_brand'], set=[p_name,p_details,p_price,p_quantity,p_brand], condn='product_id', inp=p_id)
        


    def find_product(self,search_product):
        query = Query()
        product_name = query.search(sql=None, table_name='product_table', cols='product_name', find=search_product.lower())
        #print(product_name[0])
        return product_name

            
'''np = AdminMethods()
np.add_new_Product()'''