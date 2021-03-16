from tkinter import *
class Fenetre():
    
    __fenetre__ = None
    __form_arriere_plan__ = None
    __image_epsi__ = None
    __bouton_quitter__ = None

    #Constructeur
    def __init__(self):

        #Configuration de la fenêtre
        self.__fenetre__ = Tk()
        form_arriere_plan = Canvas(self.__fenetre__,bg='#271549',height=700,width=1000)

        #Ajout du logo Epsi
        self.import_logo_epsi()
        self.add_logo_epsi(form_arriere_plan)

        #Ajout du bouton quitter
        self.bouton_quitter()
        self.__fenetre__.mainloop()

    #Fonction qui permet de fermer le programme
    def bouton_quitter(self) :
        self.__bouton_quitter__= Button(self.__fenetre__, text='Quitter', command=self.__fenetre__.destroy)
        self.__bouton_quitter__.pack()

    #Fonction qui importe le logo de l'epsi
    def import_logo_epsi(self):
        self.__image_epsi__ = PhotoImage(file="media/logo.png")
 
    #Fonction qui ajoute  à l'écran le logo de l'epsi
    def add_logo_epsi(self, form1):
        form1.create_image(500, 400, image = self.__image_epsi__)
        form1.pack()

        



