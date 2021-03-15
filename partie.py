from plateau import *
import json

class Partie:
    def __init__(self) :
        nb=-1
        while (nb<2  or nb%2 != 0):
            print("Choisissez la taille de votre plateau ")
            nb = int(input())
        
        self.Jeu = Plateau(nb)
        

        #print json string
        
        self.tour=1
        self.passerSonTour=0
        while not self.Jeu.unGagnant() and self.passerSonTour!=2 :
            if (self.tour%2)!=0:
                print("Au tour du joueur 1")
                self.couleur="noir"
            else:
                print("Au tour du joueur 2")
                self.couleur="rouge"
            self.Jeu.PeutOnRetourner(self.couleur)
            self.Jeu.affichage()
            if self.Jeu.getCaseAJouer()>0:
                x=int(input("Choisissez x"))
                y=int(input("Choisissez y"))
                while not self.Jeu.check(x,y,self.couleur):
                    x=int(input("Choisissez x"))
                    y=int(input("Choisissez y"))
                self.Jeu.ajouter(x,y,self.couleur)
                self.passerSonTour=0
                self.annuler =""
                while (self.annuler != "oui") and (self.annuler != "non") :
                        self.annuler= input("Voulez vous annulez votre coup oui ou non")
                if self.annuler=="non":
                    self.tour+=1
                else:
                    self.Jeu.annuler(x,y,self.couleur)
            else:
                if self.passerSonTour==0 :
                    print("Vous n'avez aucune possibilité de jouer vous devez passez votre tour ")
                    self.passerSonTour +=1
                else :
                    print("Vous aussi vous n'avez plus la possibilté de jouer la partie s'arrete la ")
                    self.passerSonTour +=1
                self.tour+=1
            

            
        self.Jeu.quiEstLeGagnant()





     



# for x in range(8):
#     for y in range (8) :9
#         leJeu.Jeu.PeutOnRetourner(x,y,"rouge")







