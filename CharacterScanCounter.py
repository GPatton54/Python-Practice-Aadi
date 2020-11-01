sen=str(input("Give a sentence: "))
char=str(input("What character are you scanning for, in lowercase: "))

idk = sen.lower()

def numds(sen, char):
  return idk.count(char)

ds = numds(idk, char)

print(ds)