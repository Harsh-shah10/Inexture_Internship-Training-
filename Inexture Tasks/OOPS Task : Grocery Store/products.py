
from cart import CartMethods
from query import Query

class Products:
    def __init__(self,usr_name):
        self.usr_name = usr_name
    
    def view_all_products(self):
        query = Query()
        data = query.select(sql=None, table_name='product_table', cols='*')
        return data 


    def view_all_products_admin(self):
        query = Query()
        data = query.select(sql=None, table_name='product_table', cols='*')
        return data

    '''
    def view_and_select_Category(self,choice,c_id):
        # for viewing products belonging to category
        self.view_products(c_id)

    '''

    def view_categories(self):
        query = Query()
        data = query.select(sql=None, table_name='category_table', cols='*')
        return data 
     
    def view_products(self,c_id):
        query = Query()

        data = query.select_where(sql=None, table_name='product_table', cols='*', condn='category_id', inp=c_id)
        return data
        


'''pl = Products()
pl.view_products()'''

'''c1 = Products()
c1.view_and_select_Category()'''