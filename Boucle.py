salaire = 1500
while salaire < 2000:
    
    if salaire == 1740 :
        salaire += 130
        print ("Augmentation à 130 €")
        print ("votre salaire est de " + str(salaire) + "€")
        salaire += 120
        continue
    
    else:
        print ("votre salaire est de " + str(salaire) + "€")
        salaire += 120

