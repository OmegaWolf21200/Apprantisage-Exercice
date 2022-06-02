wallet = input ("quelle est votre porte monnaie ") 
price = input ("quelle est le prix de l'objet ")
total = int(wallet) - int(price)


if  wallet >= price:
    print ("Vous pouvez acheter l'objet, il vour restera " + str(total) + " €")
else:
    print ("vous n'avez pas assez d'argent pour acheter ceci") 