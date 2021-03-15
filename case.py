class Case:
    def __init__(self,x,y,couleur) :
            self.__x__=x
            self.__y__=y
            self.__couleur__= couleur
            self.__coupAJouer=[]
    


    def get_CaseY(self):
        return self.__x__
    
    def get_coupAJouer(self):
        return self.__coupAJouer
    
    def get_CaseX(self):
        return self.__y__
    
    def get_CaseCouleur(self):
        return self.__couleur__

    def set_CaseCouleur(self,couleur):
        self.__couleur__=couleur 