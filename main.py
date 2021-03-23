from tkinter import *
from Animation_Logo_EPSI import Animation_Logo_EPSI
import time

def main():
    root = Tk()
    fenetre = Animation_Logo_EPSI(root)
    fenetre.after(1)
    fenetre.after(2)
    fenetre.after(3)
    root.resizable(width=False, height=False)
    root.mainloop()

main()