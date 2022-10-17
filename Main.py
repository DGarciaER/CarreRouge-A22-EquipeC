from ControleurJeu import ControleurJeu, Mouvement
from functools import partial
import tkinter as tk
# import c31Geometry2 as c31

if __name__ == "__main__":

    # créer une fenetre tk avec un titre, un background et des dimensions
    root = tk.Tk()
    root.title("Carré Rouge")
    root.config(background="white")
    root.geometry("550x650")

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
    
    def test(e):
        
        cursorX = e.x
        cursorY = e.y
        
        if cursorX > 205 and cursorX < 245:
            if cursorY > 205 and cursorY < 245:
                    aireDeJeu.bind('<Motion>', test2)
                    

    # définir l'objet controleur
    jeu = ControleurJeu(aireDeJeu)
    
    def test2(e):
        cursorX = e.x
        cursorY = e.y
        
        # cette condition sert à verifier si la cursor est directement sur le carre rouge, si oui le jeu commence
        jeu.move(aireDeJeu,cursorX, cursorY)


    aireDeJeu.bind("<Button-1>", test)

    # créer un container des buttonset le mettre dans un grid en lui donnant du padding
    buttonsContainer = tk.Canvas(mainContainer, background="grey90")
    buttonsContainer.grid(column=1, row=2, padx=10, pady=15) # pour centrer et donner un padding

    # créer un button qui commence une nouvelle session et le mettre dans un grid en lui donnant du padding
    buttonNouvSession = tk.Button(buttonsContainer, text="Nouvelle Session", background="pink")
    buttonNouvSession.grid(column=1, row=1, padx=15)

    # créer un button qui affiche le menu score un nouveau jeu et le mettre dans un grid en lui donnant du padding
    buttonMenuScores = tk.Button(buttonsContainer, text="Menu Score", background="pink")
    buttonMenuScores.grid(column=2, row=1, padx=15, pady=15)

    # créer un button quitte du programme et le mettre dans un grid en lui donnant du padding
    buttonQuitter = tk.Button(buttonsContainer, text="Quitter", background="pink")
    buttonQuitter.grid(column=3, row=1, padx=15)
    
    # boocler la fenetre tk
    root.mainloop()