def marks(tamil,english,maths,science,social):
  avg = tamil + english + maths + science + social
  print("Your Total Mark is:",avg)
  per=avg/5
  if(per>=90):
    print("You Secure A Grade, V.Good")
  elif(per>=80):
    print("You Secure B Grade, Good")
  elif(per>=70):
    print("You Secure C Grade, Not Bad")
  elif(per>=60):
    print("You Secure D Grade, Try to improve")
  elif(per>=40):
    print("You Secure E Grade, Try to make hardwok")
  else:
    print("You Secure F Grade, make try to get pass mark ")
  
marks(tamil=60,english=88,science=42,social=33,maths=98)

#Output:
Your Total Mark is: 321
You Secure D Grade, Try to improve
