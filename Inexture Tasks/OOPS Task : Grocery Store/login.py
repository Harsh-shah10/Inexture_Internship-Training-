from admin_dashboard import Admin_Dashboard
from customer_dashboard import Customer_Dashboard
from query import Query


class Login:
    def user_login(self,usr_name,usr_pass):
        query = Query()

        #query for validating user name and pass for customers 
        sql = "select  user_name ,user_pass from user_data_table"
        records = query.select(sql=sql)
      

        for row in records:
            if(row[0] == usr_name and row[1] == usr_pass):
                    print(f"Welcome Id : {row[0]}")
                    # moving the control to customer dashboard 
                    Customer_menu_obj = Customer_Dashboard(usr_name)
                    Customer_menu_obj.customer_menu()
                    return

        #query for validating user name and pass for Admin
        sql = "select  admin_user_id ,admin_pass from admin_data_table"
        records = query.select(sql=sql)
        
        for row in records:
            if(row[0] == usr_name and row[1] == usr_pass):
                    print(f"Id : {row[0]}, Pass : {row[1]}")
                    # moving the control to admin dashboard 
                    Admin_menu_obj = Admin_Dashboard(usr_name)
                    Admin_menu_obj.admin_menu()
                    return
                    
        print("Incorrect ID or Password !!")
        return False, None
         
# --just for testing modules is working or not--
'''l = Login()
l.user_login()'''