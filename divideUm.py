def divideUm(entered_string): #pg.63
  individual=entered_string.split()
  x=0
  for i in individual:
    print individual[x]
    x=x+1 #increments x each time throught the loop
  print x