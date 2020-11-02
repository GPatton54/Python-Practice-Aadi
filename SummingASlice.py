lst = [1, 4, 8, 6]
n = int(input("Type a number: "))


def sumofthething(lst, n):
	return sum(lst[:n])

idk = sumofthething(lst, n)

print(idk)