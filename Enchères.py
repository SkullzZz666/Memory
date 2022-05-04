from platform import processor
import random

class Enchere:
    def __init__(self):
        self.prix = random.randint(20,60)
        self.object = 10
        self.objectE = 0
        self.objectJ = 0
        self.money = 1000

    def FinGame(self):
        win = False
        if (self.object == 0):
            win = True
            print("les enchères sont fini !")
        return win 

    def actionE(self):
        choixE = random.randint(1,2)
        if (choixE == 1):
            propositionE = random.randint(20,100)
            self.prix = self.prix + propositionE 
            print("une autre personne encherie et augmente le prix, maintenant le prix est a : ",self.prix, "qui veut monter l'enchère ? ")
        else :
            print("vous gagner l'object bravo, ne vous inquiétez pas le prochain object arrive bientôt")
            self.object =self.object - 1
            self.objectJ =self.objectJ + 1
            self.money = self.money - self.prix
            return self.prix
    
    def Player(self):
        print("le prix de l'object est a ", self.prix)
        propositionJ = int(input("de combien voulez vous enchérire ! \n"))
        if (propositionJ == 0):
            print("vous n'avez pas encherie l'autre personne a gagner l'object")
            self.object = self.object -1
            self.objectE = self.objectE +1
            return self.prix
        else:
            self.prix = self.prix + propositionJ
            print("vous avez encherie, le prix est a : ", self.prix, "qui veut monter l'enchère ? ")


    def play(self):
        while (self.object != 0 and not self.FinGame()):
            print("il vous reste ",self.money,"€")
            self.Player()
            self.actionE()

myGame = Enchere()
myGame.play()