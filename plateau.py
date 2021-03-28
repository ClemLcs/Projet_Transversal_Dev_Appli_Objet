from case import *
class Plateau(object):

    #Constructeur

    def __init__(self,tailleDuPlateau) :

        self.__noir = 2
        self.__blanc = 2 
        self.__tailleDuPlateau = tailleDuPlateau
        self.__tour = 1
        #onPeutJouerIci est une liste de tuples des coordonées jouables sur le plateau a un moment donné
        self.__onPeutJouerIci = []
        #la variable list est une liste de liste representant notre plateau il contiendra l'ensemble de nos cases
        self.__list = [[0 for i in range(tailleDuPlateau)] for j in range(tailleDuPlateau)]
        # On crée notre matrice contenant des objets
        for i in range(tailleDuPlateau):
            for y in range(tailleDuPlateau):
                    # On initialise notre plateau avec les 4 pions deja posés sur les cases du centre
                    if i == (tailleDuPlateau / 2) - 1 and y == (tailleDuPlateau / 2) - 1:
                            self.__list[i][y] = Case(i,y,"noir") 
                    elif i == (tailleDuPlateau / 2) and y == (tailleDuPlateau / 2) - 1:
                            self.__list[i][y] = Case(i,y,"blanc") 
                    elif i == (tailleDuPlateau / 2) - 1 and y == (tailleDuPlateau / 2):
                            self.__list[i][y] = Case(i,y,"blanc") 
                    elif i == (tailleDuPlateau / 2) and y == (tailleDuPlateau / 2):
                            self.__list[i][y] = Case(i,y,"noir") 
                    else:
                            self.__list[i][y] = Case(i,y,"vide")
        
    #Définition des getters
    @property
    def list(self):
            return self.__list
    @property
    def tour(self):
            return self.__tour
    @property
    def tailleDuPlateau(self):
            return self.__tailleDuPlateau
    @property
    def blanc(self):
            return self.__blanc
    @property
    def noir(self):
            return self.__noir
    @property
    def onPeutJouerIci(self):
            return self.__onPeutJouerIci
 
    #Définition des setters
    @blanc.setter
    def blanc(self,value):
            self.__blanc = value     
    @noir.setter
    def noir(self,value):
            self.__noir = value     
    @onPeutJouerIci.setter
    def onPeutJouerIci(self,value):
            self.__onPeutJouerIci = value 
    @tour.setter
    def tour(self,value):
            self.__tour = value
                                       


    def affichage(self, choix) :
            # Simple methode d'afichage avec un parametre qui indique si dans notre affichage on souhaite voir les cases jouable par le joueur
            if choix == "Avant":
                    print("                   Score : Joueur 1 =",self.noir,"Joueur 2 =",self.blanc)
            print("\n ", end="                         ")
            for x in range(1, self.tailleDuPlateau + 1):
                    print(x, end="  ")

            for x in range(self.tailleDuPlateau):

                    print("\n ", end="                     ")
                    print(chr(x + 1 + 64), end="   ") # Transformation des chiffres en lettres

                    for y in range(self.tailleDuPlateau) :

                            # Création des points à l'affichage
                            if  (self.list[x][y].couleur == "noir"):
                                    print("x", end="  ")
                            elif  (self.list[x][y].couleur == "blanc"):
                                    print("o", end="  ")

                            # Si choix = "Avant" on affiche tous les coups jouables par le joueur sous la forme
                            elif len(self.list[x][y].coupJouable) > 0 and choix == "Avant":
                                    print("*", end="  ")
                            elif (self.list[x][y].couleur == "vide"):
                                    print(".", end="  ")
            print("\n")

    # Methode permettant de regler le nombre de pions noir ou blanc sur le pateau
    def pionEnPlus(self,couleur,nombre):
            if couleur == "noir":
                    self.noir +=nombre
            else:
                    self.blanc +=nombre

    # Methode permettant de regler le nombre de pions noir ou blanc sur le pateau
    def pionEnMoins(self,couleur,nombre):
            if couleur == "noir":
                    self.noir -=nombre
            else:
                    self.blanc -=nombre

    #Methode retournant la couleur de l'adversaire en fonction de sa propre couleur
    def couleurOppose(self,couleur):
            if couleur == "noir":
                    return "blanc"
            else:
                    return"noir"

    # Methode qui permet de savoir si des coordonées sont en dehors de notre plateau
    def estOnHorsLimite(self,x,y):
            if x < 0 or x >= self.tailleDuPlateau or y < 0 or y >= self.tailleDuPlateau:
                    return True
            else:
                    return False

    # Methode permettant de determiner l'ensemble des case à jouer
    def PeutOnRetourner(self,couleur):
            self.onPeutJouerIci.clear() 
            
            #Deux boucles pour scanner un par un l'ensemble des cases du plateau
            for x in range(1,self.tailleDuPlateau + 1):
                    for y in range(1,self.tailleDuPlateau + 1):
                            #Cette condition va permettre de verifier
                            #seulement les cases vides
                            if self.list[x - 1][y - 1].couleur == "vide":
                                    #On efface coupJouable de chaque case
                                    #pour bien avoir les informations de ce
                                    #tour
                                    self.list[x - 1][y - 1].coupJouable.clear()
                                    #Puis on verifie pour chaque case dans
                                    #toutes les directions
                                    #si il ya une possibilité de retourner
                                    #un pion adverse en la jouant
                                        
                                    #En haut
                                    if x > 2: 
                                            self.PeutOnRetournerVersUneDirection(x,y,couleur,-1,0) 
                                    #En bas
                                    if x < self.tailleDuPlateau - 1:
                                            self.PeutOnRetournerVersUneDirection(x,y,couleur,1,0) 
                                    #A gauche
                                    if y > 2:
                                            self.PeutOnRetournerVersUneDirection(x,y,couleur,0,-1) 
                                    #A droite
                                    if y < self.tailleDuPlateau - 1:
                                            self.PeutOnRetournerVersUneDirection(x,y,couleur,0,1) 
                                    #en haut a droite
                                    if x > 2 and y < self.tailleDuPlateau - 1:
                                            self.PeutOnRetournerVersUneDirection(x,y,couleur,-1,1) 
                                    #en bas a droite
                                    if x < self.tailleDuPlateau - 1 and y < self.tailleDuPlateau - 1 : 
                                            self.PeutOnRetournerVersUneDirection(x,y,couleur,1,1) 
                                    #en bas a gauche
                                    if x < self.tailleDuPlateau - 1 and y > 2 : 
                                            self.PeutOnRetournerVersUneDirection(x,y,couleur,1,-1) 
                                    #en haut a gauche
                                    if x > 2 and y > 2 :  
                                            self.PeutOnRetournerVersUneDirection(x,y,couleur,-1,-1)
                                        

       
    #Méthode qui permet de chercher dans la direction voulu si on peut retourner
    def PeutOnRetournerVersUneDirection(self,x,y,couleur,directionVerticale,directionHorizontale):
            # On verifie dabbord que la premiere case que l'on rencontre est occupé par un pion de la couleur adverse
            if self.list[x - 1 + directionVerticale][y - 1 + directionHorizontale].couleur == self.couleurOppose(couleur) :
                    # i nous renseignera sur combien de pion on peut retoruner
                    i = 1
                    while True:
                            # On verifie qu'on ne sort pas du plateau
                            if self.estOnHorsLimite(x - 1 + directionVerticale + (i * directionVerticale),y - 1 + directionHorizontale + (i * directionHorizontale)):
                                    break
                                    # Si la n ieme case dans la direction indiqué est de la meme couleur que celui qui joue
                            elif self.list[x - 1 + directionVerticale + (directionVerticale * i)][y - 1 + directionHorizontale + (i * directionHorizontale)].couleur == couleur:
                                    # on indique dans l'attribut coupjouable de la case joué que jouer sur cette case retournera i pions vers telle direction
                                    self.list[x - 1][y - 1].coupJouable.append((directionVerticale,directionHorizontale,i))
                                    # On indique que cette case est jouable
                                    self.onPeutJouerIci.append((x,y))
                                        
                                    break
                            #On continu a avancer dans la direction indiqué en incrementant de 1 i tant qu'on tombe sur des cases occupées par des pions de couleurs adverse au joueur actuel
                            elif self.list[x - 1 + directionVerticale + (directionVerticale * i)][y - 1 + directionHorizontale + (i * directionHorizontale)].couleur == self.couleurOppose(couleur):
                                    i+=1
                            else:
                                    break

 
                
    # Methode qui permet de verifier certaines conditions de jeu
    def check(self, x, y, couleur):
            # Si la case que l'on veut jouer est hors limite
            if x < 1 or y < 1 or x > self.tailleDuPlateau or y > self.tailleDuPlateau:
                    print("Oh cette case est hors limite")
                    return False
            # Si la case que l'on veut jouer est deja utilisé
            elif  self.list[x - 1][y - 1].couleur != "vide":
                    print("Oh cette case est deja occupé")
                    return False
            # Si la case que l'on veut jouer ne retournera aucun pion adverse
            elif len(self.list[x - 1][y - 1].coupJouable) == 0:
                    print("Jouez ici ne retournera aucune piece adverse")
                    return False
            #return true si tout est bon
            else:
                    return True    


    # Méthode qui permet de retourner un pion
    def retourner(self,x,y,couleur):
            # Apres que le joueur ait placé son pion sur une case On verifie dans lattribue coup jouable de cette case vers quelle direction et combien de piece adverse il faut retourner
            for element in self.list[x - 1][y - 1].coupJouable:
                    # On ajuste aussi les attributs representant le nombre de pions de chaque couleur sur le plateau
                    self.pionEnPlus(couleur,element[2])
                    self.pionEnMoins(self.couleurOppose(couleur),element[2])
                    for z in range(element[2]):
                            self.list[x - 1 + element[0] + z * element[0]][y - 1 + element[1] + z * element[1]].couleur = couleur
                        

                                
    # Méthode qui attribue à une case vide la couleur du joueur qui pose son pion
    def ajouter(self,x,y,couleur):
            # Elle ajoute à la case vide la couleur du joueur qui pose son pion
            self.list[x - 1][y - 1].couleur = couleur
            # puis elle ajuste le nombre de pions
            self.pionEnPlus(couleur,1)
            # Et enfin retourner les pions adverses qu'elle doit retourner
            self.retourner(x,y,couleur)
            # Des qu'on ajoute un pion on passe au tour suivant
            self.tour +=1
        
    # Méthode qui permet d'annuler le coup qui vient d'être effectué
    def annuler(self,x,y,couleur):
            # on recupere la couleur oposé a celle du joueur qui vient de jouer
            couleurOppose = self.couleurOppose(couleur)
            # la case qui vient d'être joué est remis a vide
            self.list[x - 1][y - 1].couleur = "vide"
            self.pionEnMoins(couleur,1)
            # Puis on retourne dans l'autre sens tous les pions qui viennent être retourné
            self.retourner(x,y,couleurOppose)
            self.tour -=1
