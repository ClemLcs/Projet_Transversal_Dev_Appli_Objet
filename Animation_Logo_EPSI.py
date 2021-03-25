from tkinter import *
import time
import os
root = Tk()

frames = [PhotoImage(file='./media/gif.gif',format = 'gif -index %i' %(i)) for i in range(21)]

def update(ind):
    try: 
        frame = frames[ind]
        ind += 1
        print(ind)
        label.configure(image=frame)
        root.after(100, update, ind)
       
    except:
        pass
    

label = Label(root, bg='#271748', width=1000, height=700)
label.pack()
root.after(0, update, 0)
root.mainloop()