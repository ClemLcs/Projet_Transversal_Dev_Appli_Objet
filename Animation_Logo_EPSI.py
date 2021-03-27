from tkinter import *
import time
import os

class Animation_Logo_EPSI(object):
        
    #Constructeur
    def __init__(self, fenetre):
        
        self.fenetre = fenetre
            
        self.frames = [PhotoImage(file='./media/gif.gif',format = 'gif -index %i' %(i)) for i in range(21)]

        self.label = Label(self.fenetre, bg='#271748', width=1000, height=700)
        self.label.pack()
        try:
            self.fenetre.after(0, self.update, 0)
            epsi.bouton_quitter()
        except IndexError:
          print("Error found")

    #Fonction qui importe les frames du logo de l'epsi
    def update(self, ind):
        if ind == len(self.frames):
            raise IndexError
        else:
            if ind == 11:
                time.sleep(2)
            frame = self.frames[ind]
            ind += 1
            self.label.configure(image=frame)
            self.fenetre.after(100, self.update, ind)

    #Fonction qui permet de fermer le programme
    def bouton_quitter(self) :
        self.bouton_quitter = Button(self.fenetre, text='Quitter', command=self.fenetre.destroy)
        self.bouton_quitter.pack()

    #Définition des Getters
    @property
    def fenetre (self):
        return self.__fenetre

    @property
    def frames (self):
        return self.__frames

    @property
    def label (self):
        return self.__label

    @property
    def bouton_quitter (self):
        return self.__bouton_quitter

    #Définitons des Setters
    @fenetre.setter
    def fenetre(self, value):
        self.__fenetre = value

    @frames.setter
    def frames(self, value):
        self.__frames = value

    @label.setter
    def label(self, value):
        self.__label = value

    @bouton_quitter.setter
    def bouton_quitter(self, value):
        self.__bouton_quitter = value
    


    


