lst = []
num = int(input("Enter the list size : "))

for i in range(0, num):
    print("Enter number at location", i, ":")
    idk = int(input())
    lst.append(idk)

    def multiply(lst):
        return [[i]*len(lst) for i in lst]
    
    bruh = multiply(lst)
    print(bruh)