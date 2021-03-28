from tkinter import *
from Animation_Introduction import Animation_Introduction
import time
import os
from partie import *  


def main():

    root = Tk()
    Animation_Introduction(root)
    root.mainloop()
    
    lancetapartie = Partie()
    lancetapartie.quelEstLeTypeDePartie()
    lancetapartie.laPartie()

main()
