import c31Geometry2 as c31

class CarreRouge:
    tailleCarreRouge = 40
    
    def __init__(self, container):
        """Dans cette méthode (constructeur du ModeleJeu), on initialiser les éléments de l'aire de jeu."""
        
        # initialisation du Carre Rouge
        couleur = '#ed4242'
        self.carreRouge = c31.Carre(container, c31.Vecteur(225,225),self.tailleCarreRouge,0, couleur, couleur, 0)


class Rectangles:
    listeTaillesRectangles = [[60, 60], [60, 50], [30, 60], [100, 20]]
    
    def __init__(self, container):
        
        # initialisation des Rectangles (Pions)
        couleur = '#2c67f2'
        self.listeRectangles = [
                    c31.Rectangle(container, c31.Vecteur(0, 0), self.listeTaillesRectangles[0][0], self.listeTaillesRectangles[0][1], 0, couleur, couleur, 0),  #rectangle haut gauche
                    c31.Rectangle(container, c31.Vecteur(0, 0), self.listeTaillesRectangles[1][0], self.listeTaillesRectangles[1][1], 0, couleur, couleur, 0),   #rectange haut droite
                    c31.Rectangle(container, c31.Vecteur(0, 0), self.listeTaillesRectangles[2][0], self.listeTaillesRectangles[2][1], 0, couleur, couleur, 0),   #rectange bas gauche
                    c31.Rectangle(container, c31.Vecteur(0, 0), self.listeTaillesRectangles[3][0], self.listeTaillesRectangles[3][1], 0, couleur, couleur, 0)   #rectange bas droite
                    ]

class Bordure:
    coteAirDeJeu = 450
    listeTaillesBordure = [[50, 450], [50, 450], [450, 50], [450, 50]]
    
    def __init__(self, container):
        
        # initialisation de la Bordure
        couleur = '#1b1b1c'
        self.listeBordures = [
                    c31.Rectangle(container, c31.Vecteur(25, self.coteAirDeJeu/2), self.listeTaillesBordure[0][0], self.listeTaillesBordure[0][1], 0,couleur, couleur, 0),   #bordure gauche
                    c31.Rectangle(container, c31.Vecteur(425, self.coteAirDeJeu/2), self.listeTaillesBordure[1][0], self.listeTaillesBordure[1][1], 0,couleur, couleur, 0),  #bordure droite
                    c31.Rectangle(container, c31.Vecteur(self.coteAirDeJeu/2, 25), self.listeTaillesBordure[2][0], self.listeTaillesBordure[2][1], 0,couleur, couleur, 0),   #bordure haut
                    c31.Rectangle(container, c31.Vecteur(self.coteAirDeJeu/2, 425), self.listeTaillesBordure[3][0], self.listeTaillesBordure[3][1], 0,couleur, couleur, 0)   #bordure bas
        ]