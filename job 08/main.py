def meteo (type , saison) :
        if type == 'fruits' and saison == 'hiver':
          return ("orange, mandarine et kiwi")
        elif type == 'fruits' and saison == 'été':
          return ("Poire, fraise, cassis")
        elif  type == 'légume' and saison == 'hiver':
          return ("carotte, topinambour, endive")
        elif type == 'légume' and saison == 'été':
          return ("artichaut, aubergine,navet")
    
    

print (meteo ('fruits' , 'hiver'))
    