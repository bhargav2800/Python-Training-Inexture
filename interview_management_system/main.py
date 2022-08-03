from candidate_user import candidate,user_registration
from organization_user import organization,organization_registration
from credential_validation import validation
import webbrowser
from datetime import datetime
from super_admin import management
import email_service
import validation_variable
import fetch_query
from query import execute_query

def register_user():
	statement = fetch_query.fetch_fields('streams','fieldsdata')
	parameters = None
	stream = execute_query(statement,parameters,'returned')

	 
	statement = fetch_query.fetch_fields('tech','fieldsdata')
	parameters = None
	tec = execute_query(statement,parameters,'returned')

	streams = []
	tech = []

	for i in stream:
		streams += [i[0]]
	for j in tec:
		tech += [j[0]]

	while True:
		f_name = input("Enter Your first name : ")
		if validation_variable.is_alpha(f_name):
			break
		else:
			print("Please Enter Valid f_name ! ")
	while True:
		l_name = input("Enter Your last name : ")
		if validation_variable.is_alpha(l_name):
			break
		else:
			print("Please Enter Valid l_name ! ")
	while True:
		mobile_no = input("Enter Your mobile no : ")
		if validation_variable.is_numeric(mobile_no):
			if len(mobile_no) == 10:
				break
			else:
				print("Please Enter Valid Mobile No !")
		else:
			print("Please Enter Valid Mobile No !")
	while True:	
		email = input("Enter Your email : ")
		if validation_variable.check_email(email):
			break
		else:
			print("Please Enter valid email ! ")
	while True:
		age = input("Enter Your age : ")
		if validation_variable.is_numeric(age):
			age = int(age)
			break
		else:
			print("Please Enter Valid Input !")
	while True:
		password = input("Enter Your Password : ")
		if validation_variable.check_pass(password):
			break
		else:
			print("Please Enter valid Password ! ")
			print("Constarints : \n uppercase letters: A-Z \n lowercase letters: a-z \n numbers: 0-9 \n any of the special characters: @#$%^&+=")

	while True:
		ssc_result = input("Enter Your ssc_result : ")
		ssc_result = validation_variable.is_valid_marks(ssc_result)
		if ssc_result != None:
			if ssc_result > 0 and ssc_result<101:
				break
			else:
				print("Please Enter valid input !")
		else:
			print("Please Enter Valid Input !")
		
			
	while True:
		hsc_result = input("Enter Your hsc_result : ")
		hsc_result = validation_variable.is_valid_marks(hsc_result)
		if hsc_result != None:
			if hsc_result > 0 and hsc_result<101:
				break
			else:
				print("Please Enter valid input !")
		else:
			print("Please Enter Valid Input !")

	print("Chose Your Stream : ")
	while True:
		j = 1
		for i in streams:
			print(f"{j}. {i}")
			j+=1
		stream_choice = input("Chose Your Stream : ")
		if validation_variable.is_numeric(stream_choice) and int(stream_choice) <= len(streams):
			stream = streams[int(stream_choice) -1]
			break
		else:
			print("Please Enter Valid Input!")

	while True:
		cgpa = input("Enter Your CGPA : ")
		cgpa = validation_variable.is_valid_marks(cgpa)
		if cgpa != None:
			if cgpa > 0 and cgpa<11:
				break
			else:
				print("Please Enter valid input !")
		else:
			print("Please Enter Valid Input !")

	while True:
		city = input("Enter Your City :")
		if validation_variable.is_alpha(city):
			break
		else:
			print("Please Enter Valid city ! ")
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
		if validation_variable.is_numeric(n):
			n=int(n)
			while n>0:
				k = 1
				for i in tech:
					print(f"{k}. {i}")
					k+=1
				tech_choice = input("Enter Your choice : ")
				if validation_variable.is_numeric(tech_choice) and int(tech_choice) > 0 and int(tech_choice)<10:
					interested_tech += [tech[int(tech_choice)-1]]
					n-=1
				else:
					print("Please Enter Valide Input !")
			break
		else:
			print("Please Enter Valid Input !")

	obj = user_registration(f_name,l_name,mobile_no,email,age,password,ssc_result,hsc_result,stream,cgpa,city,resume,interested_tech)
	if obj.register_user():
		return True


def view_company_details():
	data = obj.view_org_details()
	print(f"Company id : {data[0]}")
	print(f"Company name : {data[1]}")
	print(f"Company web site : {data[2]}")
	print(f"Company official mail id : {data[3]}")
	print(f"Company question set no : {data[4]}")


def update_company_details(ch1):
	l1 = ['c_name','web_site','official_mail','admin_pass']
	new_val = input(f"Please Enter New Value for {l1[int(ch1)-1]} : ")
	if obj.update_org_details(l1[int(ch1)-1],new_val):
		return True
	else:
		return False

def View_applicant():
	l1 = ['f_name','age','ssc_result','hsc_result','stream','cgpa','city','tech']
	j = 1
	print("Add Filter ... To your search")
	for i in l1:
		print(f"{j}. {i}")
		j+=1
	print("9. None")

	constraint = input("By Which parameter you want to filter your search ? : ")
	if constraint=='2' or constraint=='3' or constraint=='4' or constraint=='6':
		constraint = l1[int(constraint)-1]
		print("1. less than")
		print("2. grater than")
		ch7 = input("select your constraint : ")
		while True:
			val = input("Enter Value for selected constraint (< or > val)")
			if validation_variable.is_numeric(val):
				val = int(val)
				break
			else:
				print("Please Enter Valid input ! ")
		if ch7 == '1':
			c_id,temp,l = obj.view_applicants(constraint,val,'1')
			
			if temp:
				ids = []
				print(f"user_id     {'name'.center(20,' ')}     marks")
				for i in l:
					print(f"{i[0]}           {i[1].center(20,' ')}       {i[2]}")
					ids += [i[0]]
				flag = input("Which candidate you want check ? Type User_id : ")
				if validation_variable.is_numeric(flag) and int(flag) in ids:
					uid = int(flag)
					l1,flag3 = obj.view_user_details(uid,c_id)

					if flag3:
						print("User_id : ", l1[0])
						print("f_name : ", l1[2])
						print("l_name : ", l1[3])
						print("mobile_no : ", l1[4])
						print("email : ", l1[5])
						print("age : ", l1[6])
						print("ssc_result : ", l1[7])
						print("hsc_result : ", l1[8])
						print("stream : ", l1[9])
						print("CGPA : ", l1[10])
						print("city : ", l1[11])
						while True:
							flag = input("For View Resume type 'yes' Else type 'no:  ")

							if flag=='yes':
								storeFilePath = "file.pdf"
								with open(storeFilePath,"wb") as File:
									File.write(l1[12])
									File.close()
								webbrowser.open(storeFilePath)
								break
							elif flag=='no':
								break
							else:
								print("Invalid Input !")

						flag1 = input("\n\nDo You Want To select This Candidate? yes or no  ?  :  ")
						if flag1 == 'yes':
							obj.select_candidate(uid,c_id,'selected')
							# break
						elif flag1 == 'no':
							obj.select_candidate(uid,c_id,'rejected')
							# break
						else:
							print("Please enter valid input ! ")
					else:
						print("Invalid id has been entered ! ")
				else:
					print("Invalid Input !")
			else:
				print("No Candidate Found !")
			# break

		elif ch7 == '2':
			c_id,temp,l = obj.view_applicants(constraint,val,'2')
			if temp:
				ids = []
				print(f"user_id     {'name'.center(20,' ')}     marks")
				for i in l:
					print(f"{i[0]}           {i[1].center(20,' ')}       {i[2]}")
					ids += [i[0]]
				flag = input("Which candidate you want check ? Type User_id : ")
				if validation_variable.is_numeric(flag) and int(flag) in ids:
					uid = int(flag)
					l1,flag3 = obj.view_user_details(uid,c_id)
					if flag3:
						print("User_id : ", l1[0])
						print("f_name : ", l1[2])
						print("l_name : ", l1[3])
						print("mobile_no : ", l1[4])
						print("email : ", l1[5])
						print("age : ", l1[6])
						print("ssc_result : ", l1[7])
						print("hsc_result : ", l1[8])
						print("stream : ", l1[9])
						print("CGPA : ", l1[10])
						print("city : ", l1[11])
						while True:
							flag = input("For View Resume type 'yes' Else type 'no:  ")

							if flag=='yes':
								storeFilePath = "file.pdf"
								with open(storeFilePath,"wb") as File:
									File.write(l1[12])
									File.close()
								webbrowser.open(storeFilePath)
								break
							elif flag=='no':
								break
							else:
								print("Invalid Input !")

						flag1 = input("\n\nDo You Want To select This candidate? yes or no  ?  :  ")
						if flag1 == 'yes':
							obj.select_candidate(uid,c_id,'selected')
							# break
						elif flag1 == 'no':
							obj.select_candidate(uid,c_id,'rejected')
							# break
						else:
							print("Please enter valid input ! ")
					else:
						print("Invalid id has been entered ! ")
				else:
					print("Invalid Input !")
			else:
				print("No Candidate Found !")
			# break
		else:
			print("please enter valid input !")

	elif constraint=='1' or constraint=='5' or constraint=='7':
		constraint = l1[int(constraint)-1]
		val = input("Enter the string which you want to add as constraint : ")
		c_id,temp,l = obj.view_applicants(constraint,val,'0')
		if temp:
			ids = []
			print(f"user_id     {'name'.center(20,' ')}     marks")
			for i in l:
				print(f"{i[0]}           {i[1].center(20,' ')}       {i[2]}")
				ids += [i[0]]
			flag = input("Which candidate you want check ? Type User_id : ")
			if validation_variable.is_numeric(flag) and int(flag) in ids:
				uid = int(flag)
				l1,flag3 = obj.view_user_details(uid,c_id)
				if flag3:
					print("User_id : ", l1[0])
					print("f_name : ", l1[2])
					print("l_name : ", l1[3])
					print("mobile_no : ", l1[4])
					print("email : ", l1[5])
					print("age : ", l1[6])
					print("ssc_result : ", l1[7])
					print("hsc_result : ", l1[8])
					print("stream : ", l1[9])
					print("CGPA : ", l1[10])
					print("city : ", l1[11])
					while True:
						flag = input("For View Resume type 'yes' Else type 'no:  ")

						if flag=='yes':
							storeFilePath = "file.pdf"
							with open(storeFilePath,"wb") as File:
								File.write(l1[12])
								File.close()
							webbrowser.open(storeFilePath)
							break
						elif flag=='no':
							break
						else:
							print("Invalid Input !")

					flag1 = input("\n\nDo You Want To select This candidate? yes or no  ?  :  ")
					if flag1 == 'yes':
						obj.select_candidate(uid,c_id,'selected')
						# break
					elif flag1 == 'no':
						obj.select_candidate(uid,c_id,'rejected')
						# break
					else:
						print("Please enter valid input ! ")
				else:
					print("Invalid id has been entered ! ")
			else:
				print("Invalid Input !")
		else:
			print("No Candidate Found !")
		# break

	elif constraint=='8':
		constraint = l1[int(constraint)-1]
		val = input("Enter the technology in which candidate must be interested : ")
		c_id,temp,l = obj.view_applicants(constraint,val,'0')
		if temp:
			ids = []
			print(f"user_id     {'name'.center(20,' ')}     marks")
			for i in l:
				print(f"{i[0]}           {i[1].center(20,' ')}       {i[2]}")
				ids += [i[0]]
			flag = input("Which candidate you want check ? Type User_id : ")
			if validation_variable.is_numeric(flag) and int(flag) in ids:
				uid = int(flag)
				l1,flag3 = obj.view_user_details(uid,c_id)
				if flag3:
					print("User_id : ", l1[0])
					print("f_name : ", l1[2])
					print("l_name : ", l1[3])
					print("mobile_no : ", l1[4])
					print("email : ", l1[5])
					print("age : ", l1[6])
					print("ssc_result : ", l1[7])
					print("hsc_result : ", l1[8])
					print("stream : ", l1[9])
					print("CGPA : ", l1[10])
					print("city : ", l1[11])
					while True:
						flag = input("For View Resume type 'yes' Else type 'no:  ")

						if flag=='yes':
							storeFilePath = "file.pdf"
							with open(storeFilePath,"wb") as File:
								File.write(l1[12])
								File.close()
							webbrowser.open(storeFilePath)
							break
						elif flag=='no':
							break
						else:
							print("Invalid Input !")

					flag1 = input("\n\nDo You Want To select This candidate? yes or no  ?  :  ")
					if flag1 == 'yes':
						obj.select_candidate(uid,c_id,'selected')
						# break
					elif flag1 == 'no':
						obj.select_candidate(uid,c_id,'rejected')
						# break
					else:
						print("Please enter valid input ! ")
				else:
					print("Invalid id has been entered ! ")
			else:
				print("Invalid Input !")
		
		else:
			print("No Candidate Found !")
		# break

	elif constraint=='9':
		c_id,temp,l = obj.view_applicants('None','None','None')
		if temp:
			ids = []
			print(f"user_id     {'name'.center(20,' ')}     marks")
			for i in l:
				print(f"{i[0]}           {i[1].center(20,' ')}       {i[2]}")
				ids += [i[0]]
			flag = input("Which candidate you want check ? Type User_id : ")
			if validation_variable.is_numeric(flag) and int(flag) in ids:
				uid = int(flag)
				l1,flag3 = obj.view_user_details(uid,c_id)
				if flag3:
					print("User_id : ", l1[0])
					print("f_name : ", l1[2])
					print("l_name : ", l1[3])
					print("mobile_no : ", l1[4])
					print("email : ", l1[5])
					print("age : ", l1[6])
					print("ssc_result : ", l1[7])
					print("hsc_result : ", l1[8])
					print("stream : ", l1[9])
					print("CGPA : ", l1[10])
					print("city : ", l1[11])
					while True:
						flag = input("For View Resume type 'yes' Else type 'no:  ")

						if flag=='yes':
							storeFilePath = "file.pdf"
							with open(storeFilePath,"wb") as File:
								File.write(l1[12])
								File.close()
							webbrowser.open(storeFilePath)
							break
						elif flag=='no':
							break
						else:
							print("Invalid Input !")

					flag1 = input("\n\nDo You Want To select This candidate? yes or no  ?  :  ")
					if flag1 == 'yes':
						email = obj.select_candidate(uid,c_id,'selected')
						message = input("Type Email Instructions For Selected candidate : ")
						email_service.email_module(email[0],message)
						# break
					elif flag1 == 'no':
						email = obj.select_candidate(uid,c_id,'rejected')
						message = input("Enter The Reason For Reject Him/Her  :  ")
						email_service.email_module(email[0],message)
						# break
					else:
						print("Please enter valid input ! ")
				else:
					print("Invalid id has been entered ! ")
			else:
				print("Invalid Input !")
		else:
			print("No Candidate Found !")
		# break
	else:
		print("Please Enter Valid input !")
	# break
	return


def provide_instruction():
	c_id,temp,l = obj.view_applicants(None,None,None)
	if temp:
		ids = []
		print(f"user_id     {'name'.center(20,' ')}     marks")	
		for i in l:
			print(f"{i[0]}           {i[1].center(20,' ')}       {i[2]}")
			ids += [i[0]]
		flag = input("For Which candidate you want to add/update Information ? Type User_id : ")
		if validation_variable.is_numeric(flag) and (int(flag) in ids):
			uid = int(flag)
			while True:
				date_time = str(input('Enter date_time in format(yyyy-mm-dd hh:mm) : '))
				if validation_variable.validate_date(date_time):
					break
				else:
					print("Please Enter Date and time in given format only")
					
			location = input("Enter the location of offline interview : ")
			other_instuctions = input("Please Enter Other Instructions for candidate : ")

			instruction = f"Date and Time : {date_time} \nlocation : {location} \nOther_instruction : {other_instuctions}"

			email =  obj.provide_instruction(instruction,c_id,uid)
			print("\nInstructions Added Sucessfully...\n")
			message1 = f"\nYou have a further instructions from :\norganization's company_id:{c_id}\nInformation:{instruction}\nNote: You can see on app"
			email_service.email_module(email[0],message1)
			return True

		else:
			print("Invalid User_id !")
	else:
		return False



def user_query_reply():
	flag,c_id,query_result = obj.view_user_queries()
							
	if flag != None and c_id != None:
		uid_lst = []
		print(f"user_id     c_id        {'Your_query'.center(50,' ')}        {'responce'.center(50,' ')}")
		for i in query_result:
			print(f"  {i[0]}       {i[1]}        {i[2].center(50,' ')}        {i[3].center(50,' ')}")
			uid_lst += [i[0]]
		uid = input("\nWhich user's query you want to reply ? Type user_id")
		if validation_variable.is_numeric(uid) and (int(uid) in uid_lst):
			message = input("Please Enter Your Responce : ")
			email,company_id = obj.reply_to_querires(uid,c_id,message)
			print("Responded Sucessfully ! ")

			message1 = f"\nYou have responce For Your Query:\norganization's c_id:{company_id}\nResponce:{message}\nNote: You can see on app"

			email_service.email_module(email[0],message1)

			return True
				
		else:
			print("Invalid User_id !")
	else:
		return False




def create_test():
	role = input("Enter the Role For which hiring is open   :  ")
	question_lst = []
	no_of_question = input("Please Enter Number of questions")
	if validation_variable.is_numeric(no_of_question):
		no_of_question = int(no_of_question)
		i=0
		while i < no_of_question:
			print(f"*****************  QUESTION - {i+1} ***********")
			options = []
			while True:
				marks = input(f"Enter the marks for question-{i+1} : ")
				if validation_variable.is_numeric(marks):
					marks = int(marks)
					break
				else:
					print("Please Enter Valid Marks !")

			question = input(f"Enter Question-{i+1} : ")
			for j in range(4):
				while True:
					op = input(f"Enter Op{j+1} for question-{i+1}")
					if op in options:
						print("Please Add Unique Options for question ! ")
					else:
						options += [op]
						break
			
			while True:
				for k in range(4):
					print(f"{k+1}. {options[k]}")
				answer = input("Select answer for this question")
				if answer == '1' or answer =='2'or answer=='3' or answer=='4':
					answer = options[int(answer)-1]
					l = [question,marks,answer,options[0],options[1],options[2],options[3]]
					question_lst += [l]
					i = i+1
					break
				else:
					print("Invalid Input!")

		if obj.create_test(question_lst,role):
			return True

	else:
		print("Please Enter Valid input !")


def update_test():
	flag,l1 = obj.display_questions()
	if flag:
		print(f"\nq_id     q_set{'question'.center(20,' ')}marks{'answer'.center(15,' ')}{'op1'.center(15,' ')}{'op2'.center(15,' ')}{'op3'.center(15,' ')}{'op4'.center(15,' ')}   \n")
		for i in l1:
			print(f"   {i[0]}      {i[1]}{i[2].center(20,' ')}     {i[3]}{i[4].center(15,' ')}{i[5].center(15,' ')}{i[6].center(15,' ')}{i[7].center(15,' ')}{i[8].center(15,' ')}")
		while True:
			q_id = input("Please Enter q_id of question which you want to update...")
			if validation_variable.is_numeric(q_id):
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

					if obj.update_question(l1[int(ch3)-1],new_val,q_id):
						print("Test has been updated Sucessfully ... ")
					else:
						print("Invalid Input !")

					break
				elif ch3=='2':
					new_val = input(f"Enter New value for {l1[int(ch3)-1]} : ")
					if validation_variable.is_numeric(new_val):
						new_val = int(new_val)

						if obj.update_question(l1[int(ch3)-1],new_val,q_id):
							return True
						else:
							print("Invalid Input !")
						
						break
					else:
						print("Invalid Input !")
				else:
					print("Please Enter Valid Input !")
			else:
				print("Please Enter Valid Input !")
	else:
		print("\n\nYou have not Created Your Test !\n")


def insert_company():
	c_name = input("Enter Company name : ")
	web_site = input("Enter the site link : ")
	while True:
		official_mail = input("Enter official mail id of company : ")
		if validation_variable.check_email(official_mail):
			break
		else:
			print("Please enter valid email !")
	while True:
		admin_id = input("Enter the admin id : ")
		if validation_variable.is_numeric(admin_id):
			admin_id = int(admin_id)
			break
		else:
			print("Please Enter Valid admin_id !")
	admin_pass = input("Enter the admin password : ")

	obj = organization_registration(c_name,web_site,official_mail,admin_id,admin_pass)
	if obj.register_comapny():
		return True
	else:
		return False


def delete_org():
	obj = management()
	org_details = obj.view_organizations()
	cid_lst = []
	for i in org_details:
		print("c_id      c_name      ")
		print(f"{i[0]}       i{1}")
		cid_lst += [i[0]]
	cid = input("Which Company You want to delete ? Type c_id")
	if validation_variable.is_numeric(cid) and int(cid) in cid_lst:
		cid=int(cid)
		if obj.delete_organization(cid):
			return True
		else:
			return False
	else:
		print("Invalid Input !")


def delete_user():
	obj = management()
	can_Details = obj.view_candidates()
	uid_lst = []
	print("user_id      f_name     email ")
	for i in can_Details:
		print(f"{i[0]}       {i[1]}      {i[2]}")
		uid_lst += [i[0]]
	uid = input("Which Candidate You want to delete ? Type user_id")
	if validation_variable.is_numeric(uid) and int(uid) in uid_lst:
		uid=int(uid)
		if obj.delete_candidates(uid):
			return True
		else:
			return False
	else:
		print("Invalid Input !")


def view_org():
	obj = management()
	org_details = obj.view_organizations()
	print("c_id      c_name      ")
	for i in org_details:
		print(f"{i[0]}       i{1}")

def view_candidat():
	obj = management()
	can_Details = obj.view_candidates()
	print("user_id      f_name     email ")
	for i in can_Details:
		print(f"{i[0]}       {i[1]}      {i[2]}")


def view_user_self_details():
	data = obj.view_details()
	print("User_id : ", data[0])
	print("f_name : ", data[2])
	print("l_name : ", data[3])
	print("mobile_no : ", data[4])
	print("email : ", data[5])
	print("age : ", data[6])
	print("ssc_result : ", data[7])
	print("hsc_result : ", data[8])
	print("stream : ", data[9])
	print("CGPA : ", data[10])
	print("city : ", data[11])

	while True:
		flag = input("For View Resume type 'yes' Else type 'no:  ")

		if flag=='yes':
			storeFilePath = "file.pdf"
			with open(storeFilePath,"wb") as File:
				File.write(data[12])
				File.close()
			webbrowser.open(storeFilePath)
			break
		elif flag=='no':
			break
		else:
			print("Please Enter Valid Input")

def apply_for_interview():
	c_id,result,flag = obj.Apply_interview(1,0,0)
	print("In Which Company You want to apply for interview ? Please Enter a C_id of that company : ")
	print(f"c_id     {'c_name'.center(20,' ')}{'web_site'.center(20,' ')}{'official_mail'.center(30,' ')}{'Hiring_Role'.center(30,' ')}")
	c_id_lst = []
	for i in result:
		print(f"{i[0]}        {i[1].center(20,' ')}{i[2].center(20,' ')}{i[3].center(30,' ')}{i[4].center(30,' ')}")
		c_id_lst += [i[0]]
	c_id = input("Enter c_id of company in which you want to apply for interview test: ")

	c_id,test,flag = obj.Apply_interview(0,c_id,c_id_lst)

	if flag:
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

		print(f"Your Result : {gained_marks}/{Total_marks}... ")

		if obj.take_test(c_id,gained_marks):
			return True

		else:
			print("Application Process Has been terminated ! ")
	
	elif flag==None:
		print("Please Enter Valid Input ! ")
	else:
		print("You have Alredy Apear in test ! You can not Re-attempt it !...")



def view_application():
	query_result = obj.View_applications()
	print(f"user_id      Company_id      {'Comapany_name'.center(20,' ')}     Marks     {'selection_status'.center(30,' ')}{'Instruction_by_company'.center(30,' ')}")


	if len(query_result) == 0:
		print("No Apllications Found ! ")
	else:
		for i in query_result:
			l1 = f"{i[5]}"
			print(f"{i[0]}                {i[1]}      {i[2].center(20,' ')}           {i[3]}         {i[4].center(30,' ')}{l1.center(30,' ')}")

def update_user_details():
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
			return True
		else:
			return False
	elif choice3 in ['6','7','8','10']:
		while True:
			new_val = input(f"Please Enter New detail for {l1[int(choice3)-1]} : ")
			if validation_variable.is_numeric(new_val):
				new_val = int(new_val)
				obj = candidate(uid)
				if obj.update_details(l1[int(choice3)-1],new_val):
					return True
					
				else:
					return False
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
			return True
		else:
			return False
	else:
		print("Please Enter Valid Input !")


def submit_user_query():
	query_result = obj.View_applications()

	if len(query_result) == 0:
		print("\nNo Apllications Found ! \n")
	else:
		print(f"user_id      Company_id      {'Comapany_name'.center(20,' ')}     Marks     {'selection_status'.center(30,' ')}{'Instruction_by_company'.center(30,' ')}")
		cid_lst = {}
		for i in query_result:
			l1 = f"{i[5]}"
			print(f"{i[0]}                {i[1]}      {i[2].center(20,' ')}           {i[3]}         {i[4].center(30,' ')}{l1.center(30,' ')}")

			cid_lst[i[1]] = i[4]

		while True:
			c_id = input("In Which Company you want to put your query ? Type C_id")
			if validation_variable.is_numeric(c_id) and (int(c_id) in cid_lst):
				break
			else:
				print("Please Enter valid C_id ! ")

		if cid_lst[int(c_id)] == 'selected':
			query = input("Enter Your Query message : ")
			email,user_id = obj.submit_query(query,c_id)

			message = f"\nYou Have A Query From Applicant:\nApplicants User_id:{user_id}\nquery:{query}\nNote: You can Respond him via app"

			if email_service.email_module(email[0],message):
				return True
			else:
				return False
		else:
			print("Your Applicantion is under observation! You can put your querry only if you will selected ! ")

def view_query_responce():
	query_result = obj.view_query()
	if len(query_result) == 0:
		print("\nNo Queris Found ! ")
	
	else:
		print(f"user_id     c_id        {'Your_query'.center(50,' ')}        {'responce'.center(50,' ')}")
		for i in query_result:
			print(f"  {i[0]}       {i[1]}        {i[2].center(50,' ')}        {i[3].center(50,' ')}")

if __name__ == '__main__':

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
						uid = input("Please Enter Your Email-Id : ")
						if validation_variable.check_email(uid):
							break
						else:
							print("Please Enter Valid Email-id ! ")
					password = input("Please Enter Your password : ")
					obj = validation(uid,password)
					if obj.validate_user():
						print("Successfully Logged In...")
						uid = obj.fetch_uid()
						while True:
							print("1. View Details")
							print("2. Apply For interview")
							print("3. View Applications(selection_status,instuructions)")
							print("4. update details")
							print("5. Submit Query")
							print("6. View Query responce")
							print("7. Go back")

							choice2 = input("Please Enter Your Choice [1-5] : ")
							obj = candidate(uid)
							if choice2 == '1':
								view_user_self_details()
							elif choice2 == '2':
								if apply_for_interview():
									print("Test submitted Sucessfully")
									print("We will evaluate results in Short time and notify you ... ")
								else:
									print("Test Is not submitted !")

							elif choice2 == '3':
								view_application()


							elif choice2 == '4':
								if update_user_details():
									print("Detail Updated Sucessfully")
								else:
									print("Not Updated Sucessfully !")

							elif choice2 == '5':
								if submit_user_query():
									print("Query submitted Successfully ! And Mail Has Been Sent ")
								else:
									print("Error in sending Mail !")


							elif choice2 == '6':
								view_query_responce()


							elif choice2 == '7':
								break

							else:
								print("please Enter Valid Input !")

					else:
						print("Invalid Credentials !")	

				elif choice1 == '2':
					if register_user():
						print("You have Registred Sucessfully...")
					else:
						print("Registration Has not been Done !")

				elif choice1 == '3':
					break
				else:
					print("Please Enter Valid Input")
		elif choice == '2':
			while True:
				uid = input("Please Enter Your Id : ")
				if validation_variable.is_numeric(uid):
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
					print("4. Start Hiring Process")
					print("5. Close Hiring Process")
					print("6. go back")
					choice5 = input("Enter Your Choice [1-4] : ")
					obj = organization(uid)
					if choice5 == '1':
						view_company_details()

					elif choice5 == '2':
						print("Which Detail You Want to update ? ")
						print("1. organization name")
						print("2. web site link")
						print("3. official mail id")
						print("4. admin password")
						print("5. Go back")

						ch1 = input("Enter Your Choice [1-5] : ")
						if ch1 == '1' or ch1 == '2' or ch1 == '3' or ch1=='4':
							if update_company_details(ch1):
								print("Updated Sucessfully")
							else:
								print("Not Updated ! Some Error Has Been occured !")
						
						elif ch1 == '5':
							break
						else:
							print("Please enter valid input !")
					
					elif choice5  == '3':
					
						print("1. View Applicants")
						print("2. Provide Information for selected candidates")
						print("3. Update Information for selected candidates")
						print("4. Reply to user's query")
						print("5. Go back")

						ch6 = input("Enter Your Choice : ")

						if ch6 == '1':
							View_applicant()
							break

						elif ch6 == '2' or ch6 == '3':
							if provide_instruction():
								print("Mail Send Sucessfully")
							else:
								print("No Candidate Found !")

						elif ch6 == '4':
							if user_query_reply():
								print("Mail Send Sucessfully")
							else:
								print("\nNo Queris Found ! ")

						elif ch6 == '5':
							break

						else:
							print("Please Enter Valid Input ! ")

					elif choice5 == '4':
						print("1. Create A new question set")
						print("2. Update question set")
						ch2 = input("Please Enter Your choice[1-2] : ")
						if ch2 == '1':
							if create_test():
								print("Test Added Sucessfully !")
							else:
								print("Some Error Has Been Occured !")

						elif ch2 == '2':
							if update_test():
								print("Test has been updated Sucessfully ... ")
							else:
								print("Test is Not Submit ! Some Error has Been occured !")
							
						else:
							print("Please Enter valid input")

					elif choice5 == '5':
						if obj.close_hiring():
							print("Hiring Is Sucessfully Closed !")

					elif choice5 == '6':
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
					print("4. View Companies")
					print("5. View Users")
					print("6. Go Back")
					choice4 = input("Enter Your Choice : ")
					if choice4 == '1':
						if insert_company():
							print("Registration Successfully Done...")
						else:
							print("Some Error Has Been Occured !")

					elif choice4 == '2':
						if delete_org():
							print("Deleted Sucessfully ")
						else:
							print("You can not delete organization First Delete It's Users")

					elif choice4 == '3':
						if delete_user():
							print("Successfully Deleted")
						else:
							print("Some Error has Been Occured !")
						
					elif choice4 == '4':	
						view_org()
					elif choice4 == '5':
						view_candidat()
					
					elif choice4 == '6':
						break
					
					else:
						print("Please Enter Valid input !")
			else:
				print("Invalid Credentials !")

		elif choice == '4':
			exit()
		else:
			print("Please enter valid input !")