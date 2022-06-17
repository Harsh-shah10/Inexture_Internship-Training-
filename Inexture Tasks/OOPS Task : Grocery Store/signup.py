from connectn import Database
from query import Query
#print(Database)

class Signup:
    def signup(self, usr_name,usr_pass,fn,ln,address,email):
        query = Query()

        # inserting user data into user_data_table
        store_data = (usr_name,usr_pass,fn,ln,address,email)
        cols = ('user_name','user_pass','user_first_name','user_last_name','user_address','user_email')
        table_name = 'user_data_table'
        query.insert(table_name, cols, store_data)

        #fetch user id 
        row1 = query.select_where(sql=None, table_name='user_data_table', cols='*',condn='user_name', inp=usr_name)
        fetches_usr_id = row1[0][0]
        print("fetches_usr_id : ",fetches_usr_id)

        store_data = [fetches_usr_id,0]
        cols = ['user_id_fk','wallet_balance']
        table_name = 'wallet'
        query.insert(table_name, cols, store_data)

        # setting wallet balance to zero 
        #updated_balance = 5
        #query.update(sql=None, table_name='wallet', cols=['wallet_balance'], set=updated_balance, condn='user_id_fk', inp=fetches_usr_id) 
                
        print(f"\n---- Dear {usr_name} ,You Had Been Sucessfully Registered ----")

    # -- checking whether the username already exist or not -- 
    def check_user_name(self, usr_name):
        query = Query()
                # fetching the user_name from the customer table
        sql = f"select * from user_data_table where exists (select * from user_data_table where user_name = '{usr_name}' )"
        rows1=query.select(sql=sql)

            # fetching the user_name from the admin table
        sql = f"select * from admin_data_table where exists (select * from admin_data_table where admin_user_id = '{usr_name}' )"
        rows2=query.select(sql=sql)
        if(len(rows1) != 0 or len(rows2) != 0):
            print("\nUser name already exist")
            return False
        return True

# --just for testing modules are working or not--
#   s = Signup()
#   s.signup()