arg=input("Boolean:")

def rev(arg = None):
	return not arg if type(arg) == bool else "boolean expected"
idk=rev(arg = None)
print(idk)