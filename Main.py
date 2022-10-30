from cProfile import label
from curses import newwin
from tkinter import simpledialog
from ControleurJeu import ControleurJeu
from functools import partial
import time
import tkinter as tk
from tkinter import *

# import c31Geometry2 as c31

if __name__ == "__main__":
    '''
    Le main du projet (...)
    '''

    # créer une fenetre tk avec un titre, un background et des dimensions
    root = tk.Tk()
    root.title("Carré Rouge")
    root.config(background="white")
    root.geometry("550x800")

    # créer un containter et le centrer dans la fenetre tk
    mainContainer = tk.Frame(root, background="light blue")
    mainContainer.pack(pady=20) # pour centrer et donner un padding
    
    # créer un titre de jeu et le mettre dans un grid en lui donnant du padding
    titre = tk.Label(mainContainer, text="Carré Rouge", background="light blue")
    titre.configure(font=("Bahnschrift", 25, "italic"))
    titre.grid(column=1, row=0, padx=10)
                    
    # créer l'aire de jeu et le mettre dans un grid en lui donnant du padding
    aireDeJeu = tk.Canvas(mainContainer, height=450, width=450, background="grey90")
    aireDeJeu.grid(column=1, row=1, padx=20, pady=10) # pour centrer et donner un padding
    
    # # définir l'objet controleur
    jeu = ControleurJeu(aireDeJeu)

    #créer le label pour le chronometre
    # stopwatch_label = tk.Label(mainContainer, text="00:0000 ", font=("Bahnschrift", 15, "italic"))
    # stopwatch_label.grid(column=1, row=2)

    # créer un container des buttonset le mettre dans un grid en lui donnant du padding
    buttonsContainer = tk.Canvas(mainContainer, background="grey90")
    buttonsContainer.grid(column=1, row=3, padx=10, pady=15) # pour centrer et donner un padding

    # créer un button qui commence une nouvelle session et le mettre dans un grid en lui donnant du padding
    buttonNouvSession = tk.Button(buttonsContainer, text="Nouvelle Session", background="pink")
    buttonNouvSession.grid(column=1, row=1, padx=15)

    # créer un button qui affiche le menu score un nouveau jeu et le mettre dans un grid en lui donnant du padding
    buttonMenuScores = tk.Button(buttonsContainer, text="Menu Score", background="pink")
    buttonMenuScores.grid(column=2, row=1, padx=15, pady=15)

    def create():
        newWindow = tk.Toplevel(root, background='pink')
        newWindow.geometry("300x300")
        labelExample = tk.Label(newWindow, text = "Prenom:")
        labelExample.pack(side=LEFT)
        nom = Entry(newWindow, bd=5)
        nom.pack(side=RIGHT)
        #labelScore = tk.Label(newWindow, text = jeu.temp)
        #labelScore.pack(side=BOTTOM)
        buttonOK = tk.Button(newWindow, text="OK", command=root.quit)
        buttonOK.pack()

    def askUsername():
        jeu.setUsername(simpledialog.askstring("Username", "Entrez votre nom:"))
        jeu.openCSV(jeu.listScore, jeu.username)
        root.quit()

    # créer un button quitte du programme et le mettre dans un grid en lui donnant du padding
    buttonQuitter = tk.Button(buttonsContainer, text="Quitter", background="pink", command=askUsername)
    buttonQuitter.grid(column=3, row=1, padx=15)
   
    
    
    
    # boocler la fenetre tk
    root.mainloop()