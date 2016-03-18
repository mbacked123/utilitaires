# -*- coding: utf-8 -*-
def LongestWord(sen): 
  """une fonction retournant le plus long mot dans une phrase"""

  
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


  def FirstFactorial(num): 
    """Fonction calculant le factoriel d'un nombre données"""


  if num == 0 or num == 1:
    return 1
  else:
    num = num * FirstFactorial(num-1)    
  return num    


def LetterChanges(str): 
  """fonction changeant chaque lettre par sa suivante en mettant les voyelles en majuscule"""

 
  alphabet = ['a','b','c','d','e','f','g','h','i','j','i','k','l',
              'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
  vowel = ['a','e','i','o','u']
  chaine = ""
  for i in str:
    if i in alphabet:
      ind = alphabet.index(i)
      if ind == (len(alphabet) -1):
        chaine += alphabet[0].upper()
      else:
        if alphabet[ind + 1] in vowel:
          chaine += alphabet[ind + 1].upper()
        else:
          chaine += alphabet[ind + 1]
    else:
      chaine += i
     
    str = chaine
    
  return str    