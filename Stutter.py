word=str(input("Word:"))

def stutter(word):
	return (2*(word[:2]+'... '))+word+'?'

idk=stutter(word)

print(idk)