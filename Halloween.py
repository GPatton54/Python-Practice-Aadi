date=str(input("Give the date: "))

def halloween(date):
	return 'Bonfire toffee' if date.endswith('10/31') else 'toffee'

idk=halloween(date)
print(idk)