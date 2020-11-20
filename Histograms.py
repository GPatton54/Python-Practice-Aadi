lst = []
num = int(input("Enter the list size : "))

for i in range(0, num):
    print("Enter number at location", i, ":")
    idk = int(input())
    lst.append(idk)

char = str(input("Pick your character:"))


def histogram(lst, char):
    return "\n".join(char * i for i in lst)

bruh = histogram(lst, char)
print(bruh)
