a=int(input("Number:"))
b=int(input("Number:"))
def half(a, b):
	i=0
	while a>b:
		a = a/2
		i+=1
	return i-1
idk=half(a, b)
print(idk)