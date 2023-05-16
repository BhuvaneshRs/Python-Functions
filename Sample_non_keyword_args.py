def data(id,name,number,*all):
  """Non Keyword argument will be show in tuple""" 
  print("Id=",id)
  print("Name=",name)
  print("Number=",number)
  print("Other Details=",all)

#Output:
data(2,"Bhuvanesh",8610073184,"All","Other","Details")

Id= 2
Name= Bhuvanesh
Number= 8610073184
Other Details= ('All', 'Other', 'Details')
