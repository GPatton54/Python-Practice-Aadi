lst = []
num = int(input("Enter the list size : "))

for i in range(0, num):
    print("Enter number at location", i, ":")
    idk = int(input())
    lst.append(idk)

def sort(lst):
  purgedlst = []
  for i in sorted(lst):
    if i not in purgedlst:
      purgedlst.append(i)
  return purgedlst
bruh=sort(lst)
print(bruh)