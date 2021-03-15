from case import *
class Plateau :
        def __init__(self,nb) :
           self.__noir__=2
           self.__rouge__=2 
           self.__nb__=nb   
           self.__caseAJouer__=0
           self.__list__=[[0 for i in range(nb)] for j in range(nb)]
           for i in range(nb):
                for y in range(nb):
                        if i==(nb/2)-1 and y==(nb/2)-1:
                                self.__list__[i][y]=Case(i,y,"noir") 
                        elif i==(nb/2) and y==(nb/2)-1:
                                self.__list__[i][y]=Case(i,y,"rouge") 
                        elif i==(nb/2)-1 and y==(nb/2):
                                self.__list__[i][y]=Case(i,y,"rouge") 
                        elif i==(nb/2) and y==(nb/2):
                                self.__list__[i][y]=Case(i,y,"noir") 
                        else:
                                self.__list__[i][y]=Case(i,y,"vide")
        

        def getList(self):
                return self.__list__
        def getnb(self):
                return self.__nb__
        def getrouge(self):
                return self.__rouge__
        def getnoir(self):
                return self.__noir__
        def getCaseAJouer(self):
                return self.__caseAJouer__
                        
                
                
                


        def affichage(self) :

                print("\n ", end="   ")
                for x in range(1, self.getnb()+1):
                        print(x, end="  ")

                for x in range(self.getnb()):
                        print("")
                        print (x+1, end="   ")
                        for y in range (self.getnb()) :
                                if  ( self.getList()[x][y].get_CaseCouleur()=="noir"):
                                        print("x", end="  ")
                                elif  ( self.getList()[x][y].get_CaseCouleur()=="rouge"):
                                        print("o", end="  ")
                                elif len(self.getList()[x][y].get_coupAJouer())>0:
                                        print("k", end="  ")
                                elif ( self.getList()[x][y].get_CaseCouleur()=="vide"):
                                        print(".", end="  ")

        def pionEnPlus(self,couleur,nombre):
                if couleur=="noir":
                        self.__noir__ +=1
                else:
                        self.__rouge__ +=1
        
        def pionEnMoins(self,couleur,nombre):
                if couleur=="noir":
                        self.__rouge__ -=1
                else:
                        self.__noir__ -=1
        def couleurOppose(self,couleur):
                if couleur=="noir":
                        return "rouge"
                else:
                        return"noir"

        def PeutOnRetourner(self,couleur):
                couleurOppose=self.couleurOppose(couleur)
                self.__caseAJouer__=0
                for x in range(1,self.getnb()+1):
                        for y in range(1,self.getnb()+1):
                                self.getList()[x-1][y-1].get_coupAJouer().clear()
                                #en haut
                                if self.getList()[x-1][y-1].get_CaseCouleur()=="vide":
                                        if x>2:
                                                if self.getList()[x-2][y-1].get_CaseCouleur()==couleurOppose :
                                                        i=1
                                                        grandX=x-2
                                                        grandY=y-1
                                                        while True :
                                                                if grandX-i<0:
                                                                        break
                                                                elif self.getList()[grandX-i][grandY].get_CaseCouleur() == couleur:
                                                                        self.getList()[x-1][y-1].get_coupAJouer().append(("Haut",i))
                                                                        self.__caseAJouer__+=1
                                                                        break
                                                                elif self.getList()[grandX-i][grandY].get_CaseCouleur()==couleurOppose :
                                                                        i+=1
                                                                        
                                                                else:
                                                                        break
                                                
                                        #en bas
                                        if x<self.getnb()-1:
                                                if self.getList()[x][y-1].get_CaseCouleur()==couleurOppose    :
                                                        i=1
                                                        grandX=x
                                                        grandY=y-1
                                                        while True:
                                                                if grandX+i == self.getnb():
                                                                        break
                                                                elif self.getList()[grandX+i][grandY].get_CaseCouleur() == couleur:
                                                                        self.getList()[x-1][y-1].get_coupAJouer().append(("Bas",i))
                                                                        self.__caseAJouer__+=1
                                                                        break
                                                                elif self.getList()[grandX+i][grandY].get_CaseCouleur()==couleurOppose :
                                                                        i+=1
                                                                
                                                        
                                                                else:
                                                                        break

                                                        
                                        # a GAuche
                                        if y>2:
                                                
                                                if self.getList()[x-1][y-2].get_CaseCouleur()==couleurOppose :
                                                        i=1
                                                        grandX=x-1
                                                        grandY=y-2
                                                        while True:
                                                                if grandY-i < 0:
                                                                        break
                                                                elif self.getList()[grandX][grandY-i].get_CaseCouleur() == couleur:
                                                                        self.getList()[x-1][y-1].get_coupAJouer().append(("Gauche",i))
                                                                        self.__caseAJouer__+=1
                                                                        break
                                                                elif self.getList()[grandX][grandY-i].get_CaseCouleur()==couleurOppose :
                                                                        i+=1
                                                                
                                                        
                                                                else:
                                                                        break

                                        #A droite 
                                        if y< self.getnb()-1:
                                                if self.getList()[x-1][y].get_CaseCouleur()==couleurOppose :
                                                        i=1
                                                        grandX=x-1
                                                        grandY=y
                                                        while True:
                                                                if grandY+i ==self.getnb():
                                                                        break
                                                                elif self.getList()[grandX][grandY+i].get_CaseCouleur() == couleur:
                                                                        self.getList()[x-1][y-1].get_coupAJouer().append(("Droite",i))
                                                                        self.__caseAJouer__+=1
                                                                        break
                                                                elif self.getList()[grandX][grandY+i].get_CaseCouleur()==couleurOppose :
                                                                        i+=1
                                                                else:
                                                                        break

                                        ##en haut a  droite 
                                        if x>2 and y < self.getnb()-1:
                                                if self.getList()[x-2][y].get_CaseCouleur()==couleurOppose :
                                                        i=1
                                                        grandX=x-2
                                                        grandY=y
                                                        while True:
                                                                if  grandX-i<0  or grandY+i ==self.getnb():
                                                                        break
                                                                elif self.getList()[grandX-i][grandY+i].get_CaseCouleur() == couleur:
                                                                        self.getList()[x-1][y-1].get_coupAJouer().append(("Haut_Droite",i))
                                                                        self.__caseAJouer__+=1
                                                                        break
                                                                elif self.getList()[grandX-i][grandY+i].get_CaseCouleur()==couleurOppose :
                                                                        i+=1
                                                                else:
                                                                        break
                                        ##en bas a droite
                                        if x<self.getnb()-1 and y < self.getnb()-1 :  
                                                if self.getList()[x][y].get_CaseCouleur()==couleurOppose :
                                                        i=1
                                                        grandX=x
                                                        grandY=y
                                                        while True:
                                                                if  grandX+i==self.getnb()  or grandY+i ==self.getnb():
                                                                        break
                                                                elif self.getList()[grandX+i][grandY+i].get_CaseCouleur() == couleur:
                                                                        self.getList()[x-1][y-1].get_coupAJouer().append(("Bas_Droite",i))
                                                                        self.__caseAJouer__+=1
                                                                        break
                                                                elif self.getList()[grandX+i][grandY+i].get_CaseCouleur()==couleurOppose :
                                                                        i+=1
                                                                else:
                                                                        break

                                        ##en bas a gauche
                                        if x<self.getnb()-1 and y >2 :  
                                                if self.getList()[x][y-2].get_CaseCouleur()==couleurOppose :
                                                        i=1
                                                        grandX=x
                                                        grandY=y-2
                                                        while True:
                                                                if  grandX+i==self.getnb()  or grandY-i <0:
                                                                        break
                                                                elif self.getList()[grandX+i][grandY-i].get_CaseCouleur() == couleur:
                                                                        self.getList()[x-1][y-1].get_coupAJouer().append(("Bas_Gauche",i))
                                                                        self.__caseAJouer__+=1
                                                                        break
                                                                elif self.getList()[grandX+i][grandY-i].get_CaseCouleur()==couleurOppose :
                                                                        i+=1
                                                                else:
                                                                        break
                                        ##en haut a gauche
                                        if x>2 and y >2 :  
                                                if self.getList()[x-2][y-2].get_CaseCouleur()==couleurOppose :
                                                        i=1
                                                        grandX=x-2
                                                        grandY=y-2
                                                        while True:
                                                                if  grandX-i<0  or grandY-i <0:
                                                                        break
                                                                elif self.getList()[grandX-i][grandY-i].get_CaseCouleur() == couleur:
                                                                        self.getList()[x-1][y-1].get_coupAJouer().append(("Haut_Gauche",i))
                                                                        self.__caseAJouer__+=1
                                                                        break
                                                                elif self.getList()[grandX-i][grandY-i].get_CaseCouleur()==couleurOppose :
                                                                        i+=1
                                                                else:
                                                                        break




        
                

        def check(self,x,y,couleur):
                if x<1 or y<1 or x>self.getnb()or  y >self.getnb():
                        print("Oh cette case est hors limite")
                        return False
                elif  self.getList()[x-1][y-1].get_CaseCouleur()!="vide":
                        print("Oh cette case est deja occupé")
                        return False
                elif len(self.getList()[x-1][y-1].get_coupAJouer())==0:
                        print("Jouez ici ne retournera aucune piece adverse")
                        return False
                else:
                        return True    


      
        def retourner(self,x,y,couleur):
                for element in self.getList()[x-1][y-1].get_coupAJouer():
                        #en haut 
                        if element[0]=="Haut":
                                self.pionEnPlus(couleur,element[1])
                                self.pionEnMoins(couleur,element[1])
                                for z in range(element[1]):
                                        self.getList()[x-2-z][y-1].set_CaseCouleur(couleur)

                        #en bas
                        elif element[0]=="Bas":
                                self.pionEnPlus(couleur,element[1])
                                self.pionEnMoins(couleur,element[1])
                                for z in range(element[1]):
                                        self.getList()[x+z][y-1].set_CaseCouleur(couleur)
                        #A gauche
                        elif element[0]=="Gauche":
                                self.pionEnPlus(couleur,element[1])
                                self.pionEnMoins(couleur,element[1])
                                for z in range(element[1]):
                                        self.getList()[x-1][y-2-z].set_CaseCouleur(couleur)
                        #a droite
                        elif element[0]=="Droite":
                                self.pionEnPlus(couleur,element[1])
                                self.pionEnMoins(couleur,element[1])
                                for z in range(element[1]):
                                        self.getList()[x-1][y+z].set_CaseCouleur(couleur)
                        #en haut a droite 
                        elif element[0]=="Haut_Droite":
                                self.pionEnPlus(couleur,element[1])
                                self.pionEnMoins(couleur,element[1])
                                for z in range(element[1]):
                                        self.getList()[x-2-z][y+z].set_CaseCouleur(couleur)
                        #en bas a droite
                        elif element[0]=="Bas_Droite":
                                self.pionEnPlus(couleur,element[1])
                                self.pionEnMoins(couleur,element[1])
                                for z in range(element[1]):
                                        self.getList()[x+z][y+z].set_CaseCouleur(couleur)
                        #en bas a gauche
                        elif element[0]=="Bas_Gauche":
                                self.pionEnPlus(couleur,element[1])
                                self.pionEnMoins(couleur,element[1])
                                for z in range(element[1]):
                                        self.getList()[x+z][y-2-z].set_CaseCouleur(couleur)
                        #en haut a gauche
                        elif element[0]=="Haut_Gauche":
                                self.pionEnPlus(couleur,element[1])
                                self.pionEnMoins(couleur,element[1])
                                for z in range(element[1]):
                                        self.getList()[x-2-z][y-2-z].set_CaseCouleur(couleur)



        def ajouter(self,x,y,couleur):
                self.getList()[x-1][y-1].set_CaseCouleur(couleur)
                self.pionEnPlus(couleur,1)
                self.retourner(x,y,couleur)
        
        def annuler(self,x,y,couleur):
                couleurOppose= self.couleurOppose(couleur)
                self.getList()[x-1][y-1].set_CaseCouleur("vide")
                for element in self.getList()[x-1][y-1].get_coupAJouer():
                        #en haut 
                        if element[0]=="Haut":
                                self.pionEnPlus(couleurOppose,element[1])
                                self.pionEnMoins(couleurOppose,element[1])
                                for z in range(element[1]):
                                        self.getList()[x-2-z][y-1].set_CaseCouleur(couleurOppose)

                        #en bas
                        elif element[0]=="Bas":
                                self.pionEnPlus(couleurOppose,element[1])
                                self.pionEnMoins(couleurOppose,element[1])
                                for z in range(element[1]):
                                        self.getList()[x+z][y-1].set_CaseCouleur(couleurOppose)
                        #A gauche
                        elif element[0]=="Gauche":
                                self.pionEnPlus(couleurOppose,element[1])
                                self.pionEnMoins(couleurOppose,element[1])
                                for z in range(element[1]):
                                        self.getList()[x-1][y-2-z].set_CaseCouleur(couleurOppose)
                        #a droite
                        elif element[0]=="Droite":
                                self.pionEnPlus(couleurOppose,element[1])
                                self.pionEnMoins(couleurOppose,element[1])
                                for z in range(element[1]):
                                        self.getList()[x-1][y+z].set_CaseCouleur(couleurOppose)
                        #en haut a droite 
                        elif element[0]=="Haut_Droite":
                                self.pionEnPlus(couleurOppose,element[1])
                                self.pionEnMoins(couleurOppose,element[1])
                                for z in range(element[1]):
                                        self.getList()[x-2-z][y+z].set_CaseCouleur(couleurOppose)
                        #en bas a droite
                        elif element[0]=="Bas_Droite":
                                self.pionEnPlus(couleurOppose,element[1])
                                self.pionEnMoins(couleurOppose,element[1])
                                for z in range(element[1]):
                                        self.getList()[x+z][y+z].set_CaseCouleur(couleurOppose)
                        #en bas a gauche
                        elif element[0]=="Bas_Gauche":
                                self.pionEnPlus(couleurOppose,element[1])
                                self.pionEnMoins(couleurOppose,element[1])
                                for z in range(element[1]):
                                        self.getList()[x+z][y-2-z].set_CaseCouleur(couleurOppose)
                        #en haut a gauche
                        elif element[0]=="Haut_Gauche":
                                self.pionEnPlus(couleurOppose,element[1])
                                self.pionEnMoins(couleurOppose,element[1])
                                for z in range(element[1]):
                                        self.getList()[x-2-z][y-2-z].set_CaseCouleur(couleurOppose)






        def unGagnant(self):
                if self.getnoir()==0:
                        return True
                elif self.getrouge()==0:
                        return True
                else:
                        return False
        def quiEstLeGagnant(self):
                if self.getnoir()>self.getrouge():
                        print("Et le grand gagnant est le joueur 1 ")
                elif self.getnoir()<self.getrouge():
                        print("Et le grand gagnant est le joueur 2 ")
                else:
                        print("Nous avons une égalité")

     
                

                



        
   