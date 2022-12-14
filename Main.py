from cProfile import label
from sqlite3 import Time
from tkinter import Button, Label, Toplevel, simpledialog
from tkinter import *
from ControleurJeu import ControleurJeu
from functools import partial
import tkinter as tk
import csv
# import c31Geometry2 as c31


if __name__ == "__main__":

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
        """Fonction pour demander le nom de lutilisateur. Cette fonctione est appelle lorsque lutilisateur clique sur nouvelle session ou quitter"""
        #simpledialog demande le nom a lutilisateur
        jeu.setUsername(simpledialog.askstring("Save", "Entrer votre nom pour enregistrer"))
        #si il clique sur annuler, rien ne se passe
        if jeu.username == None:
            pass
        elif jeu.username == "\n":
            jeu.listScore = []
        else:
            if len(jeu.listScore) != 0:
                jeu.openCSV(jeu.listScore, jeu.username)
                jeu.listScore = []

    def askUsernameQuit():
        """fonction pour demander le nom de lutilisateur lorsque lon quitte le jeu (clique sur quitter)"""
        jeu.setUsername(simpledialog.askstring("Save", "Entrer votre nom pour enregistrer"))
        if jeu.username == None:
            pass
        elif jeu.username == "\n":
            #fonction pour quitter le tkinter
            root.quit()
        else:
            if len(jeu.listScore) != 0:
                jeu.openCSV(jeu.listScore, jeu.username)
                root.quit()

    def AfficherScores():
        """Fonction pour afficher les scores """
        
        #creation du widget
        fenetreScore = tk.Tk()
        fenetreScore.title("Scores")
        fenetreScore.geometry("400x400")
        buttonsContainerAlignement = tk.Canvas(fenetreScore, highlightthickness=0)
        buttonsContainerAlignement.pack() # pour centrer et donner un padding
        scoresLabel = Label(buttonsContainerAlignement, text="LES SCORES :")
        scoresLabel.grid(column=1,row=1,padx=15)
        buttonExit = Button(buttonsContainerAlignement, text="Retour",command=fenetreScore.destroy)
        buttonSuppimer = Button(buttonsContainerAlignement, text="Supprimer scores",command=deleteScore)
        buttonExit.grid(column=2, row=1,padx=15)
        buttonSuppimer.grid(column=3, row=1, padx=15)
        scrollbar = Scrollbar(fenetreScore)
        scrollbar.pack( side = RIGHT, fill = Y )
        canvascore = Listbox(fenetreScore, yscrollcommand = scrollbar.set )
        

        canvascore.pack( side = LEFT, fill = BOTH, padx= 50 )
        scrollbar.config( command = canvascore.yview )

        
        
        scores = []  # creation du tableau scores   

        #ouverture du fichier CSV
        with open("score.csv",'r') as r:
            obj = csv.reader(r, delimiter="\n")
            for i in obj:
                ligne = i
                scores.append(ligne)
        r.close()
        
        if not scores == [[]]:  #si le tableau dans le tableau principal est vide
            for i in scores:
                i[0] = i[0].split('\n')
                i[0][1] = i[0][1][3:-2]
                i[0][1] = i[0][1].split(', ')  #Affiche les prenoms
                canvascore.insert(END, i[0][0])
                for j in i[0][1]:
                    canvascore.insert(END, j)

        

    def deleteScore():
        """Fonction pour supprimer les scores """
        
        f = open("score.csv", "w")
        f.truncate()
        f.close()
        
    jeu.create_widget(mainContainer)

    # créer un container des buttonset le mettre dans un grid en lui donnant du padding
    buttonsContainer = tk.Canvas(mainContainer, background= couleurTheme, highlightthickness=0)
    buttonsContainer.grid(column=1, row=3, padx=10) # pour centrer et donner un padding

    couleutButtons = "#EE95A6"

    # créer un button qui commence une nouvelle session et le mettre dans un grid en lui donnant du padding
    buttonNouvSession = tk.Button(buttonsContainer, text="  Nouvelle Session  ", background= couleutButtons, command=askUsername)
    buttonNouvSession.grid(column=1, row=1, padx=15)

    # créer un button qui affiche le menu score un nouveau jeu et le mettre dans un grid en lui donnant du padding
    buttonMenuScores = tk.Button(buttonsContainer, text="  Menu Score  ", background= couleutButtons, command=AfficherScores)
    buttonMenuScores.grid(column=2, row=1, padx=15, pady=15)

    # créer un button quitte du programme et le mettre dans un grid en lui donnant du padding
    buttonQuitter = tk.Button(buttonsContainer, text="  Quitter  ", background= couleutButtons, command=askUsernameQuit)
    buttonQuitter.grid(column=3, row=1, padx=15)
    
    # boocler la fenetre tk
    root.mainloop()