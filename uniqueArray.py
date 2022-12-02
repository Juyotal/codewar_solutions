def isUnique(list):
	a = []
	for i in list:
		if i in a:
			print(i)
			return False
		else:
			a.append(i)
	return True