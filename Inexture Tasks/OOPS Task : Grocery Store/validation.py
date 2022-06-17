import re

def validate_user_name(value):
	regex = r'^[a-z0-9_-]{5,15}$'
	if re.match(regex, value):
		return True
	return False
	
def validate_string(value):
	regex = r'^[a-zA-Z]+$'
	if re.match(regex, value):
		return True
	return False
	
def validate_int(value):
	regex = r'^[0-9]+$'
	if re.match(regex, value):
		return True
	return False
	
def validate_email(email):
	email_regex = r'^[a-zA-Z0-9._]{3,10}@[a-zA-Z0-9_]{1,10}\.[a-zA-Z]{2,10}$'
	if re.match(email_regex, email):
		return True
	return False
	
def validate_password(password):
	pw_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{4,14}$'
	if re.match(pw_regex, password):
		return True
	return False


def validate_address(value):
	#regex = r'^[a-zA-Z]+$'
	regex = r"^(?=.*[0-9])(?=.*[a-z|A-Z])[a-zA-Z0-9 ]*$"
	if re.match(regex, value):
		return True
	return False

def validate_name(value):
	regex = r'^[a-zA-Z]{3,7}$'
	if re.match(regex, value):
		return True
	return False

def validate_empty(value):
	if len(value)!=0:
		return True
	return False
	
def product_integer(value):
	regex = r'[1-9][0-9]*'
	if re.match(regex, value):
		return True
	return False

