from query import execute_query
import fetch_query

class organization_registration:
	def __init__(self,c_name,web_site,official_mail,admin_id,admin_pass):
		self.c_name = c_name
		self.web_site = web_site
		self.official_mail = official_mail
		self.admin_id = admin_id
		self.admin_pass = admin_pass

	def register_comapny(self):
		try:
			# print(self.password,self.f_name,self.l_name,self.mobile_no,self.email,self.age,self.ssc_result,self.hsc_result,self.stream,self.cgpa,self.city,self.resume)
			# statement = "INSERT INTO organization(c_name,web_site,official_mail,admin_id,admin_pass) VALUES (%s,%s,%s,%s,%s) RETURNING c_id,q_set;"
			statement = fetch_query.register_comapny_query('c_name','web_site','official_mail','admin_id','admin_pass')
			parameters = (self.c_name,self.web_site,self.official_mail,self.admin_id,self.admin_pass)
			l = execute_query(statement,parameters,'returned')
			l1 = l[0]
			print(f"Company_id : {l1[0]}")
			print(f"Company_set_number : {l1[1]}")

			statement = fetch_query.insert_query_3('hiring_role','q_set','role')
			parameters = (l1[1],'None')
			l = execute_query(statement,parameters,'no_return')
			
			return True
		except Exception as error :
			print(error)

class organization():
	def __init__(self,admin_id):
		self.admin_id = admin_id

	def view_org_details(self):
		# statement = f"SELECT * FROM organization WHERE admin_id = {self.admin_id}"
		statement = fetch_query.select_query('*','organization','admin_id',self.admin_id)
		parameters = None
		l = execute_query(statement,parameters,'returned')
		l1 = l[0]
		return l1

	def update_org_details(self,col_name,new_val):
		# statement = f"UPDATE organization SET {col_name}=%s where admin_id=%s"
		statement = fetch_query.update_query('organization',col_name,'admin_id')
		parameters = (new_val,self.admin_id)
		l = execute_query(statement,parameters,'no_return')
		return True

	def create_test(self,question_lst,role):
		# statement = f"SELECT q_set FROM organization where admin_id = {self.admin_id};"
		statement = fetch_query.select_query('q_set','organization','admin_id',self.admin_id)
		parameters = None
		l = execute_query(statement,parameters,'returned')
		l1 = l[0]
		# statement = f"DELETE FROM questions WHERE q_set = {l1[0]}"
		statement = fetch_query.delete_query('questions', 'q_set', l1[0])
		parameters = None
		l = execute_query(statement,parameters,'no_return')

		for i in question_lst:
			# statement = f"INSERT INTO questions(question,marks,answer,op1,op2,op3,op4,q_set) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
			statement = fetch_query.insert_query('question','marks','answer','op1','op2','op3','op4','q_set')
			parameters = tuple(i + [l1[0]])
			l2 = execute_query(statement,parameters,'no_return')

		statement = fetch_query.update_query('hiring_role','role','q_set')
		parameters = (role,l1[0])
		l2 = execute_query(statement,parameters,'no_return')
		return True


	def display_questions(self):
		# statement = f"SELECT q_set FROM organization where admin_id = {self.admin_id};"
		statement = fetch_query.select_query('q_set','organization','admin_id',self.admin_id)
		parameters = None
		l = execute_query(statement,parameters,'returned')

		# statement = f"SELECT * FROM questions WHERE q_set={l[0][0]}"
		statement = fetch_query.select_query('*','questions','q_set',l[0][0])
		parameters = None
		l1 = execute_query(statement,parameters,'returned')
		
		if len(l1) == 0:
			return False,0
		else:
			return True,l1


	def update_question(self,col_name,new_val,q_id):
		# statement = f"UPDATE questions SET {col_name} = %s WHERE q_id=%s"
		statement = fetch_query.update_query('questions',col_name, 'q_id')
		parameters = (new_val,q_id)
		l = execute_query(statement,parameters,'no_return')
		return True

	def view_applicants(self,constraint,val,condition):
		# statement = f"SELECT c_id FROM organization where admin_id = {self.admin_id};"
		statement = fetch_query.select_query('c_id','organization','admin_id',self.admin_id)
		parameters = None
		l = execute_query(statement,parameters,'returned')

		temp = True

		if len(l) != 0:
			
			company_id = l[0][0]

			if constraint=='f_name' or constraint=='stream' or constraint=='city':
				# statement = f"SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd WHERE sd.c_id = %s and sd.user_id = cd.user_id and cd.{constraint}=%s;"
				statement = fetch_query.view_applicants_select_query(constraint)
				parameters = (company_id,val)
				l = execute_query(statement,parameters,'returned')
			elif constraint=='age' or constraint=='cgpa' or constraint=='ssc_result' or constraint=='hsc_result':
				if condition=='1':
					# statement = f"SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd WHERE sd.c_id = %s and sd.user_id = cd.user_id and cd.{constraint} < %s;"
					statement  = fetch_query.view_applicants_select_query(constraint)
					parameters = (company_id,val)
					l = execute_query(statement,parameters,'returned')
				elif condition=='2':
					# statement = f"SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd WHERE sd.c_id = %s and sd.user_id = cd.user_id and cd.{constraint} > %s;"
					statement = fetch_query.view_applicants_select_query(constraint)
					parameters = (company_id,val)
					l = execute_query(statement,parameters,'returned')
				else:
					print("Some loophole ! ")

			elif constraint=='tech':
				# statement = "SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd, interested_tech AS it WHERE sd.c_id = %s and sd.user_id = cd.user_id and it.user_id = sd.user_id and it.tech = %s;"
				statement = fetch_query.view_applicants_select_query_2()
				parameters = (company_id,val)
				l = execute_query(statement,parameters,'returned')
			else:
				# statement = f"SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd WHERE sd.c_id = {company_id} and sd.user_id = cd.user_id;"
				statement = fetch_query.view_applicants_select_query_3(company_id)
				parameters = None
				l = execute_query(statement,parameters,'returned')


			if len(l) != 0:
				return company_id,temp,l
			else:
				temp = False
				return company_id,temp,None
		else:
			temp = False
			return 0,temp,None



	def select_candidate(self,uid,company_id,status):
		# statement = "UPDATE selection_details SET selection_status=%s WHERE user_id=%s and c_id=%s"
		statement = fetch_query.update_query_1('selection_details','selection_status','user_id','c_id')
		parameters = (status,uid,company_id)
		l = execute_query(statement,parameters,'no_return')

		statement = fetch_query.select_query('email','candidate','user_id',uid)
		parameters = None
		query_result = execute_query(statement,parameters,'returned')

		return query_result[0]

	def view_user_details(self,uid,c_id):
		# statement = f"SELECT cd.* FROM candidate AS cd,selection_details AS sd WHERE cd.user_id = %s and sd.user_id = %s and sd.c_id = %s"
		statement = fetch_query.view_user_details_query()
		parameters = (uid,uid,c_id)
		l = execute_query(statement,parameters,'returned')
		if len(l) == 0:
			return 0,False
		else:
			l1 = l[0]
			return l1,True


	def provide_instruction(self,instruction,company_id,uid):
		# statement = "UPDATE selection_details SET next_process_info=%s WHERE user_id=%s and c_id=%s"
		statement = fetch_query.update_query_1('selection_details','next_process_info','user_id','c_id')
		parameters = (instruction,uid,company_id)
		l = execute_query(statement,parameters,'no_return')

		statement = fetch_query.select_query('email','candidate','user_id',uid)
		parameters = None
		query_result = execute_query(statement,parameters,'returned')
		return query_result[0]

	def view_user_queries(self):
		# statement = f"SELECT c_id FROM organization where admin_id = {self.admin_id};"
		statement = fetch_query.select_query('c_id','organization','admin_id',self.admin_id)
		parameters = None
		l = execute_query(statement,parameters,'returned')

		c_id = l[0][0]

		# statement = f"SELECT * FROM user_queries WHERE c_id={c_id}"
		statement = fetch_query.select_query('*','user_queries','c_id',c_id)
		parameters = None
		query_result = execute_query(statement,parameters,'returned')

		if len(query_result) == 0:
			return None,None,query_result
		
		else:
			return 1,c_id,query_result

	def reply_to_querires(self,u_id,c_id,message):
		# statement = "UPDATE user_queries SET organization_responce = %s WHERE user_id=%s AND c_id=%s"
		statement = fetch_query.update_query_1('user_queries','organization_responce','user_id','c_id')
		parameters = (message,u_id,c_id)
		query_result = execute_query(statement,parameters,'no_return')

		# statement = f"SELECT email FROM candidate WHERE user_id={u_id}"
		statement = fetch_query.select_query('email','candidate','user_id',u_id)
		parameters = None
		query_result = execute_query(statement,parameters,'returned')
		return query_result[0],c_id

	def close_hiring(self):
		statement = fetch_query.select_query('q_set','organization','admin_id',self.admin_id)
		parameters = None
		l = execute_query(statement,parameters,'returned')
		q_set = l[0][0]

		statement = fetch_query.select_query('c_id','organization','admin_id',self.admin_id)
		parameters = None
		l = execute_query(statement,parameters,'returned')
		cid = l[0][0]

		statement = fetch_query.delete_query('questions','q_set',q_set)
		parameters = None
		l = execute_query(statement,parameters,'no_return')

		statement = fetch_query.delete_query('selection_details','c_id',cid)
		parameters = None
		l = execute_query(statement,parameters,'no_return')

		return True