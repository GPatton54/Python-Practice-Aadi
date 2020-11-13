txt=str(input("Bruh momento numero uno: Give me a string:"))
def xo(txt):
  txt = txt.lower()
  return txt.count("x") == txt.count("o")
idk=xo(txt)
print(idk)