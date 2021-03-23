from tkinter import *
import time
class Fenetre(object):
    
    #----------------

    def __init__(self, main):

        # Ajout de l'arrière plan
        self.canvas = Canvas(main, bg='#271549', width=1000, height=700)
        self.canvas.grid(row=0, column=0)

        # Listes des images
        self.my_images = []
        self.my_images.append(PhotoImage(file = "media/logo-0.png"))
        self.my_images.append(PhotoImage(file = "media/logo-10.png"))
        self.my_images.append(PhotoImage(file = "media/logo-20.png"))
        self.my_images.append(PhotoImage(file = "media/logo-30.png"))
        self.my_images.append(PhotoImage(file = "media/logo-40.png"))
        self.my_images.append(PhotoImage(file = "media/logo-50.png"))
        self.my_images.append(PhotoImage(file = "media/logo-60.png"))
        self.my_images.append(PhotoImage(file = "media/logo-70.png"))
        self.my_images.append(PhotoImage(file = "media/logo-80.png"))
        self.my_images.append(PhotoImage(file = "media/logo-90.png"))
        self.my_images.append(PhotoImage(file = "media/logo-100.png"))
        self.my_image_number = 0

        # Ajout de la première image
        self.image_on_canvas = self.canvas.create_image(100, 100, anchor = NW, image = self.my_images[self.my_image_number])

        # Ajout du bouton changer
        self.button = Button(main, text="Changer l'image", command=self.onButton)
        self.button.grid(row=1, column=0)


    def onButton(self):

        # image suivante
        self.my_image_number += 1

        # retourne la première image
        if self.my_image_number == len(self.my_images):
            self.my_image_number = 0

        # Change l'image
        self.canvas.itemconfig(self.image_on_canvas, image = self.my_images[self.my_image_number])




        
            
            


        



