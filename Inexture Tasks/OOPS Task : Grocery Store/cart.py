from query import Query
from validation import *
from customers import CustomerMethods
#print(Database)

class CartMethods:
    def __init__(self,usr_name):
        self.usr_name = usr_name
     
    def add_to_cart(self,c_id):
        query = Query()

        # break the code if the category consist of no products
        check_pdt_in_cat = query.select_where(sql=None, table_name='product_table', cols='*',condn='category_id', inp=c_id)
        if len(check_pdt_in_cat)==0:
            print("\n !! No products are present in this Category right now !!")
            return

        row1=query.select_where(sql=None, table_name='user_data_table', cols='*',condn='user_name', inp=self.usr_name)
        f_usr_id = row1[0][0]
           
        # fetching all the user_id available in the cart_data_table
        row1=query.select_where(sql=None, table_name='cart_data_table', cols='*',condn='user_id_fk', inp=f_usr_id)
        #print("row1 :",row1)

        if len(row1)==0:
       
        # adding user_id to the cart_data_table
            store_data = [f_usr_id]
            cols = ['user_id_fk']
            table_name = 'cart_data_table'
            query.insert(table_name, cols, store_data)


        # fetching the cart id from the cart_data_table
        row1=query.select_where(sql=None, table_name='cart_data_table', cols='*',condn='user_id_fk', inp=f_usr_id)
        f_cart_id = row1[0][0]
        #print("f_cart_idf_cart_id ",f_cart_id)
  
        print('\n-------|ADD ITEMS TO Cart|--------')
        p_ids = self.view_products(c_id)
        
        p_id = input("Select the product ID : ")#most probably it will be int
        while not validate_int(c_id) or not (p_id in p_ids):
            print("Invalid Input!!")
            p_id = input("Select the product ID : ")

        # fetching the quantity in no
        q = self.fetch_quantity(p_id)   
        #print("Available product Quantity [STOCK]",q,type(q))
        if q>0:
            # fetch from cart_products_table with u_id and p_id as input
            #cart_data = query.select_where(sql=None, table_name='cart_products_table', cols='*', condn='product_id_fk', inp=p_id)

            sql = f"select * from cart_products_table where cart_id_fk = {f_cart_id} and product_id_fk = {p_id}" 
            cart_data = query.select(sql=sql)
            
            #print("cart_data",cart_data)

            # if the product is already added to the cart          
            if len(cart_data)!=0:  
                # if p_id is already added to the cart
                if int(p_id)==cart_data[0][1]:
                    # fetch from product data table
                    pdt_data = query.select_where(sql=None, table_name='product_table', cols='*', condn='product_id', inp=p_id)
                    
                    while True:
                        inp_quantity = input("Update quantity in Cart: ")
                        if inp_quantity.isnumeric()==True:
                            inp_quantity = int(inp_quantity)
                            break

                    current_quantity = pdt_data[0][4]-cart_data[0][2]
                    if inp_quantity<=current_quantity and inp_quantity>0:
                        #update_q = cart_data[0][2] + inp_quantity

                        # fetch cost of product
                        pcost = query.select_where(sql=None, table_name='product_table', cols=['product_price'], condn='product_id', inp=p_id)
                     
                        t_cost = inp_quantity * pcost[0][0]

                        #query.update(sql=None, table_name='cart_products_table', cols=['product_quantity'], set=update_q, condn='product_id_fk', inp=p_id)
                    
                        sql = f"UPDATE cart_products_table SET product_quantity={inp_quantity},total_cost={t_cost} WHERE product_id_fk={p_id} AND cart_id_fk={f_cart_id}"
                        query.update(sql=sql)
                         
                        print("\nProduct Quantity Updated successfully!!")
                        return
                    else:
                        if current_quantity==0:
                            print("\n!! You have already added the MAX Quantity of product to Cart !!")
                        elif inp_quantity==0:
                            print("Input Qunatity must be greater than 0")
                        else:
                            print(f"\nSorry!! We have only add {current_quantity} more quantity in Stock")
                        return
            else:
                # if some new product is added to the cart
                while True:
                    
                    inp_quantity = input("Select quantity : ")
                    if inp_quantity.isnumeric()==True:
                    
                        inp_quantity = int(inp_quantity)
                        if inp_quantity<=q and inp_quantity>0:
                            
                            # fetching the product price and storing it into cart_product_table
                            p_price = query.select_where(sql=None, table_name='product_table', cols=['product_price'],condn='product_id', inp=p_id)
                            pdt_cost = p_price[0][0]
                            total_cost = pdt_cost*inp_quantity
                            #print("total_cost ",total_cost)
                            p_id = int(p_id)

                            # storing the data inside the cart_product_table
                            # use where with & operator here
                          
                            sql = f"select product_id_fk from cart_products_table where product_id_fk = {p_id} and cart_id_fk = {f_cart_id}" 
                            check_pid_prsence = query.select(sql=sql)
                         
                            
                            if len(check_pid_prsence)==0:
                                store_data = (f_cart_id,p_id,inp_quantity,total_cost,pdt_cost)
                                cols = ['cart_id_fk','product_id_fk','product_quantity','total_cost','product_price']
                                table_name = 'cart_products_table'
                                query.insert(table_name, cols, store_data)
                                
                                print("\nProduct Added to cart successfully!!")
                                
                                return
                            
                        else:
                            #print("Invliad Input !!")
                            print(f"!! You can add MAX {q} quantities of the product to cart !! ")
                    else:
                        inp_quantity = input("Select quantity : ")          
        else:
            print("\nStock not availble !!")
            return


    def view_products(self,c_id):
        query = Query()
        data = query.select_where(sql=None, table_name='product_table', cols='*', condn='category_id', inp=c_id)
        p_ids = []
        for i in data:
            p_ids.append(str(i[0]))
        return p_ids

    def fetch_quantity(self,p_id):
        query = Query()
        data = query.select_where(sql=None, table_name='product_table', cols=['available_product_quantity'], condn='product_id', inp=p_id)
        return data[0][0]
    
    def view_cart(self):
        query = Query()
        
        # fetching the user_id from the user_name table
        row1 = query.select_where(sql=None, table_name='user_data_table', cols=['*'],condn='user_name', inp=self.usr_name)
        f_usr_id = row1[0][0]       
        #print("User id : ",f_usr_id)

        # fetching the cart id that belongs to the fetched_usr_id
        row1 = query.select_where(sql=None, table_name='cart_data_table', cols=['*'],condn='user_id_fk', inp=f_usr_id)
        
        
        if len(row1)==0:
            print("Cart is Empty")
            return row1

        else:
            # checking whether the cart_products_table
            cart_p_table = query.select_where(sql=None, table_name='cart_products_table', cols=['*'],condn='cart_id_fk', inp=row1[0][0])
      
            if len(cart_p_table)==0:
                print("Cart is Empty")
                return cart_p_table


        if len(row1)!=0:
            f_cart_id = row1[0][0]

            # update the cart in case the admin has updated the cost of the product
            p_id_incart = query.select_where(sql=None, table_name='cart_products_table', cols=['product_id_fk'],condn='cart_id_fk', inp=f_cart_id)
            for i in p_id_incart:
                #print("p_id",i[0])

                # update the product quantity in cart in case the inventory has been modified
                    # fetching the current quanity in product table
                cart_qnt = self.fetch_quantity(i[0]) 
                cart_qnt = int(cart_qnt)
                #print("cart_qnt",cart_qnt)

                    # fetching the current quantity in cart table
                p_qnt = query.select_where(sql=None, table_name='product_table', cols=['available_product_quantity'],condn='product_id', inp=i[0])
                product_qnt = p_qnt[0][0]
                product_qnt = int(product_qnt)
                #print("product_qnt",product_qnt)

                if product_qnt<cart_qnt:
                    sql = f"UPDATE cart_products_table SET product_quantity={0} WHERE product_id_fk={i[0]} AND cart_id_fk={f_cart_id}"
                    query.update(sql=sql)
                
                if product_qnt<=0:
                    sql = f"DELETE FROM cart_products_table WHERE product_id_fk={i[0]} AND cart_id_fk={f_cart_id}"
                    query.update(sql=sql)


                # fertching the p_details
                p_cost = query.select_where(sql=None, table_name='product_table', cols=['product_price'],condn='product_id', inp=i[0])
                #print("p cost : ",p_cost[0][0])
                # updating the price of the product into the cart
                query.update(sql=None, table_name='cart_products_table', cols=['product_price'], set=p_cost[0][0], condn='product_id_fk', inp=i[0])
                

            # fetching all the data from the cart product table where the cart_id matches with the p_id
            row = query.select_where(sql=None, table_name='cart_products_table', cols=['*'],condn='cart_id_fk', inp=f_cart_id)
            #print("cart product table fetched row ",row) #[(5, 6, 2, 44, 22), (5, 4, 1, 34, 34)]
            
            for i in row:
                p_name = query.select_where(sql=None, table_name='product_table', cols=['product_name'],condn='product_id', inp=i[1])
                # update quanity with updated product price
                query.update(sql=None, table_name='cart_products_table', cols=['total_cost'], set=i[2]*i[4], condn='product_id_fk', inp=i[1])
                
            # fetching all the data from the cart product table where the cart_id matches with the p_id
            rowd = query.select_where(sql=None, table_name='cart_products_table', cols=['*'],condn='cart_id_fk', inp=f_cart_id)
            #print("cart product table fetched row ",row) #[(5, 6, 2, 44, 22), (5, 4, 1, 34, 34)]
            
            # from cart_product_table
            
            for i in rowd:
                print("\nProduct Id : ",i[1])
                p_name = query.select_where(sql=None, table_name='product_table', cols=['product_name'],condn='product_id', inp=i[1])
                print("Product Name : ",p_name[0][0])
                print("Product Price : ",i[4])
                print("Quantity : ",i[2])
                print("Cost : ",i[3])
                print('---------------------------')
            return rowd
        else:
            print("Cart is Empty")
        
    def del_item_from_cart(self):
        query = Query()
        x = self.view_cart()
        p_id = []
        if len(x)==0:
            print("!!You cannot del any item!!")
        else:
            print('\n-------|DELETE ITEMS FROM Cart|--------')
            for i in x:
                p_id.append(i[1])
            while True:
                inp_p_id = input("Select Product id you want to remove from cart : ")
                if inp_p_id.isnumeric()==True:
                    inp_p_id = int(inp_p_id)
                    if inp_p_id in p_id:
                       
                        # delete the row where ( p_id belonging to c_id )
                        x = self.view_cart()

                        sql = f'DELETE FROM cart_products_table WHERE cart_id_fk = {x[0][0]} AND product_id_fk = {inp_p_id}'
                        query.delete(sql=sql)

                        print(f"Product with P_id {inp_p_id} removed successfully")
                        break
                    else:
                        print("Invaild product Id entered")
          
        
    def place_order(self):
            query = Query()
            
            print('\n-------|Order Details|--------')
            self.view_cart()
            
            # fetching the user_id from the user_name table
            row1 = query.select_where(sql=None, table_name='user_data_table', cols=['*'],condn='user_name', inp=self.usr_name)
            f_usr_id = row1[0][0]       
            #print("User id : ",f_usr_id)

            # fetching the cart id that belongs to the fetched_usr_id
            row1_cart = query.select_where(sql=None, table_name='cart_data_table', cols=['*'],condn='user_id_fk', inp=f_usr_id)
            #print("Cart id : ",f_cart_id)
            
            if len(row1_cart)!=0:
                f_cart_id = row1_cart[0][0]
                row1 = query.select_where(sql=None, table_name='cart_products_table', cols=['total_cost'],condn='cart_id_fk', inp=f_cart_id)
          
                order_total = 0
                for i in row1:
                    order_total+=i[0]
                print("Order total : ",order_total)

                # checking whether the user have sufficient balance to make an order or not
                cm = CustomerMethods(self.usr_name)
                bal = cm.check_wallet_balance()
                #print("bal : ",bal)
                if bal<=0 or bal<order_total:
                    cm.get_wallet_balance()
                    print("!! Insufficient wallet balance. Please add money to youe wallet !!")
                    return
            
                buy_amount = bal - order_total
                # updating the user wallet bal
                query.update(sql=None, table_name='wallet', cols=['wallet_balance'], set=buy_amount, condn='user_id_fk', inp=f_usr_id) 
                
                # fetch admin wallet balance # as we have a single admin id is set to 1
                row = query.select_where(sql=None, table_name='admin_wallet', cols='*',condn='admin_id_fk', inp=1)
                old_wallet_bal = row[0][0]
                updatedbal = order_total + old_wallet_bal
                # update the admin wallet bal
                query.update(sql=None, table_name='admin_wallet', cols=['wallet_balance'], set=updatedbal, condn='admin_id_fk', inp=1) 

                # Updating total_cost in cart_data_table of specific usr_id
                if order_total!=0:
                    #print("order_total : ",order_total)
                    #store_data = (order_total)
                    query.update(sql=None, table_name='cart_data_table', cols=['cart_total'], set=order_total, condn='user_id_fk', inp=f_usr_id)
                 
               
                    
                # adding data into the order_data_table : Making chages to order_data_table
                if len(row1_cart)!=0:
        
                    # fetching address from the user_data_table 
                    row1 = query.select_where(sql=None, table_name='user_data_table', cols=['user_address'],condn='user_name', inp=self.usr_name)
                    f_usr_address = row1[0][0]

                    # fetching total cost fromt the cart table
                    row1 = query.select_where(sql=None, table_name='cart_data_table', cols='*',condn='cart_id', inp=f_cart_id)
                    cartId = row1[0][0]
                    total_cost = row1[0][1]
                    #print("total_cost ",total_cost)

                    if total_cost!=None:
                        # adding data into the order data table 
                        store_data = (f_usr_address,order_total,f_usr_id)
                        cols = ['order_address','total_order_cost','user_id_fk']
                        table_name = 'orders_data_table'
                        query.insert(table_name, cols, store_data)

                        # making changes to ordered_products table
                            # fetching data from cart_products_table                
                        row_cart = query.select_where(sql=None, table_name='cart_products_table', cols='*',condn='cart_id_fk', inp=cartId)
                        #print("row_cart : ",row_cart)
                        #####@@print("row_cart",row_cart)
                    
                        x = False
                        #print('\n-------|View Order Details|--------')
                        for i in row_cart:
                            # fetching the order id from the orders_data_table
                            sql = f"select order_id from orders_data_table where user_id_fk = {f_usr_id} and total_order_cost = {total_cost}" 
                            row = query.select(sql=sql)
                            order_id = row[0][0]

                            # adding data into the ordered_products table 
                            store_data = (order_id,i[1],i[4],i[2],i[3])
                            #store_data = [f_usr_id]
                            table_name = 'ordered_products'
                            cols = ['order_id_fk','product_id_fkey','product_cost','product_quantity','total_cost']
                            query.insert(table_name, cols, store_data)

                            # fetching the actual product quanitity from the product table
                            pdt_quan = query.select_where(sql=None, table_name='product_table', cols='*',condn='product_id', inp=i[1])
                            update_pdt_quan = pdt_quan[0][4] - i[2]
                            # updating the product quantity inside the product table
                            query.update(sql=None, table_name='product_table', cols=['available_product_quantity'], set=update_pdt_quan, condn='product_id', inp=i[1])

                            # fetching the details from the product_data_table
                            pdt_detail = query.select_where(sql=None, table_name='product_table', cols='*',condn='product_id', inp=i[1])
                            
                            #print("pdt_detail",pdt_detail)
                            for i in pdt_detail:
                                #####@@print(i)
                                pdt_quan = query.select_where(sql=None, table_name='cart_products_table', cols='',condn='product_id_fk', inp=i[0])
                                sql = f"select product_quantity from cart_products_table where product_id_fk = {i[0]} and cart_id_fk = {cartId}" 
                                row = query.select(sql=sql)
                                pq = row[0][0]

                                 # adding the product_id with cart_id to the order_details table
                                store_data = (i[0],i[1],i[2],i[3],i[5],order_id,pq)
                                cols = ['product_id','product_name','product_details','product_price','product_brand','order_id','product_quantity']
                                table_name = 'order_details_save'
                                query.insert(table_name, cols, store_data)
                                break

                            x = True

                        # Empty the cart after the order has been successfully placed
                        if x == True:

                            # fetching the cart id from cart_data_table
                            row1_cart = query.select_where(sql=None, table_name='cart_data_table', cols='*',condn='user_id_fk', inp=f_usr_id)
                            f_cart_id = row1_cart[0][0]

                            # empty the cart
                            query.delete(sql=None, table_name='cart_data_table', condn='cart_id', inp=f_cart_id)
                            print("!! Order Placed Successfully !!")
