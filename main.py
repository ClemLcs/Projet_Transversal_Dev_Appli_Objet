from tkinter import *
from fenetre import Fenetre
import time

def main():
    
 
    #fen = Tk()
 
    #can = Canvas(fen, bg='#271549',height=700,width=1000)
    #can.pack(side='top', fill='both', expand='yes')
    #photo = PhotoImage(file="media/logo-epsi-gif.gif")
    #can.create_image(0,0,anchor='nw', image=photo)
 
    #for ind in range(10):
    #    photo.configure(format="gif -index " + str(ind))
    #    can.update_idletasks()
 
    #fen.mainloop()

    #Fenetre()

    class MainWindow():

        #----------------

        def __init__(self, main):

            # canvas for image
            self.canvas = Canvas(main, bg='#271549', width=1000, height=700)
            self.canvas.grid(row=0, column=0)

            
            

            # set first image on canvas
            self.image_on_canvas = self.canvas.create_image(100, 100, anchor = NW, image = self.my_images[self.my_image_number])

            # button to change image
            #for element in range(len(self.my_images)):
            #    self.onButton
            #    time.sleep(1)

            self.button = Button(main, text="Change", command=self.onButton)
            self.button.grid(row=1, column=0)

        #----------------

        def onButton(self):

            print(self.my_images[self.my_image_number])

            # next image
            self.my_image_number += 1

            # return to first image
            if self.my_image_number == len(self.my_images):
                self.my_image_number = 0

            # change image
            self.canvas.itemconfig(self.image_on_canvas, image = self.my_images[self.my_image_number])

        #----------------------------------------------------------------------

    root = Tk()
    Fenetre(root)
    root.resizable(width=False, height=False)
    root.mainloop()
main()