class Carte: 
    def __init__(self, caractere):
        self.__valeur = caractere
        self.__visibility = False
        
    def getValeur (self):
        return self.__valeur 
    def affichage (self):
        if (self.__visibility == 'false'):
            return 'x'
        else : 
            print(self.__valeur)
            return self.__valeur
    def setVisibility (self):