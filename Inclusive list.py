num1=int(input("Starting number:"))
num2=int(input("Ending number:"))
def inclist(num1, num2):
	return list(range(num1, num2+1)) or [num1]

idk=inclist(num1, num2)
print(idk)