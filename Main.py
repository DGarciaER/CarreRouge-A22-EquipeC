from sqlite3 import Time
from tkinter import simpledialog
from ControleurJeu import ControleurJeu
from functools import partial
import tkinter as tk
# import c31Geometry2 as c31


if __name__ == "__main__":

    

    # créer une fenetre tk avec un titre, un background et des dimensions
    couleurTheme = "#FFE299"
    root = tk.Tk()
    root.title("Carré Rouge")
    root.config(background= couleurTheme)
    root.geometry("550x800")

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
        jeu.setUsername(simpledialog.askstring('Username', 'Entrez votre prenom: '))
        jeu.openCSV(jeu.listScore, jeu.username)
        jeu.listScore.clear()

    def askUsernameQuit():
        jeu.setUsername(simpledialog.askstring('Username', 'Entrez votre prenom: '))
        jeu.openCSV(jeu.listScore, jeu.username)
        root.quit()

    # créer un container des buttonset le mettre dans un grid en lui donnant du padding
    buttonsContainer = tk.Canvas(mainContainer, background= couleurTheme)
    buttonsContainer.grid(column=1, row=2, padx=10, pady=15) # pour centrer et donner un padding

    couleutButtons = "#C6D4FF"

    # créer un button qui commence une nouvelle session et le mettre dans un grid en lui donnant du padding
    buttonNouvSession = tk.Button(buttonsContainer, text="Nouvelle Session", background= couleutButtons, command=askUsername)
    buttonNouvSession.grid(column=1, row=1, padx=15)

    # créer un button qui affiche le menu score un nouveau jeu et le mettre dans un grid en lui donnant du padding
    buttonMenuScores = tk.Button(buttonsContainer, text="Menu Score", background= couleutButtons)
    buttonMenuScores.grid(column=2, row=1, padx=15, pady=15)

    # créer un button quitte du programme et le mettre dans un grid en lui donnant du padding
    buttonQuitter = tk.Button(buttonsContainer, text="Quitter", background= couleutButtons, command=askUsernameQuit)
    buttonQuitter.grid(column=3, row=1, padx=15)
    
    # boocler la fenetre tk
    root.mainloop()