name=str(input("Give the name:"))

def luke(name):
	solutions = {'Leia':'sister',
	'Darth Vader':'father',
	'Han':'brother in law',
	'R2D2':'droid'}
	return 'Luke, I am your {}.'.format(solutions[name])

idk=luke(name)
print(idk)