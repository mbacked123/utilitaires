def LongestWord(sen): 

  # code goes here 
  # Note: don't forget to properly indent in Python
  def operation_taille(val):
    taille = len(val)
    for c in val:
      if not c.isalnum():
        taille -= 1
    return taille
  
  dico = ""
  list_mot = sen.split(" ")
  maxi = operation_taille(list_mot[0])
  for value in list_mot[1:]:
    taille = operation_taille(value)
    if taille > maxi:
      maxi = taille
      dico = value
  
  return dico, maxi 