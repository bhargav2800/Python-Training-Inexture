import psycopg2
import config

def execute_query(statement,parameters,type):

	conn = psycopg2.connect(
		host = config.hostname,
		dbname = config.database,
		user = config.username,
		password = config.pwd,
		port = config.port_id)

	cur = conn.cursor()
	temp = None
	if type == 'returned':
		cur.execute(statement,parameters)
		temp = list(cur)
	else:
		cur.execute(statement,parameters)
	
	conn.commit()

	cur.close()
	conn.close()
	return temp