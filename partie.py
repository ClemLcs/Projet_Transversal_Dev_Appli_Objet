from plateau import *
import copy
from time import sleep
import os
import random

class Partie(object):

    #Constructeur

    def __init__(self) :
        self.__jeu = None
        self.__passerSonTour=0
        self.__IA=False
        self.__difficulte=None
        self.__typeDePartie=1
        self.__fichier=None
        self.__nomDuFichier="record"

    #Définition des getters

    @property
    def jeu(self):
        return self.__jeu
    
    @property
    def passerSonTour(self):
        return self.__passerSonTour
    @property
    def IA(self):
        return self.__IA
    @property
    def difficulte(self):
        return self.__difficulte
    @property
    def typeDePartie(self):
        return self.__typeDePartie
    @property
    def nomDuFichier(self):
        return self.__nomDuFichier
    @property
    def fichier(self):
        return self.__fichier

    #Définition des setters

    @jeu.setter
    def jeu(self,value):
        self.__jeu= value
    
    @IA.setter
    def IA(self,value):
        self.__IA= value
        
    @passerSonTour.setter
    def passerSonTour(self,value):
        self.__passerSonTour  = value

    @difficulte.setter
    def difficulte(self,value):
        self.__difficulte= value
    
    @typeDePartie.setter
    def typeDePartie(self,value):
        self.__typeDePartie= value

    @fichier.setter
    def fichier(self,value):
        self.__fichier= value
    
    @nomDuFichier.setter
    def nomDuFichier(self,value):
        self.__nomDuFichier= value

  # Définiton des méthodes de la classes

    # Méthode qui permet de jouer une Partie 
    def laPartie(self):
            # Tant qu'il n'ya pas de gagnant on continue le deroule de  la partie 
        try:
            while  not self.unGagnant(): 
                # On determine la couleur du joueur 
                couleurDuJoueur = self.determinerLaCouleurDuJoueur(self.jeu.tour)
                # On analyse le plateau afin de definir les coups possible pour le joueur actuel
                self.jeu.PeutOnRetourner(couleurDuJoueur) 
                # l'attribue onPeutJouerIci est un tableau de type Plateau qui indique l'ensemble des case sur lequel un joueur a le droit de jouer si ce tableau est vide le joueur sera obligé de passer son tour
                if len(self.jeu.onPeutJouerIci)>0:
                    # Condition  qui permet de savoir si on joue contre l'ordi auquel cas l'ordi joue son tour on verifie aussi qu'on est dans un tour impaire arbitrairement attribué a l'ordi
                    if self.IA and self.jeu.tour%2==0:
                        #Methode qui va permettre a l'ordinateur de jouer son coup en fonction de la difficulté choisi
                        self.affichageDuJoueur()
                        self.minimax(self.jeu,0,-1000,1000)
                        sleep(0.4)
                        self.jeu.affichage("")
                    else:
                        self.tourDunJoueur(couleurDuJoueur)
                    # Si il ya eu une possibilité de jouer alors on fixe passer son tour a 0 
                    self.passerSonTour=0
                else:
                    # Si on a pas eu de possibilité de jouer on passe son tour 
                    self.ilFautPasserSonTour()
        except KeyboardInterrupt:
            self.voulezVousSauvegarder()
            print("\nA bientot\n")
            pass

    # Méthode qui permet de déterminer quel type de partie est joué
    def quelEstLeTypeDePartie(self):
        while True :
            choix = input("\nVoulez vous charger une partie (oui ou non) : ")
            if choix=="oui" or choix=="non":
                break
            
        if choix == "oui":
            # Si l'utilisateur veut charger une partie on lance la methode charger une partie
            self.typeDePartie=2
            self.chargerLaPartie()
        else:
            self.fichier = open("record.txt", "w")
            self.fichier.write("Début de la partie")
            self.fichier.write("\n")
            self.jouercontreOrdi()
            # Si l'utilisateur veut une nouvelle partie on lui demande la taille du plateau 
            self.laTailleDuPlateau()
    
    # Méthode qui permet de changer et jouer une Partie enregistré
    def chargerLaPartie(self) :
        while True:
        # On lui demande le nom de la partie qu'on souhaite chargé on s'assure que le fichier rentré existe 
            try:
                self.nomDuFichier = input("Quel fichier voulez vous charger ? ")
                self.fichier = open(self.nomDuFichier + ".txt", "r")
                break
            except :
                print("Ce fichier n'existe pas ")

        ligne = self.fichier.readline()    
        i=0
        couleur=""
        # On parcourt notre fichier chargé 
        while ligne != "":
            if i==1:
                
                if ligne.split()[2] == "True" :
                    self.IA = True
                else :
                    self.IA = False
            if i==2:
                self.difficulte= ligne.split()[2]
            if i==3:
                # On recupere la taille du plateau 
                taillePlateau = ligne.split()[9]
                # Puis on cree le plateau avec la taille recuperé
                self.jeu= Plateau(int(taillePlateau))
                self.affichageDuJoueur()
                self.jeu.affichage("")
            if i>3:
                # On recupere chacun des coups pour les ajouter sur notre plateau en affichant chaque coup 
                x = ord(ligne.split()[2].lower())-96
                y = int(ligne.split()[3])
                # On gere le cas ou un joueur aurait passé son tour et que donc un même joueur aurait jouer deux fois d'affilé
                if couleur == ligne.split()[0]:
                    self.jeu.tour+=1
                couleur=ligne.split()[0]
                self.jeu.PeutOnRetourner(couleur)
                self.jeu.ajouter(x, y, couleur)
                self.jeu.affichage("")
                sleep(1)
               
            # On passe a la ligne suivante 
            ligne = self.fichier.readline()
            i+=1
        

        self.fichier = open(self.nomDuFichier + ".txt", "a")

    # Méthode d'affichage
    def affichageDuJoueur(self):
        if self.IA and self.jeu.tour%2==1:
            print ("A votre tour (x)")
        elif self.IA and self.jeu.tour%2==0:
            print ("Au Tour de l'ordinateur\n")
        elif self.jeu.tour%2==1:
            print("Au tour du joueur 1 (x)\n")
        else:
            print("Au tour du joueur 2 (o)\n")


    # Méthode qui permet de déterminer et générer la taille du plateau 
    def laTailleDuPlateau(self):
        taillePlateau=0
        # Simple demande a l'utilisateur la taille du plateau voulu
        while (taillePlateau<2 or taillePlateau > 26 or taillePlateau%2 != 0):
            try:
                taillePlateau = int(input("\nChoisissez la taille de votre plateau :  ")) 
                if taillePlateau<2 or taillePlateau > 26 or taillePlateau%2==1:
                    print("\n Assurez vous bien que la taille de votre plateau soit paire, superieure a 2 et inférieur à 26")                
            except:
                print("Taille du plateau invalide")

        print("\nBonne chance !")
        print("PS : Appuyer sur ctrl+c pour quitter et sauvegarder\n")
        sleep(2)
            
        # On cree le plateau 
        self.jeu = Plateau(taillePlateau)
        # Ici j'écris dans le fichier la taille du plateau
        self.fichier.write("La taille du plateau pour cette partie est : ") 
        self.fichier.write(str(taillePlateau))
        self.fichier.write("\n")


    # Méthode qui definit la couleur du pion qui va être joué
    def determinerLaCouleurDuJoueur(self,tour):
        if (tour%2)!=0:     
            return "noir"
        else:
            return "blanc"

    # Méthode qui permet d'annuler un coup et de ne pas l'enregistrer   
    def annulerUnCoup(self,x,y ,couleur):
        #Simple demande a l'utilisatuer s'il souhaite annuler son coup ou non 
        while True :
            annuler= input("\nVoulez vous annuler votre coup (oui ou non) : ")
            if annuler=="oui" or annuler=="non":
                break
        if annuler=="oui":
            #Si oui on lance la methode annuler de type Plateau
            self.jeu.annuler(x, y, couleur)
        else:
            #Si il n'annule pas le coup on l'enregistre 
            self.enregistrement(x, y, couleur)
    
    # Méthode qui permet de passe un tour
    def ilFautPasserSonTour(self):
        #Affichage du message en fonction de la valeur de passer son tour et si on joue à 2 ou 1 joueur(s)
        if self.passerSonTour== 0:
            self.affichageDuJoueur()
            if self.IA and self.jeu.tour % 2 == 0:
                print("L'ordinateur ne peut plus jouer il doit passer son tour \n")
            else:
                print("Vous n'avez aucune possibilité de jouer vous devez passez votre tour\n ")
            self.passerSonTour += 1
        else :
            self.affichageDuJoueur()
            if self.IA and self.jeu.tour%2==0:
                print("L'ordinateur ne peut plus jouer il doit lui aussi passer son tour la partie s'arrete la\n ")
            else :
                print("Vous aussi vous n'avez plus la possibilté de jouer la partie s'arrete la\n ")
            self.passerSonTour +=1
        self.jeu.tour+=1

    # Méthode qui permet de jouer contre l'ordinateur
    def jouercontreOrdi(self):
        while True:
            choix= input("Voulez vous jouer contre l'ordinateur (oui ou non) : ")
            if choix=="oui" or choix=="non":
                break
            
        if choix== "oui":
            #Si oui on fixe IA a true pour indiquer à d'eventuelles methodes  qu'on va jouer contre l'ordinateur
            self.IA=True
            while self.difficulte != "facile" and self.difficulte != "moyen" and  self.difficulte !="difficile":
                self.difficulte=  input("\nChoisissez la difficulté (facile moyen ou difficile) : ")
        
        self.fichier.write("IA :  ")
        self.fichier.write(str(self.IA))
        self.fichier.write("\n")
        self.fichier.write("difficulte :  ")
        self.fichier.write(str(self.difficulte))
        self.fichier.write("\n")

    # Méthode qui permet d'enregister les données du joueurs dans le fichiers texte
    def enregistrement(self, x, y, laCouleur) :
        
        self.fichier.write(laCouleur)
        self.fichier.write(" : ")
        self.fichier.write(chr(x+64))
        self.fichier.write(" ")
        self.fichier.write(str(y))
        self.fichier.write("\n")

    # Méthode qui permet d'enregistrer le fichier sur le disque ou non

    def voulezVousSauvegarder(self) :
        self.fichier.write("")
        self.fichier.close()   
        while True :
            choix = input("\nVoulez vous enregistrer (oui ou non) : ") 
            if choix == "oui" or choix == "non" :
                break
        if choix == "oui" :
            while True :
                try :
                    rename = input("le nom de l'enregistrement : ")
                    os.rename(r'./' + self.nomDuFichier + '.txt',r'C:./' + rename + '.txt')
                    break
                except OSError :
                    print("Le nom que vous avez entré n'est pas valide")
                except FileExistsError :
                    print("Le fichier existe déjà")
                except : 
                    print("Error !")
        else : 
            os.remove(r"./" + self.nomDuFichier + '.txt')



    # Méthode pour savoir qui est le gagant en comparant le nombre de pions noir et de pions blancs affiche un different message si on joue a deux joueurs ou contre l'ordinateur
    def quiEstLeGagnant(self):
        if self.jeu.noir>self.jeu.blanc:
                if self.IA :
                        print("Vous avez battu l'ordinateur")
                else:
                        print("Et le grand gagnant est le joueur 1 ")
        elif self.jeu.noir<self.jeu.blanc:
                if self.IA :
                        print("L'ordinateur vous a battu")
                else:
                        print("Et le grand gagnant est le joueur 2 ")
        else:
                print("Nous avons une égalité")


    # Méthode qui définit s'il y a un gagnant
    def unGagnant(self): 
        nombreDeCase= self.jeu.tailleDuPlateau*self.jeu.tailleDuPlateau
        # Conditions necessaires pour que la partie s'arrete
        if self.passerSonTour==2 or self.jeu.noir==0 or self.jeu.blanc==0 or (self.jeu.blanc+ self.jeu.noir) ==  nombreDeCase:
            self.quiEstLeGagnant()
            self.voulezVousSauvegarder()
            return True
        else:
            return False

    # Méthode qui permet de définir le tour d'u joueur
    def tourDunJoueur(self,couleur):
    # On affiche le plateau avec les cases jouable en surbrillance
        self.affichageDuJoueur()
        self.jeu.affichage("Avant")
        #On demande a l'utilisateur de choisir sa case 
        while True :
            try:
                saisie = input("\nChoisissez une case (ex : A 5) : ").split()
                x=ord(saisie[0].lower())-96
                y=int(saisie[1])
                #On verifie la validité du coup 
                if self.jeu.check(x, y, couleur): 
                    break
            except (TypeError, ValueError,IndexError) as error:
                print("Erreur de saisie")      
    # <on ajoute notre pion
        self.jeu.ajouter(x, y, couleur)
    # Puis on reaffiche le plateau sans surbrillance
        self.jeu.affichage("")
    # Pour laisser a l'utilisateur la possibilté d'annuler son coup
        self.annulerUnCoup(x, y, couleur)


    # Méthode de reccurence determinant le meilleur coup a jouer a un moment donné en mimisant la perte maximum
    def minimax(self,jeu , profondeur,alpha,beta):
        laCouleurActuelle = self.determinerLaCouleurDuJoueur(jeu.tour)
        jeu.PeutOnRetourner(laCouleurActuelle)
        # Si la partie se finit ou on atteint la profondeur souhaité on calcule la valeur heuristique de la case atteint
        if len(jeu.onPeutJouerIci)==0 or profondeur==5:
            # On determine la valeur d'un 'coup' en fonction de la difficulté choisi
                return self.heuristique(jeu)
        else :
            lesjeux=[]
            # Comme l'attribut onPeutJouerIci peut contenir des doublons on s'assure de les supprimer
            lesCoupsJouables=list(set(jeu.onPeutJouerIci))
            tableauDeCoup= []
            for i in range(len(lesCoupsJouables)):
                # On crée autant de copie de plateau qu'il ya de coup jouable au moment donné et on les range dans un tableau 
                lacopie=copy.deepcopy(jeu)
                lesjeux.append(lacopie)
                # Puis a chaque copie nous jouons un des coups jouable au moment donné
                lesjeux[i].ajouter(lesCoupsJouables[i][0],lesCoupsJouables[i][1],laCouleurActuelle)
                # Puis on reattribut a chacun de ses nouveau plateaux la methode de reccurence minimax jusqu'à donc atteindre la profondeur defini precedemment ou alors que la partie se finisse
                eval=self.minimax(lesjeux[i],profondeur+1,alpha,beta)
                # On les range dans un tableau pour pouvoir les utiliser plus facilement 
                tableauDeCoup.append(eval)
                # alpha et beta vont nous permettre de limiter les branches parcourus pour rendre la methode plus econome 
                if profondeur%2==0:
                    alpha=max(alpha,eval)
                    if beta<=alpha:
                        break
                else:
                    beta=min(beta,eval)
                    if beta <= alpha: 
                        break
            # Une fois qu'on a notre tableau remplis 
            if profondeur==0: 
                # A profondeur == 0 c'est a dire a la premiere iteration  on joue la case qui va remonter par le biais de la methode 
                index = index = max(range(len(tableauDeCoup)), key=tableauDeCoup.__getitem__)
                x=lesCoupsJouables[index][0]
                y=lesCoupsJouables[index][1]
                self.jeu.ajouter(x,y,"blanc") 
                self.enregistrement(x, y, "blanc")
                
                  

            elif  profondeur%2==0:
                # Si la profondeur est paire on retourne la valeur max de notre tableau
                return max(tableauDeCoup)

            else:
                # Si la profondeur est impaire on retourne la valeur min de notre tableau
                return min(tableauDeCoup)

    def heuristique(self,jeu):
        # On part du principe que l'ordi jouera uniquement les blancs si la difficulte est en facile on retourne donc le nombre de pions noirs- le nombre de pions blancs (ce qui desavantage l'ordi)
        if self.difficulte=="facile":
                   return jeu.noir - jeu.blanc
        elif self.difficulte=="moyen":

            hasard= random.random()
             # Si la difficulte est en moyen on initialise un float au hasard entre 0 et 1 ce qui permettra d'avoir 50%de chance qu'il nous retourne un resultat à l'avantage de l'ordi ou non 
            if hasard<0.5:
                return jeu.noir - jeu.blanc
            else :
                return jeu.blanc - jeu.noir
        # Si la difficulte est en difficile on retourne donc le nombre de pions blancs - le nombre de pions noirs  (ce qui avantage l'ordi)
        elif self.difficulte=="difficile":
            return jeu.blanc - jeu.noir
