from model_Weapon import Weapon

class Player :
    def __init__ (self, pseudo, health, attack) :
        self.pseudo = pseudo 
        self.health = health
        self.attack = attack
        self.weapon = None 
    
    def get_pseudo (self):
        return self.pseudo


    def damage (self, damage):
        self.health-= damage
        print ("Aie ... Vous venez de prendre des dégats : " , damage , "!")

    def attack_player (self, target_player) :
        target_player.damage (self.attack)
    
    def get_health(self) :
        return self.health

    
    def set_weapon (self, weapon) :
        self.weapon = weapon
     
    def has_weapon (self) :
        if self.weapon != None :
            self.attack += self.weapon.get_wep_damage()
            return str(self.weapon)