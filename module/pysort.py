def intlist(list):
	list_out = []
	for i in range(-1,(max(list))):
		i += 1
		if i in list:
			list_out.append(i)
	return list_out
