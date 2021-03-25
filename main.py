from tkinter import *
from Animation_Logo_EPSI import Animation_Logo_EPSI
import time

def main():
    root = Tk()
    fenetre = Animation_Logo_EPSI(root)
    root.resizable(width=False, height=False)
    root.mainloop()

main()