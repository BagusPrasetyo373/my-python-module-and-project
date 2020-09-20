import re #regular expression

def is_int(x):
	if isinstance(x, int): return True
	else: return False

def is_float(x):
	if isinstance(x, float): return True
	else: return False

def is_str(x):
	if isinstance(x, str): return True
	else: return False

#regex is so useful for these type of checking
def is_valid_email(email, type): 
	if is_str(email) == True and is_str(type):
		if re.search(fr"^[a-zA-Z0-9]*[@]+[{type}]+[.]+[com]$",email): return True
		else: return False
	else: return False
