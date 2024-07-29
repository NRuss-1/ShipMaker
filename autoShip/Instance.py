

class InstanceData:
    def __init__(self):
        self.page = 1
        self.all_combs = []
        self.num_people = 0
        self.CP = 0

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
    
    def getInstance(self):
        return self
    