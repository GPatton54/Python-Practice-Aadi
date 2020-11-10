num=int(input("Provide a number: "))
def factorial(num):
	return 1 if num < 2 else num * factorial(num - 1)

idk=factorial(num)
print(idk)