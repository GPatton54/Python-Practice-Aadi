num1=int(input("First number: "))
num2=int(input("Second number: "))

def opr(num1, num2):
	if num1 + num2 == 24:
		return 'added'
	elif num1 - num2 == 24 or num2 - num1 == 24:
		return "subtracted"
	elif num1 / num2 == 24 or num2 / num1 == 24:
		return 'divided'
	elif num1 * num2 == 24:
		return 'multiplied'
	else:
		return None

idk=opr(num1, num2)

print(idk)