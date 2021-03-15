#######Importations des fonctions########

from tkinter import *
from random import * #pour la génération aléatoire des pions

#######Définition des fonctions##########
def cercle(x, y, r, coul ='red'):#pour le dessin des pions
    "tracé d'un cercle de centre (x,y) et de rayon r"
    can.create_oval(x-r, y-r, x+r, y+r, fill=coul)
    
def remplir(y):#calcul des coord de la ligne
    x=0
    liste=[]
    while x<200:
        liste.append([x,y,x+20,y+20])
        x=x+20
    return liste
def pointeur(event):
    """Dessine un pion la ou l'utilisateur a cliqué"""
    if event.x>100 and event.y>100 and event.x<500 and event.y<500:
        x=event.x%50
        x=(event.x-x)+25
        y=event.y%50
        y=(event.y-y)+25
        cercle(x,y,15,'black')
def changerletext(letext,tag):
    can.itemconfigure(tag, text = letext)



fen = Tk()
can = Canvas(fen, width =600, height =600, bg ='green')
can.pack(side =TOP, padx =30, pady =30)
can.create_rectangle(100,100,500,500,fill="white")
can.create_text(80,80 , fill="blue" , tag="titre",text="voila le titre")

ecart=400/8
y=100
i=1
# while 100+x<=500:
#     can.create_line(100+x,100,100+x,500)
#     can.create_line(100,100+x,500,100+x)
#     can.create_text(75+x,90,text=i)
#     can.create_text(90,75+x,text=i)
#     x +=ecart
#     i +=1
while y<500:
    can.create_text(80,y+(ecart/2),text=i)
    can.create_text(100+(ecart*i)-ecart/2,80,text=i)
    i+=1
    x=100
    while x<500:
        rectangle= can.create_rectangle(x,y,x+ecart,y+ecart)
        print(type(rectangle))
        x+=ecart
    y+=ecart

can.bind("<Button-1>", pointeur)


fen.mainloop()