from math import sqrt

def nearest_pronic(n):
  i = int(sqrt(n))
  return i * (i+1)


n = float(input('give me a number'))
np = nearest_pronic(n)
if n == np:
  print(f"{n} is a pronic number")
else:
  print("non pronic")


