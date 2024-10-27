import Ships

class InstanceData:
    _instance = None

    def __init__(self):
        if InstanceData._instance:
            raise Exception("Class is singleton")   
        else:
            self.page = 1
            self.all_combs = []
            self.num_people = 0
            self.CP = 0
            self.ships = []
            self.delimeter = []
        
    @staticmethod
    def getInstance():
        if not InstanceData._instance:
           InstanceData._instance = InstanceData()
        return InstanceData._instance

    def setShips(self, pango=0, ares=0, hind=0):
        self.ships = Ships.setShips(pango, ares, hind)

    def initPage(self):
        self.page = 1
    
    def getNextPage(self):
        self.page += 30
    
    def getPreviousPage(self):
        self.page -= 30
    
    def initCombArr(self):
        self.all_combs = [] 
    
    def comb_append(self, comp):
        self.all_combs.append(comp)
    
    def setNumPeople(self, men):
        self.num_people = men
    
    def getNumPeople(self):
        return self.num_people

    def getMaxCP(self):
        cp = 40 * (self.num_people/15)
        self.CP = cp
    
    def setDelim(self, delim):
        delim = delim.replace(" ", "")
        delim = delim.split(",")
        self.delimeter = delim
    
    

