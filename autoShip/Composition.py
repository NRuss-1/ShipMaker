import Ships

class Composition:
    def __init__(self, comp):
        self.comp = comp

    def getHP(self):
        hp = 0
        for boat in self.comp:
            hp += boat.HP
        return hp
    
    def getNames(self):
        names = []
        for boat in self.comp:
            names.append(boat.name)
        return names
            
    def validate(self, maxCP, people):
        if self.getCP() > maxCP:
            return False
        if self.getManning() > people:
            return False 
        if self.getCP() < maxCP - (maxCP*.1):
            return False
        return True

    def getCP(self):
        cp = 0
        for boat in self.comp:
            cp += boat.cp
        return cp
    
    def getManning(self):
        men = 0
        for boat in self.comp:
            men += boat.maxCrew
        return men
    
    def getDPS(self):
        dps = 0
        for boat in self.comp:
            dps += boat.dps
        return dps 
    
    def getSpeed(self):
        speed = 0
        for boat in self.comp:
            speed += boat.speed
        return speed
    
    def getRelativePower(self):
        hp = self.getHP()
        dps = self.getDPS()
        speed = self.getSpeed()
        cp = self.getCP()
        
        rel_power = (hp + speed + dps) * cp * (1/len(self.comp))
        return rel_power