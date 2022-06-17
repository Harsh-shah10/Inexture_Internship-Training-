from connectn import Database

class Query:

    def delete(self, sql=None, table_name=None, condn=None, inp=None):
        obj = Database()
      
        if not sql:
            #cols = ','.join(cols)
            sql = f"DELETE FROM {table_name} WHERE {condn} = {inp}"
        obj.execute_query(sql)
        #print("executed del query")
    
    def insert(self, table_name, cols, store_data):
        obj = Database()
        
        cols = ','.join(cols)
        store_data = ','.join(["'"+str(data)+"'" for data in store_data])
        
        sql = f'INSERT INTO {table_name}({cols}) Values({store_data})'
        obj.execute_query(sql)
        #print("executed insert query")

    def select(self, sql=None, table_name=None, cols=None):
        obj = Database()
      
        if not sql:
            cols = ','.join(cols)
            sql = f'SELECT {cols} FROM {table_name}'
            
        record=obj.execute_query_2(sql)
        #print("executed select query")
        return record
       

    def select_where(self, sql=None, table_name=None, cols=None, condn=None, inp=None):
        obj = Database()
      
        if not sql:
            cols = ','.join(cols)
            sql = f"SELECT {cols} FROM {table_name} WHERE {condn} = '{inp}'"
      
        record=obj.execute_query_2(sql)
        #print("executed Select_where query")
        return record
        
        

    def select_no_inp(self, sql=None, table_name=None, cols=None):
        obj = Database()
        
        if not sql:
           
            sql = f'SELECT {cols} FROM {table_name}'

        obj.execute_query_2(sql)
        record=obj.execute_query_2(sql)
        #print("executed select_no_inp query")
        return record
        
        
    # for integer as an input
    def update(self, sql=None, table_name=None, cols=None, set=None, condn=None, inp=None):
        obj = Database()
      
        if not sql:
            cols = ','.join(cols)
            sql = f"UPDATE {table_name} SET {cols} = {set} WHERE {condn} = '{inp}'"

        obj.execute_query(sql)
        #print("executed update query")

    # for multiple and single inputs
    def update_string(self, sql=None, table_name=None, cols=None, set=None, condn=None, inp=None):
        obj = Database()
        
        if not sql:
            new_val = ','.join(cols[i] +"='"+set[i]+"'" for i in range(len(cols)))
            sql = f"UPDATE {table_name} SET {new_val} WHERE {condn} = '{inp}'"

        obj.execute_query(sql)
        #print("executed update_string query")

    def search(self, sql=None, table_name=None, cols=None, find=None):
        obj = Database()
      
        if not sql:
            sql = f"SELECT {cols} FROM {table_name} WHERE {cols} LIKE '{find}%'"

        record=obj.execute_query_2(sql)
        #print("executed search query")
        return record
        
















