class Case:
    def __init__(self,x,y,couleur) :
            self.__x=x
            self.__y=y
            self.__couleur= couleur
            self.__coupAJouer=[]
    
    @property
    def x(self):
        return self.coords[0]

    @property
    def x(self):
        return self.__x
    
    @property
    def coupAJouer(self):
        return self.__coupAJouer
    
    @property
    def y(self):
        return self.__y

    @property
    def couleur(self):
        return self.__couleur
    
    
    @couleur.setter
    def couleur(self,value):
        self.__couleur= value