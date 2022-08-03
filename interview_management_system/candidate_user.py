from query import execute_query;
import fetch_query

class user_registration:
	def __init__(self,f_name,l_name,mobile_no,email,age,password,ssc_result,hsc_result,stream,cgpa,city,resume,interested_tech):
		self.f_name = f_name
		self.l_name = l_name
		self.mobile_no = mobile_no
		self.email = email
		self.age = age
		self.password = password
		self.ssc_result = ssc_result
		self.hsc_result = hsc_result
		self.stream = stream
		self.cgpa = cgpa
		self.city = city
		self.resume = resume
		self.interested_tech = interested_tech

	def register_user(self):
		try:
			# print(self.password,self.f_name,self.l_name,self.mobile_no,self.email,self.age,self.ssc_result,self.hsc_result,self.stream,self.cgpa,self.city,self.resume)
			statement = "INSERT INTO candidate(password,f_name,l_name,mobile_n,email,age,ssc_result,hsc_result,stream,cgpa,city,resume) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING user_id;"
			# statement = fetch_query.insert_query_1('candidate','password','f_name','l_name','mobile_n','email','age','ssc_result','hsc_result','stream','cgpa','city','resume')
			parameters = (self.password,self.f_name,self.l_name,self.mobile_no,self.email,self.age,self.ssc_result,self.hsc_result,self.stream,self.cgpa,self.city,self.resume)
			
			temp = execute_query(statement,parameters,'returned')

			# return True
			current_user_id = temp[0][0]
			for i in self.interested_tech:
				# statement = "INSERT INTO interested_tech(user_id,tech) VALUES(%s,%s)"
				statement = fetch_query.insert_query_3('interested_tech','user_id','tech')
				parameters = (current_user_id,i)
				temp = execute_query(statement,parameters,'no_return')
			print(f"Your User_id : {current_user_id}")
			return True
		except Exception as error :
			print(error)

class candidate:
	def __init__(self,uid):
		self.uid = uid

	def view_details(self):
		# statement = f"SELECT * FROM candidate WHERE user_id = {self.uid}"
		statement = fetch_query.select_query('*','candidate','user_id',self.uid)
		parameters = None
		l = execute_query(statement,parameters,'returned')
		l1 = l[0]
		return l1
		

	def update_details(self,detail,new_val):
		# statement = f"UPDATE candidate SET {detail}=%s where user_id=%s"
		statement = fetch_query.update_query('candidate',detail,'user_id')
		if detail == 'resume':
			parameters = (new_val,self.uid)
			temp = execute_query(statement,parameters,'no_return')
			return True
		else:
			parameters = (f"{new_val}",self.uid)
			temp = execute_query(statement,parameters,'no_return')
			return True

	def Apply_interview(self,temp,c_id,c_id_lst):
		# statement = "SELECT DISTINCT org.c_id,org.c_name,org.web_site,org.official_mail FROM organization AS org , questions as q where q.q_set=org.q_set"
		if temp == 1:
			statement = fetch_query.Apply_interview_query()
			parameters = None
			query_result = execute_query(statement,parameters,'returned')


			return 0,query_result,True
		else:
			if c_id.isnumeric() and (int(c_id) in c_id_lst):
				c_id=int(c_id)
				# statement = "SELECT CASE WHEN (user_id=%s and c_id=%s) THEN True ELSE False END AS temp FROM selection_details;"
				statement = fetch_query.Apply_interview_query_1()
				parameters = (self.uid,c_id)
				query_result = execute_query(statement,parameters,'returned')
				temp = True
				for i in query_result:
					if i[0] == True:
						temp = False

				if temp:
					# statement = f"SELECT q_set FROM organization WHERE c_id={c_id};"
					statement = fetch_query.select_query('q_set','organization','c_id',c_id)
					parameters = None
					query_result = execute_query(statement,parameters,'returned')

					# statement = f"SELECT question,marks,answer,op1,op2,op3,op4 FROM questions WHERE q_Set={query_result[0][0]}"
					statement = fetch_query.select_query_1('question','marks','answer','op1','op2','op3','op4','questions','q_set',query_result[0][0])
					parameters = None
					query_result = execute_query(statement,parameters,'returned')

					statement = fetch_query.select_query('role','hiring_role','q_set',query_result[0][0])
					parameters = None
					l2 = execute_query(statement,parameters,'return')

					return c_id,query_result,True

				else:
					return 0,0,False

			else:
				return 0,0,None

	def View_applications(self):

		# statement = f"SELECT sd.user_id,sd.c_id,org.c_name,sd.marks,sd.selection_status,sd.next_process_info FROM organization AS org,selection_details as sd WHERE sd.user_id={self.uid} and org.c_id = sd.c_id"
		statement = fetch_query.View_applications_query(self.uid)
		parameters = None
		query_result = execute_query(statement,parameters,'returned')
		return query_result
			

	def take_test(self,c_id,gained_marks):
		# statement = "INSERT INTO selection_details(user_id,c_id,marks,selection_status) VALUES(%s,%s,%s,%s)"
		statement = fetch_query.insert_query_2('selection_details','user_id','c_id','marks','selection_status')
		parameters = (self.uid,c_id,gained_marks,'Under Processing...')
		query_result = execute_query(statement,parameters,'no_return')
		return True


	def submit_query(self,message,c_id):
		# statement = "INSERT INTO user_queries(user_id,c_id,user_query,organization_responce) VALUES(%s,%s,%s,%s)"
		statement = fetch_query.insert_query_2('user_queries','user_id','c_id','user_query','organization_responce')
		parameters = (self.uid,c_id,message,'under_observation...')
		query_result = execute_query(statement,parameters,'no_return')
		print("Your Query Has Been Submited Sucessfully ... ")

		# statement = f"SELECT official_mail FROM organization where c_id={c_id}"
		statement = fetch_query.select_query('official_mail','organization','c_id',c_id)

		parameters = None
		query_result = execute_query(statement,parameters,'returned')
		return query_result[0],self.uid

	def view_query(self):
		# statement = f"SELECT * FROM user_queries WHERE user_id={self.uid}"
		statement = fetch_query.select_query('*','user_queries','user_id',self.uid)
		parameters = None
		query_result = execute_query(statement,parameters,'returned')

		return query_result