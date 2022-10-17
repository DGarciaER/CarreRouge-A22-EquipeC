from tkinter import Canvas
import c31Geometry2 as c31


class ModeleJeu:

    tailleCarreRouge = 40
    coteAirDeJeu = 450

    """Dans cette méthode (constructeur du ModeleJeu), on initialiser les éléments de l'aire de jeu."""
    def __init__(self, container):
        
        # initialisation du Carre carreRouge
        self.carreRouge = c31.Carre(container, c31.Vecteur(225,225),self.tailleCarreRouge,0, '#ff0000', '#ff0000', 0)
        
        # initialisation du Rectangle rectangleBleuGauche
        self.rectangleBleuGauche = c31.Rectangle(container, c31.Vecteur(100, 100), 60, 60, 0, '#0000ff', '#0000ff', 0)
        
        # initialisation du Rectangle rectangleBleuSupDroit
        self.rectangleBleuSupDroit = c31.Rectangle(container, c31.Vecteur(300, 85), 60, 50, 0, '#0000ff', '#0000ff', 0)
        
        # initialisation du Rectangle rectangleBleuInfGauche
        self.rectangleBleuInfGauche = c31.Rectangle(container, c31.Vecteur(85, 350), 30, 60, 0, '#0000ff', '#0000ff', 0)
        
        # initialisation du Rectangle rectangleBleuInfDroit
        self.rectangleBleuInfDroit = c31.Rectangle(container, c31.Vecteur(355, 340), 100, 20, 0, '#0000ff', '#0000ff', 0)
        
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
        self.rectangleBleuGauche.draw()

    """Cette méthode affiche le rectangle bleuSupDroit."""
    def afficher_rectangleBleuSupDroit(self):
        self.rectangleBleuSupDroit.draw()

    """Cette méthode affiche le rectangle bleuInfGauche."""
    def afficher_rectangleBleuInfGauche(self):
        self.rectangleBleuInfGauche.draw()

    """Cette méthode affiche le rectangle bleuInfDroit."""
    def afficher_rectangleBleuInfDroit(self):
        self.rectangleBleuInfDroit.draw()

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