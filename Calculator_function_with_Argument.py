def Calculator(A,B,C):
  if(C=="+"):
    print(A+B)
  elif (C=="-"):  
    print(A-B)
  elif (C=="*"):  
    print(A*B)
  elif (C=="/"):
    print(A/B)
  else:  
    print("enter valid option")

Calculator(2,2,"*")

#Output:
4


Calculator(6,7,"+")

#Output:
13
