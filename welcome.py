from tkinter import *

class Welcome():
    
    __fenetre__ = None
    __bouton_quitter__ = None

    #Constructeur
    def __init__(self):

        self.__fenetre__ = Tk()

        self.bouton_quitter()
        self.__fenetre__.mainloop()

    #Fonction qui permet de fermer le programme
    def bouton_quitter(self) :
        self.__bouton_quitter__= Button(self.__fenetre__, text='Quitter', command=self.__fenetre__.destroy)
        self.__bouton_quitter__.pack()



