from partie import *  
from tkinter import *
from Animation_Introduction import Animation_Introduction

def main():

    root = Tk()
    Animation_Introduction(root)
    root.after(17000, lambda: root.destroy())
    root.mainloop()
    
    lancetapartie = Partie() # Création de l'objet
    lancetapartie.quelEstLeTypeDePartie() # Choix des paramètres de partie
    lancetapartie.laPartie() # Lancement de la partie

main()
