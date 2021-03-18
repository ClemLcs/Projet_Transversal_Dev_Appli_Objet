from plateau import *
import json

class Partie:
    def __init__(self) :
        nb=-1
        while (nb<2 or nb%2 != 0):
            nb = int(input("Choisissez la taille de votre plateau : "))
        
        Jeu = Plateau(nb)
        
        #print json string
        
        tour=1
        passerSonTour=0

        while not Jeu.unGagnant() and passerSonTour!=2 :
            if (tour%2)!=0:
                print("Au tour du joueur 1")
                laCouleur="noir"
            else:
                print("Au tour du joueur 2")
                laCouleur="blanc"

            Jeu.PeutOnRetourner(laCouleur)
            Jeu.affichage("Avant")

            if Jeu.caseAJouer>0:

                while True :
                    saisie = input("\n\nChoississez une case (ex : 3 5) : ").split()
                    if Jeu.check(int(saisie[0]), int(saisie[1]), laCouleur) :
                        Jeu.ajouter(int(saisie[0]), int(saisie[1]), laCouleur)
                        break

                passerSonTour=0
                annuler =""

                Jeu.affichage("")

                while (annuler != "oui") and (annuler != "non") :
                        annuler= input("\n\nVoulez vous annulez votre coup (oui ou non) : ")
                if annuler=="non":
                    tour+=1
                else:
                    Jeu.annuler(int(saisie[0]), int(saisie[1]), laCouleur)
                   

            else:
                if passerSonTour==0 :
                    print("Vous n'avez aucune possibilité de jouer vous devez passez votre tour ")
                    passerSonTour +=1
                else :
                    print("Vous aussi vous n'avez plus la possibilté de jouer la partie s'arrete la ")
                    passerSonTour +=1
                tour+=1

        Jeu.quiEstLeGagnant()