lst = []
num = int(input("Enter the list size : "))

for i in range(0, num):
    print("Enter number at location", i, ":")
    idk = int(input())
    lst.append(idk)

def programmers(lst):
	return(max(lst)-min(lst))

idk=programmers(lst)

print(idk)