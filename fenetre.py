from tkinter import *
from pil import Image, ImageTk

class Fenetre():
    
    __fenetre__ = None
    __bouton_quitter__ = None
    __image_epsi__ = None

    #Constructeur
    def __init__(self):

        self.__fenetre__ = Tk()

        self.import_logo_epsi()

        self.bouton_quitter()
        self.__fenetre__.mainloop()

    #Fonction qui permet de fermer le programme
    def bouton_quitter(self) :
        self.__bouton_quitter__= Button(self.__fenetre__, text='Quitter', command=self.__fenetre__.destroy)
        self.__bouton_quitter__.pack()

    #Fonction qui importe le logo de l'epsi
    def import_logo_epsi(self):
        self.__image_epsi__ = Image.open()



