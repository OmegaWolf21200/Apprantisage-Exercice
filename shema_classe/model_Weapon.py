class Weapon :
    def __init__(self, name, wep_damage) :
        self.name = name 
        self.damage = wep_damage
    
    def get_pseudo (self):
        return self.name

    def get_wep_damage (self) :
        return self.damage 