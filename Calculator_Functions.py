def Calculator():
  A=int(input("Enter A value: "))
  B=int(input("Enter B value: "))
  C=int(input("1.add 2.sub 3.mul 4.div: "))
  if(C==1):
    print(A+B)
  elif (C==2):  
    print(A-B)
  elif (C==3):  
    print(A*B)
  elif (C==4):
    print(A/B)
  else:  
    print("enter valid option")

Calculator()

#Output:(1)
Enter A value: 1
Enter B value: 4
1.add 2.sub 3.mul 4.div: 4
0.25

#Output:(2)
Enter A value: 5
Enter B value: 5
1.add 2.sub 3.mul 4.div: 3
25
