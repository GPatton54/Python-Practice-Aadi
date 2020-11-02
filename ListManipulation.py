lst = [1, 2, 3, 8]

def incr(lst):
	for i in range(len(lst)):
		lst[i] += 1
	return lst

idk=incr(lst)

print(idk)