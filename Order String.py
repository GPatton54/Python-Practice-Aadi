txt=str(input("Text:"))

def order(txt):
	return list(txt) == sorted(txt)
idk=order(txt)
print(idk)