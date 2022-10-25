from tkinter import Canvas
import tkinter as tk
import c31Geometry2 as c31


class ModeleJeu:
    
    '''
    Classe pour le la partie "Modèle" du modèle MVC (Model-View-Controller)
    '''

    tailleCarreRouge = 40
    coteAirDeJeu = 450

    """Dans cette méthode (constructeur du ModeleJeu), on initialiser les éléments de l'aire de jeu."""
    def __init__(self, container):
        
        # initialisation du Carre carreRouge
        self.carreRouge = c31.Carre(container, c31.Vecteur(225,225),self.tailleCarreRouge,0, '#ff0000', '#ff0000', 0)
        
        self.listT = [[60, 60], [60, 50], [30, 60], [100, 20]]
        
        self.listeRectangles = [
                           c31.Rectangle(container, c31.Vecteur(100, 100), self.listT[0][0], self.listT[0][1], 0, '#0000ff', '#0000ff', 0),
                           c31.Rectangle(container, c31.Vecteur(300, 85), self.listT[1][0], self.listT[1][1], 0, '#0000ff', '#0000ff', 0),
                           c31.Rectangle(container, c31.Vecteur(85, 350), self.listT[2][0], self.listT[2][1], 0, '#0000ff', '#0000ff', 0),
                           c31.Rectangle(container, c31.Vecteur(355, 340), self.listT[3][0], self.listT[3][1], 0, '#0000ff', '#0000ff', 0)
                           ]
        
        # initialisation du Rectangle leftBorder
        self.leftBorder = c31.Rectangle(container, c31.Vecteur(25, self.coteAirDeJeu/2), 50, 450, 0,'black','black',0)

        # initialisation du Rectangle rightBorder
        self.rightBorder = c31.Rectangle(container, c31.Vecteur(425, self.coteAirDeJeu/2), 50, 450, 0,'black','black',0)          
 
        # initialisation du Rectangle topBorder
        self.topBorder = c31.Rectangle(container, c31.Vecteur(self.coteAirDeJeu/2, 25), 450, 50, 0,'black','black',0)     

        # initialisation du Rectangle bottomBorder
        self.bottomBorder = c31.Rectangle(container, c31.Vecteur(self.coteAirDeJeu/2, 425), 450, 50, 0,'black','black',0)

    """Cette méthode affiche le carré rouge."""
    def afficher_carreRouge(self):
        self.carreRouge.draw()
        # cette fonctionnalité permet de déplacer carreRouge lorsque le boutton gauche de la souris est appuyé
        # self.carreRouge.bind("<B1-Motion>", move)

    """Cette méthode affiche le rectangle bleuGauche."""
    def afficher_rectangleBleuGauche(self):
        self.listeRectangles[0].draw()

    """Cette méthode affiche le rectangle bleuSupDroit."""
    def afficher_rectangleBleuSupDroit(self):
        self.listeRectangles[1].draw()

    """Cette méthode affiche le rectangle bleuInfGauche."""
    def afficher_rectangleBleuInfGauche(self):
        self.listeRectangles[2].draw()

    """Cette méthode affiche le rectangle bleuInfDroit."""
    def afficher_rectangleBleuInfDroit(self):
        self.listeRectangles[3].draw()

    """Cette méthode affiche le rectangle leftBorder."""
    def afficher_leftBorder(self):
        self.leftBorder.draw()

    """Cette méthode affiche le rectangle rightBorder."""
    def afficher_rightBorder(self):
        self.rightBorder.draw()

    """Cette méthode affiche le rectangle topBorder."""
    def afficher_topBorder(self):
        self.topBorder.draw()

    """Cette méthode affiche le rectangle bottomBorder."""
    def afficher_bottomBorder(self):
        self.bottomBorder.draw()
        
    def stopwatch(self):
        stopwatch_label = tk.Label(text="00:00:00", font=("Bahnschrift", 25, "italic"))
        pass    