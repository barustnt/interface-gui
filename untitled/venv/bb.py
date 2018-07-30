import os
import Tkinter
import tkMessageBox

Manager = Tkinter.Tk()

# Presentation du programme

presentation = Tkinter.Label(Manager, text='Mise en route du programme NetworkManager')
presentation.pack()


# Programme d'execution

def Network():
    ad = "su root -c /usr/sbin/NetworkManager"
    com = os.system(ad)
    tkMessageBox.showinfo("INFO", "Fonctionnement de Network")


# Creation du bouton Network

Bouton = Tkinter.Button(Manager, text='NetworkManager', command=Network, bg='yellow', fg='black')
Bouton.pack()
Manager.mainloop()