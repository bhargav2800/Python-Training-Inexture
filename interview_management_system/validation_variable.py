import re
from datetime import datetime

def is_numeric(val):
	if val.isnumeric():
		return True
	else:
		return False

def is_valid_marks(val):
	try:
		val = float(val)
		val = int(val)
		return val
							
	except Exception:
		return None

def is_alpha(val):
	if val.isalpha():
		return True
	else:
		return False

def check_email(email):

	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

	if(re.fullmatch(regex, email)):
		return True
	else:
		return False

def validate_date(date):
	try:
		date_time = datetime.strptime(date,'%Y-%m-%d %H:%M')
		return True
	except Exception:
		return False

def check_pass(password):
	regex = r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$'
	if(re.fullmatch(regex, password)):
		return True
	else:
		return False