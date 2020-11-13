strng=str(input("Bruh momento numero dos: Give a string:"))

def vowels(strng):
   vowels = ['a','e','i','o','u']
   total = 0
   for s in strng:
      if s in vowels:
         total += 1
   return total

idk=vowels(strng)
print(idk)