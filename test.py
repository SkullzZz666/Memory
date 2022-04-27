class Carte:
    def __init__(self,valeur):
        self._valeur = valeur
        self._estVisible = False
    def __eq__(self,carteComparee):
        return self._valeur == carteComparee._valeur
    def estVisible(self):
        return self._estVisible
    def affiche(self):
        if(self._estVisible):
            print(self._valeur, end=" ")
        else:
            print("X", end=" ")
    def retourne(self):
        self._estVisible = True if not self._estVisible else False
        
class Memory:
    def __init__(self):
        self._cartes = [Carte("A"), Carte("B"), Carte("B"), Carte("A")]
        self._carteRetenue = None
        self._score = 0
        self._tour = 0
    def affichePartie(self):
        for carte in self._cartes:
            carte.affiche()
        print("\n",end="")
    def partieGagnee(self):
        win = True 
        for carte in self._cartes:
            win = win and carte.estVisible()
        return win
    def compareCartes(self,secondeCarte):
        self._tour+=1 
        if(self._carteRetenue==secondeCarte):
            self._score+=1 
            input("Paire correcte ! Validez pour continuer.")
        else:
            input("Cartes différentes ! Validez pour continuer.")
            self._carteRetenue.retourne()
            secondeCarte.retourne()
    def retourneCarte(self,numero):
        if(not self._cartes[numero].estVisible()):
            self._cartes[numero].retourne()
            if(self._carteRetenue is None):
                self._carteRetenue = self._cartes[numero]
                self.affichePartie()
            else:
                self.compareCartes(self._cartes[numero])
                self._carteRetenue = None
        else:
            nouveauNumero = int(input("Carte déjà retournée, veuillez en choisir une autre !"))
            self.retourneCarte(nouveauNumero)
    def play(self):
        while(self._tour<3 and not self.partieGagnee()):
            self.affichePartie()
            numCarte = int(input("Quelle carte voulez-vous retourner ?"))
            self.retourneCarte(numCarte)
            numCarte = int(input("Quelle seconde carte voulez-vous retourner ?"))
            self.retourneCarte(numCarte)
        print("Vous avez gagné en",self._tour,"comparaisons !")

myGame = Memory()
myGame.play()