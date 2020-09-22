def ordstr(str): #str to ord
	list_output = []
	char_list = list(str)
	char_list_len = len(char_list)
	for i in range(-1,(char_list_len-1)):
		i += 1
		char_get = char_list[i]
		char_ord = ord(char_get)
		list_output.append(char_ord)
	return list_output

def ordlist(list): #str list to ord
	str_output = []
	str_len = len(list)
	for i in range(-1,(str_len-1)):
		i += 1
		str_get = list[i]
		str_get_len = len(str_get)
		for i in range(-1,(str_get_len-1)):
			i += 1
			str_get_get = str_get[i]
			str_ord = ord(str_get_get)
			str_output.append(str_ord)
	return str_output

def binstr(str): #str to bin
	binstr_output = []
	binstr_len = len(str)
	for i in range(-1,(binstr_len-1)):
		i += 1
		binstr_get = str[i]
		binstr_ord = ord(binstr_get)
		binstr_bin = bin(binstr_ord)
		binstr_rep = binstr_bin.replace('b','')
		binstr_output.append(binstr_rep)
	return binstr_output

def binlist(list): #int list to bin
	binlist_output = []
	binlist_len = len(list)
	for i in range(-1,(binlist_len-1)):
		i += 1
		binlist_get = list[i]
		binlist_bin = bin(binlist_get)
		binlist_rep = binlist_bin.replace('b','')
		binlist_output.append(binlist_rep)
	return binlist_output

def binstrlist(list): #str list to bin
	binstrlist_output = []
	binstrlist_len = len(list)
	for i in range(-1,(binstrlist_len-1)):
		i += 1
		binstrlist_get = list[i]
		binstrlist_get_len = len(binstrlist_get)
		for i in range(-1,(binstrlist_get_len-1)):
			i += 1
			binstrlist_get_get = binstrlist_get[i] 
			binstrlist_ord = ord(binstrlist_get_get)
			binstrlist_bin = bin(binstrlist_ord)
			binstrlist_rep = binstrlist_bin.replace('b','')
			binstrlist_output.append(binstrlist_rep)
	return binstrlist_output

def chrlist(list): #int list to chr
	chrlist_output = []
	chrlist_len = len(list)
	for i in range(-1,(chrlist_len-1)):
		i += 1
		chrlist_get = list[i]
		chrlist_str = str(chrlist_get)
		chrlist_get_len = len(chrlist_str)
		for i in range(0,(chrlist_get_len-2)):
			chrlist_get_get = chrlist_str[0:chrlist_get_len]
			chrlist_int = int(chrlist_get_get)
			chrlist_chr = chr(chrlist_int)
			chrlist_output.append(chrlist_chr)
	return chrlist_output

def intmerge(list):
	x = ''
	strl = []
	for i in range(0,len(list)):
		i += 1
		strl.append(str(list[i - 1]))
		x += strl[i - 1]
	y = int(x)
	return y
