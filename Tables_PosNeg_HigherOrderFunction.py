def tables(x):
  for i in range(1,11):
    print(i,"*",x,"=",i*x)

def PosNeg(x):
  if(x>0):
    print("Given value is positive")
  else:
    print("Given Value is Negative")

def mode(arm,x):
  arm(x)

  
#Output:(1)
mode(tables,5)
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50

#Output:(2)
mode(PosNeg(2))
Given value is positive
