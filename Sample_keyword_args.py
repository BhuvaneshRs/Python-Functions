def data(id,name,number,**all):
  """Keyword argument will be show in Dict""" 
  print("Id=",id)
  print("Name=",name)
  print("Number=",number)
  print("Other Details=",all)

data(id=12,name="Bhuvanesh",number=8610073184,a=1,b=2,c=3)

#Output:
Id= 12
Name= Bhuvanesh
Number= 8610073184
Other Details= {'a': 1, 'b': 2, 'c': 3}
