class Ship:
    def __init__(self, name, maxCrew, cp, hitpoints, dps, speed):
        self.name = name
        self.maxCrew = maxCrew
        self.cp = cp
        self.HP = hitpoints
        self.dps = dps
        self.speed = speed


def setShips(pango = 0, ares = 0, hind = 0):
    ships = []
    ships.append(Ship("Starling", 2, 2, 3800, 780, 8))
    ships.append(Ship("Pelican", 3, 6, 5000, 510, 6))
    ships.append(Ship("Dart", 3, 6, 6000, 780, 10))
    ships.append(Ship("Bullet", 3, 7, 5750, 780, 10))
    ships.append(Ship("Cutlass", 3, 9, 11000, 1020, 9))
    ships.append(Ship("Dragon", 3, 11, 8500, 1410, 8))
    ships.append(Ship("Stiletto", 3, 11, 10000, 1470, 9))
    ships.append(Ship("Hook", 3, 11, 10000, 1020, 8))
    ships.append(Ship("Mercury", 3, 13, 17500, 900, 2))
    ships.append(Ship("Poseidon", 3, 14, 18000, 1020, 2))
    ships.append(Ship("Binglehopper", 3, 18, 24000, 960, 1))
    ships.append(Ship("Weasel", 4, 8, 8000, 1350, 8))
    ships.append(Ship("Pheasant", 4, 8, 8000, 1350, 9))
    ships.append(Ship("Marauder", 4, 8, 6500, 1350, 10))
    ships.append(Ship("Marlin", 4, 8, 8000, 2040, 7))
    ships.append(Ship("Shark", 4, 10, 9000, 2040, 8))
    ships.append(Ship("Kestrel", 4, 10, 11500, 900, 10))
    ships.append(Ship("Beaver", 4, 11, 10000, 1530, 8))
    ships.append(Ship("Fang", 4, 12, 10500, 1530, 9))
    ships.append(Ship("Ibis", 4, 12, 10500, 1530, 10))
    ships.append(Ship("Corsair", 4, 12, 10000, 1350, 10))
    ships.append(Ship("Falchion", 4, 13, 13000, 1350, 8))
    ships.append(Ship("Grouse", 4, 13, 16000, 1530, 7))
    ships.append(Ship("Fox", 4, 15, 10000, 1530, 7))
    ships.append(Ship("Albatross", 4, 15, 15000, 1350, 8))
    #ships.append(Ship("Ceres", 4, 18, 24000, 1230, 1))
    ships.append(Ship("Goose", 5, 8, 12000, 1800, 6))
    ships.append(Ship("Manta", 5, 8, 8800, 1530, 8))
    ships.append(Ship("Orca", 5, 10, 9200, 2040, 8))
    ships.append(Ship("Widgeon", 5, 10, 13000, 1800, 6))
    ships.append(Ship("Serpent", 5, 11, 12000, 2040, 8))
    ships.append(Ship("Tyrant", 5, 12, 10500, 2040, 10))
    ships.append(Ship("Otter", 5, 12, 12500, 1800, 10))
    ships.append(Ship("Phoenix", 5, 14, 15500, 1800, 9))
    ships.append(Ship("Neptune", 5, 17, 24000, 2330, 1))
    ships.append(Ship("Mongoose", 6, 14, 17500, 2250, 6))
    ships.append(Ship("Mastiff", 6, 14, 19500, 2250, 6))
    ships.append(Ship("Mule", 6, 16, 20500, 2250, 6))
    ships.append(Ship("Chimera", 6, 16, 18500, 1800, 7))
    ships.append(Ship("Gryphon", 6, 16, 21000, 2040, 6))
    ships.append(Ship("Kirin", 6, 16, 19000, 2250, 6))
    ships.append(Ship("Gargoyle", 6, 16, 23000, 2550, 6))
    ships.append(Ship("Osprey", 7, 14, 17000, 3060, 7))
    ships.append(Ship("Retaliator", 7, 14, 16500, 3060, 7))
    ships.append(Ship("Brigand", 7, 16, 16000, 3060, 8))
    ships.append(Ship("Sigil", 7, 16, 19500, 2700, 6))
    ships.append(Ship("Camel", 7, 20, 22000, 2700, 6))
    ships.append(Ship("Concord", 8, 17, 21000, 3150, 6))
    ships.append(Ship("Alliance", 9, 18, 23000, 3600, 6))
    ships.append(Ship("Pigeon", 10, 20, 22000, 4350, 6))
    ships.append(Ship("Covenant", 10, 22, 25000, 4050, 6))
    if hind == 1:
        ships.append(Ship("Hind", 11, 26, 28000, 5700, 6))
    ships.append(Ship("Poseidon w/ sails", 3, 15, 18000, 1020, 2))
    if ares == 1:
        ships.append(Ship("Ares", 4, 28, 28000, 3060, 4))
    ships.append(Ship("Brigand Elite", 8, 16, 16000, 3150, 8))
    ships.append(Ship("Raider", 8, 12, 8000, 780, 10))
    if pango == 1:
        ships.append(Ship("Pangolin", 9, 18, 25000, 3600, 6))
    return ships
