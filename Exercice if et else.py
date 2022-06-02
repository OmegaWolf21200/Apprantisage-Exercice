
print ("Bonjour bienvenu au cinéma")
age = input ("Quelle age avez vous: ")

if int(age) < 18 :
    Total = 7
else: 
    Total = 12

popcorne = input ("voullez vous du popcorne: (Oui, Non) ") 
if popcorne == "Oui": 
    Total += 5 

print ("Tres bien, cela vous fera un total de " +str(Total))