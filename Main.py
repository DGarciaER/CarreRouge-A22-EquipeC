from ControleurMenu import ControleurMenu
from ControleurJeu import ControleurJeu
from functools import partial
import tkinter as tk

if __name__ == "__main__":
    
    menu = ControleurMenu()

    # créer une fenetre tk avec un titre, un background et des dimensions
    root = tk.Tk()
    root.title("Carré Rouge - Menu")
    root.config(background="light blue")
    root.geometry("350x350")

    # créer un container et le centrer dans la fenetre tk
    container = tk.Frame(root, background="light blue")
    container.pack(pady=20) # pour centrer et donner un padding

    # créer un label menu et le mettre dans un grid en lui donnant du padding
    texte = tk.Label(container, text="Menu", background="light blue")
    texte.configure(font=("Bahnschrift", 25, "italic"))
    texte.grid(column=1, row=0, padx=10)

    # créer un button commencer un nouveau jeu et le mettre dans un grid en lui donnant du padding
    buttonNouveauJeu = tk.Button(container, text="Commencer Un Nouveau Jeu", background="pink", command=partial(menu.commencerJeu, container))
    buttonNouveauJeu.grid(column=1, row=1, padx=10, pady=15)

    # créer un button relancer une session ancienne et le mettre dans un grid en lui donnant du padding
    buttonRelancerSession = tk.Button(container, text="Relancer Une Session", background="pink", command=menu.relancerSession(container))
    buttonRelancerSession.grid(column=1, row=2, padx=10,)

    # boocler la fenetre tk
    root.mainloop()
