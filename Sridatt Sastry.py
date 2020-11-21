n = int(input("Number:"))

def sastry(n):
    return int(str(n)+str(n+1))**.5%1==0

idk = sastry(n)
print(idk)