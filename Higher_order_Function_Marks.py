def PrF(tamil,english,maths,science,social):
  total=tamil+english+maths+science+social
  print("Your Total Mark is",total)
  fail=0
  if tamil<40:
    print("Tamil Subject is Fail")
    fail+=1
  if english<40:
    print("English Subject is Fail")
    fail+=1
  if maths<40:
    print("Maths subject is Fail")
    fail+=1
  if science<40:
    print("Science subject is Fail")
    fail+=1
  if social<40:
    print("Social Subjet is fail")
    fail+=1
  per=total/5
  if fail==0:
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
    print("You are not eligible to Grade, because you fail in",fail,"Subjects")

def display(tamil,english,maths,science,social):
  print("Tamil=",tamil)
  print("English=",english)
  print("Maths=",maths)
  print("Science=",science)
  print("Social=",social)

def show(mode,tamil,english,maths,science,social):
  mode(tamil,english,maths,science,social)


#Output:(1)
show(PrF,60,40,20,10,70)

Your Total Mark is 200
Maths subject is Fail
Science subject is Fail
You are not eligible to Grade, because you fail in 2 Subjects

#Output:(2)
show(display,60,40,20,10,70)

Tamil= 60
English= 40
Maths= 20
Science= 10
Social= 70
