def credential_check_query(id,password,table_name):
	return f"SELECT case when ({id} = %s and {password} = %s) THEN True ELSE False END AS temp from {table_name};"

def fetch_uid(id,password,table_name):
	return f"SELECT user_id FROM {table_name} WHERE {id} = %s and {password} = %s"

def insert_query(par1,par2,par3,par4,par5,par6,par7,par8):
	return f"INSERT INTO questions({par1},{par2},{par3},{par4},{par5},{par6},{par7},{par8}) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

# def insert_query_1(table_name,par1,par2,par3,par4,par5,par6,par7,par8,par9,par10,par11,par12):
# 	return f"INSERT INTO {table_name}({par1},{par2},{par3},{par4},{par5},{par6},{par7},{par8},{par9},{par10},{par11},{par12}) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING user_id;"

def insert_query_2(table_name,par1,par2,par3,par4):
	return f"INSERT INTO {table_name}({par1},{par2},{par3},{par4}) VALUES(%s,%s,%s,%s)"

def insert_query_3(table_name,par1,par2):
	return f"INSERT INTO {table_name}({par1},{par2}) VALUES(%s,%s)"

def register_comapny_query(c_name,web_site,official_mail,admin_id,admin_pass):
	return f"INSERT INTO organization({c_name},{web_site},{official_mail},{admin_id},{admin_pass}) VALUES (%s,%s,%s,%s,%s) RETURNING c_id,q_set;"

def select_query(par1,table_name,par2,admin_id):
	return f"SELECT {par1} FROM {table_name} WHERE {par2} = {admin_id}"

def select_query_1(par1,par2,par3,par4,par5,par6,par7,table_name,con1,val1):
	return f"SELECT {par1},{par2},{par3},{par4},{par5},{par6},{par7} FROM {table_name} WHERE {con1}={val1}"

def select_query_2(par1,par2,table_name):
	return f"SELECT {par1},{par2} from {table_name}"

def select_query_3(par1,par2,par3,table_name):
	return f"SELECT {par1},{par2},{par3} from {table_name}"

def update_query(table_name,par1,par2):
	return f"UPDATE {table_name} SET {par1}=%s where {par2}=%s"

def update_query_1(table_name,par1,par2,par3):
	return f"UPDATE {table_name} SET {par1}=%s WHERE {par2}=%s and {par3}=%s"

def delete_query(table_name,par1,val1):
	return f"DELETE FROM {table_name} WHERE {par1} = {val1}"

def view_applicants_select_query(constraint):
	return f"SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd WHERE sd.c_id = %s and sd.user_id = cd.user_id and cd.{constraint}=%s;"

def view_applicants_select_query_2():
	return "SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd, interested_tech AS it WHERE sd.c_id = %s and sd.user_id = cd.user_id and it.user_id = sd.user_id and it.tech = %s;"

def view_applicants_select_query_3(company_id):
	return f"SELECT sd.user_id,cd.f_name,sd.marks FROM selection_details AS sd, candidate AS cd WHERE sd.c_id = {company_id} and sd.user_id = cd.user_id;"

def view_user_details_query():
	return f"SELECT cd.* FROM candidate AS cd,selection_details AS sd WHERE cd.user_id = %s and sd.user_id = %s and sd.c_id = %s"

def Apply_interview_query():
	return "SELECT DISTINCT org.c_id,org.c_name,org.web_site,org.official_mail,role.role FROM organization AS org , questions as q , hiring_role as role where q.q_set=org.q_set and org.q_set=role.q_set"

def Apply_interview_query_1():
	return "SELECT CASE WHEN (user_id=%s and c_id=%s) THEN True ELSE False END AS temp FROM selection_details;"

def View_applications_query(uid):
	return f"SELECT sd.user_id,sd.c_id,org.c_name,sd.marks,sd.selection_status,sd.next_process_info FROM organization AS org,selection_details as sd WHERE sd.user_id={uid} and org.c_id = sd.c_id"

def fetch_fields(field_name,table_name):
	return f"SELECT {field_name} FROM {table_name}"