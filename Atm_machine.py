import random

# DataBase Formate
# banks = {
# 	banks_name:{
# 		"users":{
# 			"user_id":{user_details}
# 		}
# 		"atms":{atm_name:{atm_details}}
# 		"admin":{admin_details}
# 		"slogan": slogan_of_bank
# 	}
# }


# DataBase
banks = {
	"hdfc":{
		"users":{
			"u1":{"account_no":"1234567891","name":"Bhargav","Bank":"hdfc","Balance":4000,"card_no":"1234-5678-9876-5431","mobile_no":"9662316938","pin":"2800","day_tansactions":0,"day_withdrawl":0,"day_deposite":0},
			"u2":{"account_no":"1234567892","name":"Ayushi","Bank":"hdfc","Balance":5000,"card_no":"1234-5678-9876-5432","mobile_no":"6753467891","pin":"1398","day_tansactions":0,"day_withdrawl":0,"day_deposite":0}
		},
		"atms":{"hdfc-naroda":{"balance":50000,"Pin-code":"382715","per_trans_limit":30000}, "hdfc-bopal":{"balance":40000,"Pin-code":"382711","per_trans_limit":20000}, "hdfc-gurukul":{"balance":70000,"Pin-code":"382719","per_trans_limit":40000}},
		"admin":{"name":"Shivam","admin_id":"7891","password":"1231"},
		"slogan" : "With HDFC Safe your Money"
	},
	"icici":{
		"users":{
			"u1":{"account_no":"1234567893","name":"Meet","Bank":"icici","Balance":74000,"card_no":"1234-5678-9876-5433","mobile_no":"1236549870","pin":"2000","day_tansactions":0,"day_withdrawl":0,"day_deposite":0},
		},
		"atms":{"icici-naroda":{"balance":40000,"Pin-code":"382725","per_trans_limit":40000}, "icici-iscon":{"balance":50000,"Pin-code":"381715","per_trans_limit":50000}, "icici-thaltej":{"balance":90000,"Pin-code":"482715","per_trans_limit":35000}},
		"admin":{"name":"Rutvik","admin_id":"7892","password":"1232"},
		"slogan" : "With ICICI Safe your Money"
	},
	"kotak":{
		"users":{
			"u1":{"account_no":"1234567894","name":"Himani","Bank":"kotak","Balance":4000,"card_no":"1234-5678-9876-5434","mobile_no":"9874561239","pin":"3000","day_tansactions":0,"day_withdrawl":0,"day_deposite":0},
			"u2":{"account_no":"1234567895","name":"Mansi","Bank":"kotak","Balance":84000,"card_no":"1234-5678-9876-5435","pin":"4000","day_tansactions":0,"day_withdrawl":0,"day_deposite":0}
		},
		"atms":{"kotak-naroda":{"balance":40000,"Pin-code":"322715","per_trans_limit":20000}, "kotak-iscon":{"balance":50000,"Pin-code":"382111","per_trans_limit":10000}, "kotak-gota":{"balance":60000,"Pin-code":"882715","per_trans_limit":25000}},
		"admin":{"name":"keval","admin_id":"7893","password":"1233"},
		"slogan" : "With KOTAK Safe your Money"
	},
	"axis":{
		"users":{
			"u1":{"account_no":"1234567896","name":"Meet","Bank":"axis","Balance":4000,"card_no":"1234-5678-9876-5436","mobile_no":"1239876540","pin":"5000","day_tansactions":0,"day_withdrawl":0,"day_deposite":0},
			"u2":{"account_no":"1234567897","name":"Prince","Bank":"axis","Balance":84000,"card_no":"1234-5678-9876-5437","mobile_no":"4569871230","pin":"6000","day_tansactions":0,"day_withdrawl":0,"day_deposite":0}
		},
		"atms":{"axis-naroda":{"balance":75000,"Pin-code":"982715","per_trans_limit":25000}, "axis-iscon":{"balance":85000,"Pin-code":"387715","per_trans_limit":15000}, "axis-Maninagar":{"balance":86000,"Pin-code":"382775","per_trans_limit":20000}},
		"admin":{"name":"Hetvi","admin_id":"7894","password":"1234"},
		"slogan" : "With axis Safe your Money"
	}
}


# User Validation Function
def user_validation(banks, bank_chose, atm_chose):

	y = [banks[i]["users"][j]["card_no"] for i in banks for j in banks[i]["users"]]

	print(f"Welcome to {bank_chose} Atm ! \n")

	card_no = input('Please enter your card number : ')
	if card_no in y:
		#["bank_name","user_id"]
		location = [[i,j] for i in banks for j in banks[i]["users"] if banks[i]["users"][j]["card_no"] == card_no][0]
		pin = input('Please enter you pin : ')

		if pin == banks[location[0]]["users"][location[1]]["pin"]:
			user_transaction(location,card_no,bank_chose,atm_chose)
		else:
			print("Invalid Pin !\n")

	else : 
		print("Invalid Card No !\n")



#User Transaction Function
def user_transaction(location,card_no,bank_chose,atm_chose):
	print("Please select your transaction")
	print("1. My details")
	print("2. Withdrawl")
	print("3. Deposite")
	print("4. Check Balance")
	print("5. Change PIN\n")

	transction = input('Enter your choice [1-5]')
	#My Details
	if transction=='1':
		print("Account No. :", banks[location[0]]["users"][location[1]]["account_no"])
		print("Card No. : ", card_no)
		print("Name : ", banks[location[0]]["users"][location[1]]["name"])
		print("Bank : ", banks[location[0]]["users"][location[1]]["Bank"])
		print("Balance : ", banks[location[0]]["users"][location[1]]["Balance"])
		print("Phone NO.", banks[location[0]]["users"][location[1]]["mobile_no"])
		print("No. of transaction Today: ", banks[location[0]]["users"][location[1]]["day_tansactions"])
		print("Total Withdrawl amount today : ", banks[location[0]]["users"][location[1]]["day_withdrawl"])
		print("Total Deposite amount today : ", banks[location[0]]["users"][location[1]]["day_deposite"],"\n")

	# Withdrawl
	elif transction=='2':
		if banks[location[0]]["users"][location[1]]["day_tansactions"] < 3:
			amount = int(input('Please Enter the Withdrawl amount : '))
			if amount <= banks[bank_chose]["atms"][atm_chose]["per_trans_limit"]:
				if amount%100 == 0:
					if banks[location[0]]["users"][location[1]]["day_withdrawl"]+amount <= 50000:
						if bank_chose == banks[location[0]]["users"][location[1]]["Bank"]:
							if banks[bank_chose]["atms"][atm_chose]["balance"] < amount:
								print("Atm has not enough money !\n")
							else:
								if amount > banks[location[0]]["users"][location[1]]["Balance"]:
									print("Insufficient Account Balance !\n")
								else:
									banks[location[0]]["users"][location[1]]["Balance"] -= amount
									banks[location[0]]["users"][location[1]]["day_withdrawl"] += amount
									print("\n{} You have sucessfully Withdrawl {} rupees".format(banks[location[0]]["users"][location[1]]["name"],amount))
									print("{} Your Available Balance : {}".format(banks[location[0]]["users"][location[1]]["name"],banks[location[0]]["users"][location[1]]["Balance"]),"\n")
									banks[location[0]]["users"][location[1]]["day_tansactions"] += 1
									banks[bank_chose]["atms"][atm_chose]["balance"] -= amount
						else:
							if banks[bank_chose]["atms"][atm_chose]["balance"] < amount:
								print("Atm has not enough money !\n")
							else:
								if amount+(amount*0.05) > banks[location[0]]["users"][location[1]]["Balance"]:
									print("Insufficient Account Balance !\n")
								else:
									banks[location[0]]["users"][location[1]]["Balance"] -= amount+(amount*0.05)
									banks[location[0]]["users"][location[1]]["day_withdrawl"] += amount
									print("\n{} You have sucessfully Withdrawl {} rupees".format(banks[location[0]]["users"][location[1]]["name"],amount))
									print(f"5% Transaction Charge is applied")
									print("{} Your Available Balance : {}".format(banks[location[0]]["users"][location[1]]["name"],banks[location[0]]["users"][location[1]]["Balance"]),"\n")
									banks[location[0]]["users"][location[1]]["day_tansactions"] += 1
									banks[bank_chose]["atms"][atm_chose]["balance"] -= amount

					else:
						print("Transaction Failed !")
						print("You are not allow to Withdrawl more then 50000 per day !\n")
				else:
					print("Transaction Failed !")
					print("Your transaction amount should be in multiple of 100\n")
			else:
				print("Transaction Failed !")
				print("Your transaction should be less then {} for {} ATM\n".format(banks[bank_chose]["atms"][atm_chose]["per_trans_limit"],atm_chose))
		else:
			print("Transaction Failed!")
			print("You have reached to limit of 3 transaction per day !\n")

	#Deposite
	elif transction=='3':
		if banks[location[0]]["users"][location[1]]["day_tansactions"] < 3:
			amount = int(input('Please Enter the Deposite amount : '))
			if amount <= banks[bank_chose]["atms"][atm_chose]["per_trans_limit"]:
				if amount%100 == 0:
					if banks[location[0]]["users"][location[1]]["day_withdrawl"]+amount <= 50000:
						banks[location[0]]["users"][location[1]]["Balance"] += amount
						banks[location[0]]["users"][location[1]]["day_deposite"] += amount
						print(f"You have sucessfully Deposite {amount} rupees")
						print(f"Available Balance : ", banks[location[0]]["users"][location[1]]["Balance"],"\n")
						banks[location[0]]["users"][location[1]]["day_tansactions"] += 1
						banks[bank_chose]["atms"][atm_chose]["balance"] += amount
					else:
						print("Transaction Failed !")
						print("You are not allow to Deposite more then 50000 per day !\n")
				else:
					print("Transaction Failed !")
					print("Your transaction amount should be in multiple of 100\n")
			else:
				print("transaction Failed !")
				print("Your transaction should be less then {} for {} ATM\n".format(banks[bank_chose]["atms"][atm_chose]["per_trans_limit"],atm_chose))
		else:
			print("Transaction Failed !")
			print("You have reached to limit of 3 transaction per day !\n")

	# Check Balance
	elif transction=='4':
		print("Your Account Balance : {}\n".format(banks[location[0]]["users"][location[1]]["Balance"]))


	# Change Pin
	elif transction=='5':
		if bank_chose == banks[location[0]]["users"][location[1]]["Bank"]:
			old_pin = input("Enter Your old pin")
			if old_pin == banks[location[0]]["users"][location[1]]["pin"]:
				banks[location[0]]["users"][location[1]]["pin"] = input("Enter Your New 4 Digit Pin: ")
				print("Your PIN has been chnaged Sucessfully")
				print("New pin : ", banks[location[0]]["users"][location[1]]["pin"],"\n")
			else:
				print("Invalid pin\n")
		else:
			print("Change your pin with your Bank's ATM\n")

	else:
		print("Invalid Input !\n")


# Admin Validation Funtion
def Admin_validation(banks):
	admin_id = input("Please Enter your Admin_ID: ")
	location = [i for i in banks if banks[i]["admin"]["admin_id"] == admin_id]
	if location == []:
		print("Invalid id\n")
		return False,None
	else:
		admin_password = input("Please Enter your password: ")
		if banks[location[0]]["admin"]["password"] == admin_password:
			return True,location[0]
		else:
			print("Invalid password\n")
			return False,None


#Insert, Update, Delete Users
def in_up_de_users(location,banks):
	print("Select Your Activity : ")
	print("1. Insert User")
	print("2. Update User Details")
	print("3. Delete User\n")

	admin_Activity = input("Enter Your choice Between [1-3]: ")

	print(f"\nWelcome to the Admin System of {location} bank\n")

	if admin_Activity == '1':
		print("Enter User Details : ")

		# For Taking Unique User_id
		while True:
			user_id = "u"+str(random.randint(10,10000))
			if user_id not in banks[location]["users"].keys():
				break
				
		account_no = str(random.randint(1000,9999))+str(random.randint(1000,9999))+str(random.randint(0,9))
		name = input("Enter User Name")
		Bank = location
		Balance = int(input("Enter Initial Balance : "))
		card_lst = [banks[location]["users"][i]["card_no"] for i in banks[location]["users"]]
		print(card_lst)
		while True:
			card_no = str(random.randint(1000,9999))+"-"+str(random.randint(1000,9999))+"-"+str(random.randint(1000,9999))
			if card_no not in card_lst:
				break
		M_number = input("Enter Your User's MObile Number")
		pin = str(random.randint(1000,9999))
		day_transaction = 0
		day_withdrawl = 0
		day_deposite = 0

		banks[location]["users"][user_id] = {"account_no":account_no,"name":name,"Bank":Bank,"Balance":Balance,"card_no":card_no,"mobile_no":M_number,"pin":pin,"day_tansactions":day_transaction,"day_withdrawl":day_withdrawl,"day_deposite":day_deposite}
		print(f"User Added sucessfully in bank : {location}\n")
		print(banks[location]["users"][user_id])


	elif admin_Activity == '2':
		user_id = input("Enter the user id whose detail you want to update : ")
		if user_id in banks[location]["users"].keys():
			print("Which Information of user Do you want to Update ? ")
			print("1. Name")
			print("2. Mobile Number\n")

			choice = input("ente your choice Between [1-2]")

			if choice == '1':
				new_name = input("Enter the New Name : ")
				old_name = banks[location]["users"][user_id]["name"]
				banks[location]["users"][user_id]["name"] = new_name
				print("Name Is Updated Sucessfully : {}  --->>> {}\n".format(old_name, banks[location]["users"][user_id]["name"]))

			elif choice == '2':
				new_n = input("Enter the New mobile_no : ")
				old_n = banks[location]["users"][user_id]["mobile_no"]
				banks[location]["users"][user_id]["mobile_no"] = new_n
				print("Name Is Updated Sucessfully : {}  --->>> {}\n".format(old_n, banks[location]["users"][user_id]["mobile_no"]))
			else:
				print("Invalid Input\n")
		else:
			print("Invalid User ID\n")

	elif admin_Activity == '3':

		print("List of user_ids of Bank: ")
		j = 1
		for i in banks[location]["users"]:
			print(f"{j}. {i}")
			j+=1

		user_id = input("Enter the user id Whose profile you want to Delete : ")
		if user_id in banks[location]["users"].keys():
			if banks[location]["users"][user_id]['Balance'] == 0:
				deleted_user = banks[location]["users"][user_id]
				del banks[location]["users"][user_id]
				print(f"User Profile of {user_id} is Sucessfully deleted\n")
				# print(banks[location]["users"])
			else:
				print("Before Deleting User Account Balance Of User should be 0.")
		else:
			print("The user of this user_id not exist!\n")

	else:
		print("Please Select valid option between [1-3]\n")



#Insert, Update, Delete ATMS
def in_up_de_atms(location,banks):
	print("Select Your Activity : ")
	print("1. Insert ATM")
	print("2. Update ATM Details")
	print("3. Delete ATM")

	admin_Activity = input("Enter Your choice Between [1-3]: ")

	print(f"\nWelcome to the Admin System of {location} bank\n")

	if admin_Activity == '1':
		print("Enter ATM Details : ")

		# For Taking Uninque name of ATM
		while True:
			Atm_name = input("Please Enter ATM Name : ")
			if Atm_name in banks[location]["atms"].keys():
				print("ATM Already Exist !")
			else:
				break
		Atm_balance = int(input("Please Enter ATM Balance"))
		Atm_pincode = input("PLease Enter The pincode")
		per_trans_limit = int(input("Please Enter Limit for Per User Transaction  ex. 20000,30000..."))

		banks[location]["atms"][Atm_name] = {"balance":Atm_balance,"Pin-code":Atm_pincode,"per_trans_limit":per_trans_limit}
		print(f"User Added sucessfully in bank : {location}\n")
		# print(banks[location]["atms"])


	elif admin_Activity == '2':
		print("Which ATM Details You Want TO Update ? ")
		atm_l = list(banks[location]["atms"].keys())
		k=1
		for k1 in atm_l:
			print(f"{k}. {k1}")
			k+=1
		atm_choice = int(input(f'Enter your choice [1-{k-1}]: '))

		if atm_choice>0 and atm_choice<k:
			print("Which Detail You want to update ? ")
			print("1. ATM's Pin-code")
			print("2. ATM's Per Transaction Limit")
			print("3. ATM's Name")

			choice = input("Enter Your Choice between [1-3] : ")
			if choice == "1":
				new_pincode = input("Please Enter a new pincode : ")
				old_pincode = banks[location]["atms"][atm_l[atm_choice-1]]["Pin-code"]
				banks[location]["atms"][atm_l[atm_choice-1]]["Pin-code"] = new_pincode

				print("Sucessfully chnaged the Pin-code of ATM : {} .... {} -> {}\n".format(atm_l[atm_choice-1],old_pincode, banks[location]["atms"][atm_l[atm_choice-1]]["Pin-code"]))
			elif choice == "2":
				new_limit = input("Please Enter a new per transction limit for user transaction : ")
				old_limit = banks[location]["atms"][atm_l[atm_choice-1]]["per_trans_limit"]
				banks[location]["atms"][atm_l[atm_choice-1]]["per_trans_limit"] = new_limit

				print("Sucessfully chnaged the per transaction limit of ATM : {} .... {} -> {}\n".format(atm_l[atm_choice-1],old_limit, banks[location]["atms"][atm_l[atm_choice-1]]["per_trans_limit"]))

			elif choice == "3":
				while True:
					new_atm_name = input("Please Enter a new Name for ATM : ")
					if new_atm_name in banks[location]["atms"]:
						print("This Atm Already Exists")
					else:
						break
				old_atm_name = atm_l[atm_choice-1]
				banks[location]["atms"][new_atm_name] = banks[location]["atms"].pop(old_atm_name)
				print(f"Atm Name Sucessfully changed :  {old_atm_name} -->> {new_atm_name}")
				# print(banks[location]["atms"])

			else:
				print("Please enter valid choice Between[1-2] !\n")	
		else:
			print(f"Please enter valid choice Between[1-{k-1}]\n")

	elif admin_Activity == '3':
		print("Which ATM You Want To Delete ? ")
		atm_l = list(banks[location]["atms"].keys())
		k=1
		for k1 in atm_l:
			print(f"{k}. {k1}")
			k+=1
		atm_choice = int(input(f'Enter your choice [1-{k-1}]: '))

		if atm_choice>0 and atm_choice<k:
			del banks[location]["atms"][atm_l[atm_choice-1]]

			print("Sucessfully Deleted the ATM : {}\n".format(atm_l[atm_choice-1]))

			# print(banks[location]["atms"],"\n")
		else:
			print(f"Please enter valid choice Between[1-{k-1}]\n")

	else:
		print(" Please Select valid option between [1-3]\n")





#Insert, Update, Delete Banks
def in_up_de_bank(banks,admin_Activity):
	if admin_Activity == '1':
		while True:
			Bank_name = input("Enter The Bank Name : ")
			if Bank_name not in banks.keys():
				break
			else:
				print("This Name of Bank Already Exist PLease Enter Other Bank_Name")
		banks[Bank_name] = {}
		# Add User DICT
		banks[Bank_name]["users"] = {}
		No_of_users = int(input("Please Enter The number of users : "))
		NU = 0
		while NU<No_of_users:

			print(f"Enter Details For User-{NU+1} : ")

			while True:
				user_id = "u"+str(random.randint(10,10000))
				if user_id not in banks[Bank_name]["users"].keys():
					break

			exist_account_no = []
			exist_card_no = []
			for i in banks:
				for j in banks[i]['users']:
					exist_account_no += [banks[i]['users'][j]['account_no']]
					exist_card_no += [banks[i]['users'][j]['card_no']]
			
			#Generate Unique Account_NO
			while True:
				account_no = str(random.randint(1000,9999))+str(random.randint(1000,9999))+str(random.randint(0,9))
				if account_no not in exist_account_no:
					break

			# Generate Unique Card_no
			while True:
				card_no = str(random.randint(1000,9999))+"-"+str(random.randint(1000,9999))+"-"+str(random.randint(1000,9999))
				if card_no not in exist_card_no:
					break

			name = input("Enter User Name : ")
			Bank = Bank_name
			Balance = int(input("Enter Initial Balance : "))
			m_number = input("Enter User's Mobile Number : ")
			pin = str(random.randint(1000,9999))
			day_transaction = 0
			day_withdrawl = 0
			day_deposite = 0

			banks[Bank_name]["users"][user_id] = {"account_no":account_no,"name":name,"Bank":Bank,"Balance":Balance,"card_no":card_no,"mobile_no":m_number,"pin":pin,"day_tansactions":day_transaction,"day_withdrawl":day_withdrawl,"day_deposite":day_deposite}
			print(f"User Added sucessfully in bank : {Bank_name}\n")
			NU+=1
		
		# Add ATM DICT
		banks[Bank_name]["atms"] = {}
		No_of_atms = int(input("Please Enter The number of atms of New Bank: "))
		i = 0
		while i<No_of_atms:
			print(f"Enter ATM Details For ATM-{i+1}: ")

			# For Taking Uninque name of ATM
			while True:
				Atm_name = input("Please Enter ATM Name : ")
				if Atm_name in banks[Bank_name]["atms"].keys():
					print("ATM Already Exist !")
				else:
					break
			Atm_balance = int(input("Please Enter ATM Balance : "))
			Atm_pincode = input("PLease Enter The pincode : ")
			per_trans_limit = int(input("Please Enter Limit for Per User Transaction  ex. 20000,30000...  : "))

			banks[Bank_name]["atms"][Atm_name] = {"balance":Atm_balance,"Pin-code":Atm_pincode,"per_trans_limit":per_trans_limit}
			print(f"User Added sucessfully in bank : {Bank_name}\n")
			i+=1


		# Add Admin Dict
		banks[Bank_name]["admin"] = {}
		Admin_name = input("Enter The Admin Name : ")
		# Admin_id   = input("Enter the Admin ID : ")
		Admin_id   = str(random.randint(1000,9999))
		# admin_password = input("Enter the Admin password : ")
		admin_password = str(random.randint(1000,9999))

		banks[Bank_name]["admin"] = {"name":Admin_name,"admin_id":Admin_id,"password":admin_password}


		# Add Slogan For Bank
		banks[Bank_name]["slogan"] = input("Enter The Slogan For Your Bank : ")


		print("\nBank",Bank_name,"Sucessfully inserted in database\n")
		print(f"{Bank_name} : ",banks[Bank_name])

		

	elif admin_Activity == '2':
		flag,location = Admin_validation(banks)
		if flag:
			while True:
				print(f"Welcome to the Admin System of {location} bank\n")
				print("Which Information You Want to Update ? ")
				print("1. Name Of the Bank")
				print("2. Change Slogan Of Your Bank")

				choice = input("Enter Your choice Between [1-2]: ")

				if choice == "2":
					new_slogan = input("please Enter the New Slogan For your Bank")
					old_slogan = banks[location]["slogan"]
					banks[location]["slogan"] = new_slogan
					print("Slogan has been changed sucessfully : {}  -->>  {}\n".format(old_slogan,banks[location]["slogan"]))
					break

				elif choice == "1":
					while True:
						new_bank_name = input("Please Enter a new Name for Bank : ")
						if new_bank_name in banks.keys():
							print("This Bank Already Exist")
						else:
							break
					old_bank_name = location
					banks[new_bank_name] = banks.pop(old_bank_name)
					print(f"Atm Name Sucessfully changed :  {old_bank_name} -->> {new_bank_name}\n")
					location = new_bank_name
					for i in banks[location]['users']:
						banks[location]['users'][i]['Bank'] = location
					# print("\n",banks.keys(),"\n")
					# print("\n",banks[location],"\n")
					break

				else:
					print("Invalid Input !\n")

	elif admin_Activity == '3':
		print("Which Bank You Want To Delete ? ")
		bank_l = list(banks.keys())
		k=1
		for k1 in bank_l:
			print(f"{k}. {k1}")
			k+=1
		bank_choice = int(input(f'Enter your choice [1-{k-1}]: '))
		location = bank_l[bank_choice-1]

		if bank_choice>0 and bank_choice<k:
			while True:
				print("Do You Want to delete {} Bank ??".format(location))
				print("1. Yes")
				print("2. No\n")

				choice = input("Enter Your choice Between [1-2]: ")

				if choice == "1":
					if banks[location]['users'] == {}:						
						del banks[location]
						print(f"{location} Bank Has Been Deleted Sucessfully\n")
						# print(banks.keys())
						break
					else:
						print("\nYou should Delete All Users First !\n")
						break

				elif choice == "2":
					print("Deleting Activity Terminated !\n")
					break
				else:
					print("Invalid Input !\n")
		else:
			print(f"Please enter valid choice Between[1-{k-1}]\n")

	else:
		print(" Please Select valid option between [1-3]\n")




# Add Money to ATM Function
def add_money_atm(banks, bank_chose, atm_chose):
	print(f"Welcome to {bank_chose} Atm")
	admin_id = input("Please Enter your Admin_ID: ")
	if banks[bank_chose]["admin"]["admin_id"] == admin_id:
		admin_password = input("Please Enter your password: ")
		if banks[bank_chose]["admin"]["password"] == admin_password:
			deposite_amount = int(input("Please enter the amount that you want to deposit : "))
			banks[bank_chose]["atms"][atm_chose]["balance"] += deposite_amount
			print("You have sucessfully Deposite {deposite_amount} rupees")
			print("Thank You for your visit")
			print("Now, Available Balance of {} is : {}\n".format(atm_chose,banks[bank_chose]["atms"][atm_chose]["balance"]))
		else:
			print("Invalid password !\n")
	else:
		print("Invalid Id\n")





# Main Body
while True:	
	print("Banking System Interface : ")
	print("Please select your purpose : \n")
	print("1. Visit ATM (User Functionality )")
	print("2. Insert, Update, Delete Users")
	print("3. Insert, Update, Delete ATMS")
	print("4. Insert, Update, Delete Banks")
	print("5. Insert Money into ATM")
	print("6. Day End(EXIT) \n")
	
	Purpose_choice = int(input('Enter your choice [1-6]: '))

	if Purpose_choice>0 and Purpose_choice<6:

		# Visit ATM (User Features)
		if Purpose_choice == 1:
			while True:
				bank_l = list(banks.keys())
				print("Please select Bank Of ATM : ")
				j=1
				for i in bank_l:
					print(f"{j}. {i}")
					j+=1
				print(f"{j}. Exit From ATM Options\n")

				bank_choice = int(input(f'Enter your choice [1-{j-1}]: '))
				if bank_choice>0 and bank_choice<j:
					while True:
						back = 0
						atm_l = list(banks[bank_l[bank_choice-1]]["atms"].keys())
						print("Please select Atm that you want to visit: ")
						k=1
						for k1 in atm_l:
							print(f"{k}. {k1}")
							k+=1
						print(f"{k}. Go Back to Select Other Bank\n")

						atm_choice = int(input(f'Enter your choice [1-{k-1}]: '))

						if atm_choice>0 and atm_choice<k:
							while True:
								user_validation(banks,bank_l[bank_choice-1],atm_l[atm_choice-1])
								print("Do You want to do any other Transaction ? ")
								print("1. Yes")
								print("2. No")
								choice = int(input("Enter Your Choice : "))
								if choice == 1:
									continue
								elif choice == 2:
									back = 1
									break
							if back == 1:
								break	
						elif atm_choice == k:
							break
						else:
							print(f"Please enter valid choice Between[1-{k}]\n")
				elif bank_choice==j:
					break
				else:
					print(f"Please select a valid bank Option Between[1 - {j-1}]!\n")


		# Insert, Update, Delete USers (Admin Feature)
		# Working : Firstly Enter Admin details If admin detail is valid and This admin is of HDFC Bank Then that admin can Only Access AND UPDATE Details of HDFC Bank.
		elif Purpose_choice == 2:
			flag,location = Admin_validation(banks)
			if flag:
				in_up_de_users(location,banks)


		# Insert, Update, Delete ATMs (Admin Feature)
		# Working : Firstly Enter Admin details If admin detail is valid and This admin is of HDFC Bank Then that admin can Only Access AND UPDATE Details of HDFC Bank.
		elif Purpose_choice == 3:
			flag,location = Admin_validation(banks)
			if flag:
				in_up_de_atms(location,banks)


		# Insert, Update, Delete Banks (Admin Feature)
		# Working : Firstly Enter Admin details If admin detail is valid and This admin is of HDFC Bank Then that admin can Only Access AND UPDATE Details of HDFC Bank .
		# For Inserting Bank There Will Be no Role Of Admin
		elif Purpose_choice == 4:
			print("Select Your Activity : ")
			print("1. Insert Bank")
			print("2. Update Bank")
			print("3. Delete Bank\n")

			admin_Activity = input("Enter Your choice Between [1-3]: ")
			in_up_de_bank(banks,admin_Activity)


		# ADD Money Into ATM (Admin Feature)
		# Working : Firstly Enter Admin details If admin detail is valid and This admin is of HDFC Bank Then that admin can Only Access AND UPDATE Details of HDFC Bank.s
		elif Purpose_choice == 5:
			# Only admin Can add money into atm of same bank
			while True:
				flag = 0
				bank_l = list(banks.keys())
				print("Please select Your Bank : ")
				j=1
				for i in bank_l:
					print(f"{j}. {i}")
					j+=1
				print(f"{j}. Exit From this section !\n")

				bank_choice = int(input(f'Enter your choice [1-{j-1}]: '))
				if bank_choice>0 and bank_choice<j:
					while True:
						atm_l = list(banks[bank_l[bank_choice-1]]["atms"].keys())
						print("Please select Atm that you want to visit: ")
						k=1
						for k1 in atm_l:
							print(f"{k}. {k1}")
							k+=1
						print(f"{k}. Go Back to Select Other Bank\n")

						atm_choice = int(input(f'Enter your choice between [1-{k-1}]: '))

						if atm_choice>0 and atm_choice<k:
							add_money_atm(banks,bank_l[bank_choice-1],atm_l[atm_choice-1])
							flag=1
							break
						elif atm_choice == k:
							break
						else:
							print(f"Please enter valid choice Between[1-{k}]\n")
				elif bank_choice==j:
					break
				else:
					print(f"Please select a valid bank Option Between[1 - {j-1}] !\n")
				
				if flag==1:
					break
			
	elif Purpose_choice == 6:
		break

	else:
		print("Please Select a valid Option Between[1-6] !\n")