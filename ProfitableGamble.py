prob = int(input("What is the probability: "))
prize = int(input("What is the prize: "))
pay = int(input("What is the pay: "))

result = prob * prize - pay

if result > 0:
	print("True")
else:
	print("False")