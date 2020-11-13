h=int(input("Height:"))
r=int(input("Radius:"))
import math
def cone(h, r):
	return round((1/3)*math.pi*(r**2)*h,2)
idk=cone(h, r)
print(idk)