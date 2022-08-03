from query import execute_query;
import fetch_query

class validation:
	def __init__(self,uid,password):
		self.uid = uid
		self.password = password

	def validate_super_admin(self):
		temp=False
		# statement = "SELECT case when (id = %s and password = %s) THEN True ELSE False END AS temp from super_admin;"
		statement = fetch_query.credential_check_query('id','password','super_admin')
		parameters = (self.uid,self.password)
		query_result = execute_query(statement,parameters,'returned')
		for i in query_result:
			if i[0] == True:
				temp = True
		return temp

	def validate_admin(self):
		temp=False
		# statement = "SELECT case when (admin_id = %s and admin_pass = %s) THEN True ELSE False END AS temp from organization;"
		statement = fetch_query.credential_check_query('admin_id','admin_pass','organization')
		parameters = (self.uid,self.password)
		query_result = execute_query(statement,parameters,'returned')
		for i in query_result:
			if i[0] == True:
				temp = True
		return temp

	def validate_user(self):
		temp=False
		# statement = "SELECT case when (user_id = %s and password = %s) THEN True ELSE False END AS temp from candidate;"
		statement = fetch_query.credential_check_query('email','password','candidate')
		parameters = (self.uid,self.password)
		query_result = execute_query(statement,parameters,'returned')
		for i in query_result:
			if i[0] == True:
				temp = True
		return temp

	def fetch_uid(self):
		statement = fetch_query.fetch_uid('email','password','candidate')
		parameters = (self.uid,self.password)
		uid = execute_query(statement,parameters,'returned')
		return uid[0][0]
