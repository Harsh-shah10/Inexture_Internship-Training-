from query import Query
from validation import *

class PUpdateMethods:
    def __init__(self,usr_name):
        self.usr_name = usr_name
    

    def update_Pname(self,p_name,c_id,p_id):
        query = Query()
     
        query.update_string(sql=None, table_name='product_table', cols=['product_name'], set=[p_name], condn='product_id', inp=p_id)
        
    def update_Pprice(self,p_price,c_id,p_id):
        query = Query()

        query.update_string(sql=None, table_name='product_table', cols=['product_price'], set=[p_price], condn='product_id', inp=p_id)
    
        # updating the price of the porducts inside cart whose cost has been updated
        query.update_string(sql=None, table_name='cart_products_table', cols=['product_price'], set=[p_price], condn='product_id_fk', inp=p_id)

        

    def update_Pquanity(self,p_quantity,c_id,p_id):
        query = Query()

        query.update_string(sql=None, table_name='product_table', cols=['available_product_quantity'], set=[p_quantity], condn='product_id', inp=p_id)
        

    def update_Details(self,p_details,c_id,p_id):
        query = Query()
  
        query.update_string(sql=None, table_name='product_table', cols=['product_details'], set=[p_details], condn='product_id', inp=p_id)
        

    def update_Brand(self,p_brand,c_id,p_id):
        query = Query()
  
        query.update_string(sql=None, table_name='product_table', cols=['product_brand'], set=[p_brand], condn='product_id', inp=p_id)
        


    def update_Pcategory(self,p_cat,c_id,p_id):
        query = Query()
  
        query.update_string(sql=None, table_name='product_table', cols=['category_id'], set=[p_cat], condn='product_id', inp=p_id)
        
