from sqlite3 import Time
from tkinter import simpledialog
from ControleurJeu import ControleurJeu
from functools import partial
import tkinter as tk
import csv
# import c31Geometry2 as c31


if __name__ == "__main__":

    scores = []

    # créer une fenetre tk avec un titre, un background et des dimensions
    couleurTheme = "#FFE299"
    root = tk.Tk()
    root.title("Carré Rouge")
    root.config(background= couleurTheme)
    root.geometry("550x660")

    # créer un containter et le centrer dans la fenetre tk
    mainContainer = tk.Frame(root, background= couleurTheme)
    mainContainer.pack(pady=20) # pour centrer et donner un padding
    
    # créer un titre de jeu et le mettre dans un grid en lui donnant du padding
    titre = tk.Label(mainContainer, text="Carré Rouge", background= couleurTheme)
    titre.configure(font=("Comic Sans MS", 25, "bold"))
    titre.grid(column=1, row=0, padx=10)
                    
    # créer l'aire de jeu et le mettre dans un grid en lui donnant du padding
    aireDeJeu = tk.Canvas(mainContainer, height=450, width=450, background="grey90", highlightthickness=0)
    aireDeJeu.grid(column=1, row=1, padx=20, pady=10) # pour centrer et donner un padding
    
    # # définir l'objet controleur
    jeu = ControleurJeu(aireDeJeu)
    
    def askUsername():
        jeu.setUsername(simpledialog.askstring("'Ok' = Enregistrer    'Cancel' = Pas Enregistrer", "                                                  Entrer votre nom                                                  "))
        if jeu.username == None:
            pass
        else:
            jeu.openCSV(jeu.listScore, jeu.username)
            jeu.listScore.clear()

    def askUsernameQuit():
        jeu.setUsername(simpledialog.askstring("'Ok' = Enregistrer et Quitter   'Cancel' = Pas Enregistrer et Quitter", "                                                                    Entrer votre nom                                                                    "))
        if jeu.username == None:
            root.quit()
        else:
            jeu.openCSV(jeu.listScore, jeu.username)
            root.quit()

    def AfficherScores():
        with open("score.csv",'r') as r:
            obj = csv.reader(r, delimiter="\n")
            for i in obj:
                ligne = i
                scores.append(ligne)
        r.close()

        for i in scores:
            i[0] = i[0].split('\n')
            i[0][1] = i[0][1][3:-2]
            i[0][1] = i[0][1].split(', ')
            print(i[0][0])
            for j in i[0][1]:
                print('\t' + j)

        
    jeu.create_widgets(mainContainer)


    # créer un container des buttonset le mettre dans un grid en lui donnant du padding
    buttonsContainer = tk.Canvas(mainContainer, background= couleurTheme, highlightthickness=0)
    buttonsContainer.grid(column=1, row=3, padx=10) # pour centrer et donner un padding

    couleutButtons = "#C6D4FF"

    # créer un button qui commence une nouvelle session et le mettre dans un grid en lui donnant du padding
    buttonNouvSession = tk.Button(buttonsContainer, text="Nouvelle Session", background= couleutButtons, command=askUsername)
    buttonNouvSession.grid(column=1, row=1, padx=15)

    # créer un button qui affiche le menu score un nouveau jeu et le mettre dans un grid en lui donnant du padding
    buttonMenuScores = tk.Button(buttonsContainer, text="Menu Score", background= couleutButtons, command=AfficherScores)
    buttonMenuScores.grid(column=2, row=1, padx=15, pady=15)

    # créer un button quitte du programme et le mettre dans un grid en lui donnant du padding
    buttonQuitter = tk.Button(buttonsContainer, text="Quitter", background= couleutButtons, command=askUsernameQuit)
    buttonQuitter.grid(column=3, row=1, padx=15)
    
    # boocler la fenetre tk
    root.mainloop()