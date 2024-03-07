def pair_impair(nombre):
  if nombre <= 0 :
   return "Le nombre doit être un entier positif."
  if nombre % 2 == 0:
     return "Pair"
  else:
     return "Impair"
 



print(pair_impair(7))   
print(pair_impair(10))  
print(pair_impair(-12))  
