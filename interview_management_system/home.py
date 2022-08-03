class validation:
	def __init__(self,uid,password):
		self.uid = uid
		self.password = password

	def validate_super_admin(self):
		temp=False
		cur.execute("SELECT case when (id = %s and password = %s) THEN True ELSE False END AS temp from super_admin;",(self.uid,self.password))
		for i in cur:
			if i[0] == True:
				temp = True
		return temp
	def validate_admin(self):
		temp=False
		cur.execute("SELECT case when (admin_id = %s and admin_pass = %s) THEN True ELSE False END AS temp from organization;",(self.uid,self.password))
		for i in cur:
			if i[0] == True:
				temp = True
		return temp

	def validate_user(self):
		temp=False
		cur.execute("SELECT case when (user_id = %s and password = %s) THEN True ELSE False END AS temp from candidate;",(self.uid,self.password))
		for i in cur:
			if i[0] == True:
				temp = True
		return temp


class registration:
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
			cur.execute("INSERT INTO candidate(password,f_name,l_name,mobile_n,email,age,ssc_result,hsc_result,stream,cgpa,city,resume) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING user_id;", (self.password,self.f_name,self.l_name,self.mobile_no,self.email,self.age,self.ssc_result,self.hsc_result,self.stream,self.cgpa,self.city,self.resume))
			# return True
			current_user_id = list(cur)[0][0]
			for i in interested_tech:
				cur.execute("INSERT INTO interested_tech(user_id,tech) VALUES(%s,%s)", (current_user_id,i))
			print(f"Your User_id : {current_user_id}")
			return True
		except Exception as error :
			print(error)

class candidate:
	def __init__(self,uid):
		self.uid = uid

	def view_details(self):
		cur.execute(f"SELECT * FROM candidate WHERE user_id = {self.uid}")
		l = list(cur)[0]
		print("User_id : ", l[0])
		print("f_name : ", l[2])
		print("l_name : ", l[3])
		print("mobile_no : ", l[4])
		print("email : ", l[5])
		print("age : ", l[6])
		print("ssc_result : ", l[7])
		print("hsc_result : ", l[8])
		print("stream : ", l[9])
		print("CGPA : ", l[10])
		print("city : ", l[11])
		
		flag = input("For View Resume type 'yes' Else type 'no:  ")

		if flag=='yes':
			storeFilePath = "file.pdf"
			with open(storeFilePath,"wb") as File:
				File.write(l[12])
				File.close()
			webbrowser.open(storeFilePath)
			return
		elif flag=='no':
			return
		else:
			print("Please Enter Valid Input")

	def update_details(self,detail,new_val):
		statement = f"UPDATE candidate SET {detail}=%s where user_id=%s"
		if detail == 'resume':
			cur.execute(statement,(new_val,self.uid))
			return True
		else:
			cur.execute(statement,(f"{new_val}",self.uid))
			return True

	def Apply_interview(self):
		cur.execute("SELECT DISTINCT org.c_id,org.c_name,org.web_site,org.official_mail FROM organization AS org , questions as q where q.q_set=org.q_set")
		print("In Which Company You want to apply for interview ? Please Enter a C_id of that company : ")
		print(f"c_id     {'c_name'.center(20,' ')}{'web_site'.center(20,' ')}{'official_mail'.center(30,' ')}")
		for i in cur:
			print(f"{i[0]}        {i[1].center(20,' ')}{i[2].center(20,' ')}{i[3].center(30,' ')}")
		c_id = input("Enter c_id of company in which you want to apply for interview test: ")
		if c_id.isnumeric():
			c_id=int(c_id)
			cur.execute("SELECT CASE WHEN (user_id=%s and c_id=%s) THEN True ELSE False END AS temp FROM selection_details;",(self.uid,c_id))
			temp = True
			for i in cur:
				if i[0] == True:
					temp = False

			if temp:

				cur.execute(f"SELECT q_set FROM organization WHERE c_id={c_id};")
				cur.execute(f"SELECT question,marks,answer,op1,op2,op3,op4 FROM questions WHERE q_Set={list(cur)[0][0]}")
				test = list(cur)
				Total_marks = 0
				gained_marks = 0
				j=1
				for i in test:
					while True:
						print(f"Q{j}. {i[0]}")
						print(f"1. {i[3]}")
						print(f"2. {i[4]}")
						print(f"3. {i[5]}")
						print(f"4. {i[6]}")

						ans = input("Chose Your answer [1,2,3,4]: ")
						if ans == '1' or ans=='2' or ans=='3' or ans=='4':
							ans = int(ans)
							if i[ans+2] == i[2]:
								print("Correct Answer")
								Total_marks += i[1]
								gained_marks += i[1]
							else:
								Total_marks += i[1]
								print("Wrong Answer")
							break
						else:
							print("Please Select valid Input !")
					j+=1
				cur.execute("INSERT INTO selection_details(user_id,c_id,marks,selection_status) VALUES(%s,%s,%s,%s)", (self.uid,c_id,gained_marks,'Under Processing...'))
				print(f"Your Result : {gained_marks}/{Total_marks}... ")
				return True

			else:
				print("You have Alredy Apear in test ! You can not Re-attempt it !...")

		else:
			print("Please Enter Valid Input !")

	def View_applications(self):
		cur.execute(f"SELECT sd.user_id,sd.c_id,org.c_name,sd.marks,sd.selection_status,sd.next_process_info,sd.user_responce FROM organization AS org,selection_details as sd WHERE sd.user_id={self.uid} and org.c_id = sd.c_id")
		while True:
			print(f"user_id      Company_id      {'Comapany_name'.center(20,' ')}     Marks     {'selection_status'.center(30,' ')}{'Instruction_by_company'.center(30,' ')}{'Your_request'.center(30,' ')}")

			for i in cur:
				l1 = f"{i[5]}"
				l2 = f"{i[6]}"
				print(f"{i[0]}                {i[1]}      {i[2].center(20,' ')}           {i[3]}         {i[4].center(30,' ')}{l1.center(30,' ')}{l2.center(30,' ')}")


			flag = input("\n\n\n Do You Want To Put your Query ? yes or no  ? : ")
			if flag == 'yes':
				if i[4] == 'selected':
					query = input("Enter Your Query message : ")
					cur.execute(f"UPDATE selection_details SET user_responce = {query}")
				else:
					print("Your Applicantion is under observation! You can put your querry only if you will selected ! ")
					break
			elif flag == 'no':
				break
			else:
				print("Please Enter Valid input ! ")

		return True




class register_organization:
	def __init__(self,c_name,web_site,official_mail,admin_id,admin_pass):
		self.c_name = c_name
		self.web_site = web_site
		self.official_mail = official_mail
		self.admin_id = admin_id
		self.admin_pass = admin_pass

	def register_comapny(self):
		try:
			# print(self.password,self.f_name,self.l_name,self.mobile_no,self.email,self.age,self.ssc_result,self.hsc_result,self.stream,self.cgpa,self.city,self.resume)
			cur.execute("INSERT INTO organization(c_name,web_site,official_mail,admin_id,admin_pass) VALUES (%s,%s,%s,%s,%s) RETURNING c_id,q_set;", (self.c_name,self.web_site,self.official_mail,self.admin_id,self.admin_pass))
			
			l1 = list(cur)[0]
			print(f"Company_id : {l1[0]}")
			print(f"Company_set_number : {l1[1]}")
			return True
		except Exception as error :
			print(error)

class organization(candidate):
	def __init__(self,admin_id):
		self.admin_id = admin_id

	def view_org_details(self):
		cur.execute(f"SELECT * FROM organization WHERE admin_id = {self.admin_id}")
		l1 = list(cur)[0]
		print(f"Company id : {l1[0]}")
		print(f"Company name : {l1[1]}")
		print(f"Company web site : {l1[2]}")
		print(f"Company official mail id : {l1[3]}")
		print(f"Company question set no : {l1[4]}")
		return True

	def update_org_details(self,col_name,new_val):
		statement = f"UPDATE organization SET {col_name}=%s where admin_id=%s"
		cur.execute(statement,(new_val,self.admin_id))
		return True

	def create_test(self):
		cur.execute(f"SELECT q_set FROM organization where admin_id = {self.admin_id};")
		l1 = list(cur)[0]
		cur.execute(f"DELETE FROM questions WHERE q_set = {l1[0]}")

		no_of_question = input("Please Enter Number of questions")
		if no_of_question.isnumeric():
			no_of_question = int(no_of_question)
			i=0
			while i < no_of_question:
				print(f"*****************  QUESTION - {i+1} ***********")
				options = []
				while True:
					marks = input(f"Enter the marks for question-{i+1} : ")
					if marks.isnumeric():
						marks = int(marks)
						break
					else:
						print("Please Enter Valid Marks !")

				question = input(f"Enter Question-{i+1} : ")
				for j in range(4):
					op = input(f"Enter Op{j+1} for question-{i+1}")
					options += [op]
				
				while True:
					for k in range(4):
						print(f"{k+1}. {options[k]}")
					answer = input("Select answer for this question")
					if answer == '1' or answer =='2'or answer=='3' or answer=='4':
						answer = options[int(answer)-1]
						cur.execute("INSERT INTO questions(q_set,question,marks,answer,op1,op2,op3,op4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (l1[0],question,marks,answer,options[0],options[1],options[2],options[3]))
						i = i+1
						break
					else:
						print("Invalid Input!")
			return True
		else:
			print("Please Enter Valid input !")

	def update_test(self):
		cur.execute(f"SELECT q_set FROM organization where admin_id = {self.admin_id};")
		cur.execute(f"SELECT * FROM questions WHERE q_set={list(cur)[0][0]}")
		
		print(f"\nq_id     q_set{'question'.center(20,' ')}marks{'answer'.center(15,' ')}{'op1'.center(15,' ')}{'op2'.center(15,' ')}{'op3'.center(15,' ')}{'op4'.center(15,' ')}   \n")
		for i in cur:
			print(f"   {i[0]}      {i[1]}{i[2].center(20,' ')}     {i[3]}{i[4].center(15,' ')}{i[5].center(15,' ')}{i[6].center(15,' ')}{i[7].center(15,' ')}{i[8].center(15,' ')}")

		while True:
			q_id = input("Please Enter q_id of question which you want to update...")
			if q_id.isnumeric():
				print("What you want to change ? ")
				print("1. question")
				print("2. marks")
				print("3. answer")
				print("4. op1")
				print("5. op2")
				print("6. op3")
				print("7. op4")
				ch3 = input("Enter Your choice [1-7] : ")
				l1 = ['question','marks','answer','op1','op2','op3','op4']
				if ch3 == '1' or ch3=='3' or ch3=='4' or ch3=='5' or ch3=='6' or ch3=='7':
					new_val = input(f"Enter New value for {l1[int(ch3)-1]} : ")
					statement = f"UPDATE questions SET {l1[int(ch3)-1]} = %s WHERE q_id=%s"
					cur.execute(statement, (new_val,q_id))
					return True
				elif ch3=='2':
					new_val = input(f"Enter New value for {l1[int(ch3)-1]} : ")
					if new_val.isnumeric():
						new_val = int(new_val)
						statement = f"UPDATE questions SET {l1[int(ch3)-1]} = %s WHERE q_id=%s"
						cur.execute(statement, (new_val,q_id))
						return True
					else:
						print("Invalid Input !")
				else:
					print("Please Enter Valid Input !")
			else:
				print("Please Enter Valid Input !")


	def view_applicants(self,constraint,val,condition):
		cur.execute(f"SELECT c_id FROM organization where admin_id = {self.admin_id};")
		company_id = list(cur)[0][0]
		if constraint=='f_name' or constraint=='stream' or constraint=='city':
			cur.execute("SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd WHERE sd.c_id = %s and sd.user_id = cd.user_id and cd.%s=%s;",(company_id,constraint,val))
		elif constraint=='age' or constraint=='cgpa' or constraint=='ssc_result' or constraint=='hsc_result':
			if condition=='1':
				cur.execute("SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd WHERE sd.c_id = %s and sd.user_id = cd.user_id and cd.%s < %s;",(company_id,constraint,val))
			elif condition=='2':
				cur.execute("SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd WHERE sd.c_id = %s and sd.user_id = cd.user_id and cd.%s > %s;",(company_id,constraint,val))
			else:
				print("Some loophole ! ")
		elif constraint=='tech':
			cur.execute("SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd, interested_tech AS it WHERE sd.c_id = %s and sd.user_id = cd.user_id and it.user_id = sd.user_id and it.tech = %s;",(company_id,val))
		else:
			cur.execute(f"SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd WHERE sd.c_id = {company_id} and sd.user_id = cd.user_id;")


		while True:

			for i in cur:
				print(f"user_id     {'name'.center(20,' ')}     marks")
				print(f"{i[0]}           {i[1].center(20,' ')}       {i[2]}")


			flag = input("Which candidate you want check ? Type User_id : ")
			if flag.isnumeric():
				uid = int(flag)
				super().__init__(uid)
				super().view_details()

				flag1 = input("\n\nDo You Want To select Him ? yes or no  ?  :  ")
				if flag1 == 'yes':
					cur.execute("UPDATE selection_details SET selection_status='selected' WHERE user_id=%s and c_id=%s",(uid,company_id))
					break
				elif flag1 == 'no':
					break
				else:
					print("Please enter valid input ! ")

				break
			else:
				print("Please Enter Valid Input !")

		return True



if __name__ == '__main__':
	
	import psycopg2
	import webbrowser

	hostname = 'localhost'
	database = 'ims'
	username = 'postgres'
	pwd = '28001398bhargav'
	port_id = 5432

	conn = psycopg2.connect(
		host = hostname,
		dbname = database,
		user = username,
		password = pwd,
		port =port_id)

	cur = conn.cursor()
	
	while True:
		print("Chose Your Role : ")
		print("1. Candidate")
		print("2. Company admin : ")
		print("3. Super Admin")
		print("4. Exit")

		choice = input("Please Enter Your Choice [1-3]: ")

		if choice == '1':
			while True : 
				print("1. Login")
				print("2. Register")
				print("3. Go back")
				choice1 = input("Please Enter your Choice [1-2] : ")
				if choice1 == '1':
					while True:
						uid = input("Please Enter Your Id : ")
						if uid.isnumeric():
							uid = int(uid)
							break
						else:
							print("Please Enter Valid uid ! ")
					password = input("Please Enter Your password : ")
					obj = validation(uid,password)
					if obj.validate_user():
						print("Successfully Logged In...")
						while True:
							print("1. View Details")
							print("2. Apply For interview")
							print("3. View Applications(selection_status,instuructions,your query)")
							print("4. update details")
							print("5. Go back")

							choice2 = input("Please Enter Your Choice [1-5] : ")
							obj = candidate(uid)
							if choice2 == '1':
								obj.view_details()
							elif choice2 == '2':
								if obj.Apply_interview():
									conn.commit()
									print("Test submitted Sucessfully")
									print("We will contact evaluate results in Short time and notify you ... ")
								else:
									print("Application Process Has been terminated ! ")
							elif choice2 == '3':
								obj.View_applications()
							elif choice2 == '4':
								l1 = ['password','f_name','l_name','mobile_n','email','age','ssc_result','hsc_result','stream','cgpa','city','resume']
								print("Which Detail You want to change ? ")
								print("1. password")
								print("2. first_name")
								print("3. last_name")
								print("4. mobile no.")
								print("5. email")
								print("6. age")
								print("7. ssc_result")
								print("8. hsc_result")
								print("9. stream")
								print("10. cgpa")
								print("11. city")
								print("12. resume")

								choice3 = input("Enter Your Choice [1-12] : ")
								if choice3 in ['1','2','3','4','5','9','11']:
									new_val = input(f"Please Enter New detail for {l1[int(choice3)-1]} : ")
									obj = candidate(uid)
									if obj.update_details(l1[int(choice3)-1],new_val):
										conn.commit()
										print("Detail Updated Sucessfully")
									else:
										print("There is some Error !")
								elif choice3 in ['6','7','8','10']:
									while True:
										new_val = input(f"Please Enter New detail for {l1[int(choice3)-1]} : ")
										if new_val.isnumeric():
											new_val = int(new_val)
											obj = candidate(uid)
											if obj.update_details(l1[int(choice3)-1],new_val):
												conn.commit()
												print("Detail Updated Sucessfully")
												break
											else:
												print("There is some Error !")
										else:
											print("Enter Valid Input !")
								elif choice3 == '12':
									while True:
										try:
											resume = input("Enter Your New Resume file  name : ")
											with open(resume, "rb") as File:
												resume = File.read()
												break
										except Exception as e:
											print('File not found ! Please Enter Valid File !...')
									obj = candidate(uid)
									if obj.update_details(l1[int(choice3)-1],resume):
										conn.commit()
										print("Detail Updated Sucessfully")
									else:
										print("There is some Error")
								else:
									print("Please Enter Valid Input !")

							elif choice2 == '5':
								break
							else:
								print("please Enter Valid Input !")

					else:
						print("Invalid Credentials !")

				elif choice1 == '2':
					streams = ['CE','ME','Chemical_Engi','Aironoticals','IT','Automobile','MBBS','BSC','BED','MSC','BA','Bcom','Mcom','MBA','BBA','BCA','MCA','MED','PTC','MVOC','BVOC','Micro_bio','Bio_Tech','pharmacy','nursing']
					tech = ['Ai','Ml','Web Developement','Cyber security','Adobe','XD','Ux_Ui','designing','App development']
					f_name = input("Enter Your first name : ")
					l_name = input("Enter Your last name : ")
					mobile_no = input("Enter Your mobile no : ")
					email = input("Enter Your email : ")
					while True:
						age = input("Enter Your age : ")
						if age.isnumeric():
							age = int(age)
							break
						else:
							print("Please Enter Valid Input !")
					password = input("Enter Your Password : ")
					while True:
						ssc_result = input("Enter Your ssc_result : ")
						try:
							ssc_result = float(ssc_result)
							ssc_result = int(ssc_result)
							if ssc_result > 0 and ssc_result<101:
								break
							else:
								print("Please Enter valid input !")
						except Exception:
							print("Please Enter Valid Input !")
					while True:
						hsc_result = input("Enter Your hsc_result : ")
						try:
							hsc_result = float(hsc_result)
							hsc_result = int(hsc_result)
							if hsc_result > 0 and hsc_result<101:
								break
							else:
								print("Please Enter valid input !")
						except Exception:
							print("Please Enter Valid Input !")

					print("Chose Your Stream : ")
					while True:
						j = 1
						for i in streams:
							print(f"{j}. {i}")
							j+=1
						stream_choice = input("Chose Your Stream : ")
						if stream_choice.isnumeric():
							stream = streams[int(stream_choice) -1]
							break
						else:
							print("Please Enter Valid Input!")

					while True:
						cgpa = input("Enter Your CGPA : ")
						try:
							cgpa = float(cgpa)
							cgpa = int(cgpa)
							if cgpa > 0 and cgpa < 11:
								break
							else:
								print("Please Enter valid input !")
						except Exception:
							print("Please Enter Valid Input !")

					city = input("Enter Your City :")
					while True:
						try:
							resume = input("Enter Your Resume file  name : ")
							with open(resume, "rb") as File:
								resume = File.read()
								break
						except Exception as e:
							print('File not found ! Please Enter Valid File !...')
					interested_tech = []
					while True:
						n = input("How many technologies you want to add as your interested tech ? : ")
						if n.isnumeric():
							n=int(n)
							while n>0:
								k = 1
								for i in tech:
									print(f"{k}. {i}")
									k+=1
								tech_choice = input("Enter Your choice : ")
								if tech_choice.isnumeric():
									interested_tech += [tech[int(tech_choice)-1]]
									n-=1
								else:
									print("Please Enter Valide Input !")
							break
						else:
							print("Please Enter Valid Input !")

					obj = registration(f_name,l_name,mobile_no,email,age,password,ssc_result,hsc_result,stream,cgpa,city,resume,interested_tech)
					if obj.register_user():
						conn.commit()
						print("You have Registred Sucessfully...")

				elif choice1 == '3':
					break
				else:
					print("Please Enter Valid Input")
		elif choice == '2':
			while True:
				uid = input("Please Enter Your Id : ")
				if uid.isnumeric():
					uid = int(uid)
					break
				else:
					print("Please enter valid id !")
			password = input("Please Enter Your password : ")
			obj = validation(uid,password)
			if obj.validate_admin():
				while True:
					print("1. View Company Details")
					print("2. Update Details")
					print("3. Applicants (select, give instructions)")
					print("4. Test Paper")
					print("5. go back")
					choice5 = input("Enter Your Choice [1-4] : ")
					obj = organization(uid)
					if choice5 == '1':
						obj.view_org_details()
					
					elif choice5 == '2':
						l1 = ['c_name','web_site','official_mail','admin_pass']
						print("Which Detail You Want to update ? ")
						print("1. organization name")
						print("2. web site link")
						print("3. official mail id")
						print("4. admin password")
						print("5. Go back")

						ch1 = input("Enter Your Choice [1-5] : ")
						if ch1 == '1' or ch1 == '2' or ch1 == '3' or ch1=='4':
							new_val = input(f"Please Enter New Value for {l1[int(ch1)-1]} : ")
							if obj.update_org_details(l1[int(ch1)-1],new_val):
								conn.commit()
								print("Detail Updated Sucessfully...")
							else:
								print("There is Some Error !")
						
						elif ch1 == '5':
							break
						else:
							print("Please enter valid input !")
					
					elif choice5  == '3':
						while True:
							print("1. Provide Instruction for selected candidates")
							print("2. View Applicants")
							ch6 = input("Enter Your Choice : ")
							if ch6 == '1':
								break
							elif ch6 == '2':
								l1 = ['f_name','age','ssc_result','hsc_result','stream','cgpa','city','tech']
								j = 1
								print("Add Filter ... To your search")
								for i in l1:
									print(f"{j}. {i}")
									j+=1
								print("8. interested_technologies")
								print("9. None")

								constraint = input("By Which parameter you want to filter your search ? : ")
								if constraint=='2' or constraint=='3' or constraint=='4' or constraint=='6':
									constraint = l1[int(constraint)-1]
									print("1. less than")
									print("2. grater than")
									ch7 = input("select your constraint : ")
									while True:
										val = input("Enter Value for selected constraint (< or > val)")
										if val.isnumeric():
											val = int(val)
											break
										else:
											print("Please Enter Valid input ! ")
									if ch7 == '1':
										if obj.view_applicants(constraint,val,'1'):
											conn.commit()
											break
										else:
											print("There is some Error !")
									elif ch7 == '2':
										if obj.view_applicants(constraint,val,'2'):
											conn.commit()
											break
										else:
											print("There is some Error !")
									else:
										print("please enter valid input !")

								elif constraint=='1' or constraint=='5' or constraint=='7':
									constraint = l1[int(constraint)-1]
									val = input("Enter the string which you want to add as constraint : ")
									if obj.view_applicants(constraint,val,'0'):
										conn.commit()
										break
									else:
										print("There is some Error !")

								elif constraint=='8':
									constraint = l1[int(constraint)-1]
									val = input("Enter the technology in which candidate must be interested : ")
									if obj.view_applicants(constraint,val,'0'):
										conn.commit()
										break
									else:
										print("There is some Error !")

								elif constraint=='9':
									if obj.view_applicants('None','None','None'):
										conn.commit()
										break
									else:
										print("There is some Error !")
								else:
									print("Please Enter Valid input !")
							else:
								print("please Enter valide input")
							
					elif choice5 == '4':
						print("1. Create A new question set")
						print("2. Edit question set")
						ch2 = input("Please Enter Your choice[1-2] : ")
						if ch2 == '1':
							if obj.create_test():
								conn.commit()
								print("Test Added Sucessfully !")
						elif ch2 == '2':
							if obj.update_test():
								conn.commit()
								print("Test has been updated Sucessfully ... ")
							
						else:
							print("Please Enter valid input")

					elif choice5 == '5':
						break
					else:
						print("Please enter valid input !")

			else:
				print("Invalid Credentials !")

		elif choice == '3':
			uid = input("Please Enter Your Id : ")
			password = input("Please Enter Your password : ")
			obj = validation(uid,password)
			if obj.validate_super_admin():
				while True:
					print("1. Insert Company")
					print("2. Delete Company")
					print("3. Delete user")
					print("4. Go Back")
					choice4 = input("Enter Your Choice : ")

					if choice4 == '1':
						c_name = input("Enter Company name : ")
						web_site = input("Enter the site link : ")
						official_mail = input("Enter official mail id of company : ")
						while True:
							admin_id = input("Enter the admin id : ")
							if admin_id.isnumeric():
								admin_id = int(admin_id)
								break
							else:
								print("Please Enter Valid admin_id !")
						admin_pass = input("Enter the admin password : ")

						obj = register_organization(c_name,web_site,official_mail,admin_id,admin_pass)
						if obj.register_comapny():
							conn.commit()
							print("Registration Successfully Done...")
						else:
							print("Some Error has been occured ! ")
					elif choice4 == '2':
						pass
						# print("Which Company You want to delete ? ")
						# cur.execute("SELECT c_id from organization")
						# for i in cur:
						# 	print(i)
						# del_company = input("Enter c_id of company which you want to delete : ")

					elif choice4 == '3':
						pass
					elif choice4 == '4':
						break
					else:
						print("Please Enter Valid input !")
			else:
				print("Invalid Credentials !")

		elif choice == '4':
			exit()
		else:
			print("Please enter valid input !")