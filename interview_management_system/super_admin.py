from query import execute_query
import fetch_query

class management:
	def view_organizations(self):
		# statement = "SELECT c_id,c_name from organization"
		statement = fetch_query.select_query_2('c_id','c_name','organization')
		parameters = None
		l = execute_query(statement,parameters,'returned')
		return l


	def delete_organization(self,cid):
		# statement = f"DELETE FROM organization WHERE c_id = {cid}"
		statement = fetch_query.select_query('q_set','organization','c_id',cid)
		parameters = None
		l = execute_query(statement,parameters,'returned')
		q_set = l[0][0]

		statement = fetch_query.delete_query('questions','q_set',q_set)
		parameters = None
		l = execute_query(statement,parameters,'no_return')

		statement = fetch_query.delete_query('selection_details','c_id',cid)
		parameters = None
		l = execute_query(statement,parameters,'no_return')

		try:
			statement = fetch_query.delete_query('organization','c_id',cid)
			parameters = None
			l = execute_query(statement,parameters,'no_return')
		except Exception:
			return False
		
		return True
	
	def view_candidates(self):
		# statement = "SELECT user_id,f_name from candidate"
		statement = fetch_query.select_query_3('user_id','f_name','email','candidate')
		parameters = None
		l = execute_query(statement,parameters,'returned')
		return l

	def delete_candidates(self,uid):
		# statement = f"DELETE FROM selection_details WHERE user_id = {uid}"
		statement = fetch_query.delete_query('selection_details','user_id',uid)
		parameters = None
		l = execute_query(statement,parameters,'no_return')

		# statement = f"DELETE FROM user_queries WHERE user_id = {uid}"
		statement = fetch_query.delete_query('user_queries','user_id',uid)
		parameters = None
		l = execute_query(statement,parameters,'no_return')

		# statement = f"DELETE FROM candidate WHERE user_id = {uid}"
		statement = fetch_query.delete_query('candidate','user_id',uid)
		parameters = None
		l = execute_query(statement,parameters,'no_return')

		statement = fetch_query.delete_query('interested_tech','user_id',uid)
		parameters = None
		l = execute_query(statement,parameters,'no_return')		
		return True

