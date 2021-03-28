class Case(object):
    #Constructeur
    def __init__(self,x,y,couleur) :
        # Chaque case a comme attributs ses coordonées  x et y sa couleur qui est soit noir , soit blanc ou soit vide 
        # et sa liste coupJouable qui definit  si lorsque l'utilisateur joue sur cette case cela permettra de retourner un pion adverse

            self.__x=x
            self.__y=y
            self.__couleur= couleur
            self.__coupJouable=[]

    # Définition du Getter
    @property
    def x(self):
        return self.__x
    
    @property
    def coupJouable(self):
        return self.__coupJouable
    
    # Définition des setters
    @property
    def y(self):
        return self.__y

    @property
    def couleur(self):
        return self.__couleur
    
    
    @couleur.setter
    def couleur(self,value):
        self.__couleur= value
