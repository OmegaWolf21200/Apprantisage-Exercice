from model_Player import Player
from model_Weapon import Weapon



knife = Weapon("Knife", 5)

print (knife.get_pseudo ())


player1 = Player ("Graven", 20, 3 ) 


player2 = Player ("Bob", 20, 5 )  
player2.set_weapon(knife)
player2.has_weapon()

player2.attack_player(player1)

print ("Le joueur ", str(player1.get_pseudo()) , "a donc" , str(player1.get_health()) , "point de vie")




