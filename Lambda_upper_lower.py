upper=lambda x:x.upper()
lower=lambda x:x.lower()

def UrL(uplo,x):
  print(uplo(x))

#Output:
UrL(upper,"Hello")

HELLO

UrL(lower,"HeLlO")

hello
