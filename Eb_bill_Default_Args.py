def eb(units=50):
  print(" Under 50 units price Rs.0.50/Units \n Under 100 units Price Rs.0.75/Units \n under 250 Units price Rs.1.20/Units \n Above 250 units price Rs.1.50/Units \n")
  if units <=50:
    print(units*0.50,"is Your bill amount")
  elif units <=100:
    print(units*0.75,"is Your bill amount")
  elif units <=250:
    print(units*1.20,"is Your bill amount")
  elif units >250:
    print(units*1.50,"is Your bill amount")

#Output:(1)
eb(300)

 Under 50 units price Rs.0.50/Units 
 Under 100 units Price Rs.0.75/Units 
 under 250 Units price Rs.1.20/Units 
 Above 250 units price Rs.1.50/Units 

450.0 is Your bill amount

#Output:(2)
eb()

 Under 50 units price Rs.0.50/Units 
 Under 100 units Price Rs.0.75/Units 
 under 250 Units price Rs.1.20/Units 
 Above 250 units price Rs.1.50/Units 

25.0 is Your bill amount
