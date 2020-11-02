lst = [None, 2, 8, 8]

def finone(lst):
	if None in lst:
		return lst.index(None)
	else:
		return -1

idk=finone(lst)

print(idk)