
class Composition:
    def __init__(self, comp, instanceData):
        self.instanceData = instanceData
        self.comp = comp
        self.cp = 0
        self.hp = 0
        self.mannning = 0 
        self.dps = 0
        self.speed = 0

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
        if self.instanceData.delimeter[0] != '':
            for boat in self.instanceData.delimeter:
                if boat not in self.getNames():
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
    
    def getManningRatio(self):
        max_people = self.instanceData.num_people
        manning = self.getManning()
        return manning/max_people

    def getCompSize(self):
        return len(self.comp)
    
    def getRelativePower(self):
        hp = self.getHP()
        dps = self.getDPS()
        speed = self.getSpeed()
        cp = self.getCP()
        
        rel_power = (hp + speed + dps) * (1.5 *cp) * (1/self.getCompSize()) * (1.5*self.getManningRatio())
        return rel_power
