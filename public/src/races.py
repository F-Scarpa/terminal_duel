class Races:
    def __init__(self,stre,agi,inte):
        self.stre = stre
        self.agi = agi
        self.inte = inte

    def __repr__(self):
        return f"strength: {self.stre} agility: {self.agi} intellect: {self.inte}"
    
    def __eq__(self,other):
        if self.stre == other.stre and self.agi == other.agi and self.inte == other.inte:
            return True
        return False
    
class Human(Races):
    def __init__(self):
        self.stre = 10 + 2
        self.agi = 10 + 2
        self.inte = 10 + 2
        self.race = "human"

    

class Gnome(Races):
    def __init__(self):
        self.stre = 7
        self.agi = 10
        self.inte = 13
        self.race = "gnome"

class Orc(Races):
    def __init__(self):
        self.stre = 13
        self.agi = 10
        self.inte = 7
        self.race = "orc"

class Troll(Races):
    def __init__(self):
        self.stre = 7
        self.agi = 13
        self.inte = 10
        self.race = "troll"


    
