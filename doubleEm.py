def doubleEm(entered_text):
  pile=""
  for i in entered_text:
    if i.lower() in "aeiou":
      pile=pile+i+i
    if not i.lower() in "aeiou":
      pile=pile+ "N"