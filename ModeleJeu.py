import c31Geometry2 as c31

class CarreRouge:
    tailleCarreRouge = 40
    
    def __init__(self, container):
        """Dans cette méthode (constructeur du ModeleJeu), on initialiser les éléments de l'aire de jeu."""
        
        # initialisation du Carre Rouge
        self.carreRouge = c31.Carre(container, c31.Vecteur(225,225),self.tailleCarreRouge,0, '#ff0000', '#ff0000', 0)


class Rectangles:
    listeTaillesRectangles = [[60, 60], [60, 50], [30, 60], [100, 20]]
    
    def __init__(self, container):
        
        # initialisation des Rectangles (Pions)
        self.listeRectangles = [
                    c31.Rectangle(container, c31.Vecteur(100, 100), self.listeTaillesRectangles[0][0], self.listeTaillesRectangles[0][1], 0, '#0000ff', '#0000ff', 0),
                    c31.Rectangle(container, c31.Vecteur(300, 85), self.listeTaillesRectangles[1][0], self.listeTaillesRectangles[1][1], 0, '#0000ff', '#0000ff', 0),
                    c31.Rectangle(container, c31.Vecteur(85, 350), self.listeTaillesRectangles[2][0], self.listeTaillesRectangles[2][1], 0, '#0000ff', '#0000ff', 0),
                    c31.Rectangle(container, c31.Vecteur(355, 340), self.listeTaillesRectangles[3][0], self.listeTaillesRectangles[3][1], 0, '#0000ff', '#0000ff', 0)
                    ]

class Bordure:
    coteAirDeJeu = 450
    
    def __init__(self, container):
        
        # initialisation de la Bordure
        self.listeBordures = [
                    c31.Rectangle(container, c31.Vecteur(25, self.coteAirDeJeu/2), 50, 450, 0,'black','black',0),
                    c31.Rectangle(container, c31.Vecteur(425, self.coteAirDeJeu/2), 50, 450, 0,'black','black',0),
                    c31.Rectangle(container, c31.Vecteur(self.coteAirDeJeu/2, 25), 450, 50, 0,'black','black',0),
                    c31.Rectangle(container, c31.Vecteur(self.coteAirDeJeu/2, 425), 450, 50, 0,'black','black',0)
        ]