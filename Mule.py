class joueur:
    def __init__(self, valeur, food, ore, energy, cristal, farm, factory, reactor, mine):
        self.__valeur = valeur
        self.__estVisible = False
        self.__food = food
        self.__ore = ore
        self.__energy = energy
        self.__cristal = cristal
        self.__farm = farm
        self.__factory = factory
        self.__reactor = reactor
        self.__mine = mine
        
    def estVisible(self):
        return self.__estVisible
    