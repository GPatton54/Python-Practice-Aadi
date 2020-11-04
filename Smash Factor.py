bs=int(input("What is the ball speed: "))
cs=int(input("What is the club speed: "))

def sf(bs, cs):
	return round(bs/cs, 2)

idk=sf(bs, cs)

print(idk)