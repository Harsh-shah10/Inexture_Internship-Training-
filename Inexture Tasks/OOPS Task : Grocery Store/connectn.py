import psycopg2
class Database:
	def __init__(self):
		try:
			self.conn = psycopg2.connect(database = 'grocerystore', user= 'postgres',password = 'password', host= 'localhost')
			
		except Exception:
			print("Error")
			

	def execute_query_2(self, query):
		self.cursor=self.conn.cursor()
		self.cursor.execute(query)
		fetched_data = self.cursor.fetchall()
		return fetched_data
	'''	self.cursor.close()
		self.conn.commit()
		self.conn.close()'''
		
		
    
	def execute_query(self, query):
		self.cursor=self.conn.cursor()
		self.cursor.execute(query)
	'''	self.cursor.close()
		self.conn.commit()
		self.conn.close()'''
	

	def __del__(self):
		self.cursor.close()
		self.conn.commit()
		self.conn.close()
		