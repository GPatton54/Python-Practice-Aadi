opr=str(input("Operator: "))
num1=int(input("First number: "))
num2=int(input("Second number:"))

def solve(opr, num1, num2):
  if opr=="+":
    return num1+num2
  elif opr=="*":
    return num1*num2
  elif opr=="-":
    return num1-num2
  elif opr=="**":
    return num1**num2
  else:
    return num1/num2

solution = solve(opr, num1, num2)

print(solution)