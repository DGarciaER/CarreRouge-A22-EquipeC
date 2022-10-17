from tkinter import Canvas
import c31Geometry2 as c31


class ModeleJeu:

    tailleCarreRouge = 40
    coteAirDeJeu = 450

    def __init__(self, container):
        
        self.carreRouge = c31.Carre(container, c31.Vecteur(225,225),self.tailleCarreRouge,0, '#ff0000', '#ff0000', 0)
        
        self.rectangleBleuGauche = c31.Rectangle(container, c31.Vecteur(100, 100), 60, 60, 0, '#0000ff', '#0000ff', 0)
        
        self.rectangleBleuSupDroit = c31.Rectangle(container, c31.Vecteur(300, 85), 60, 50, 0, '#0000ff', '#0000ff', 0)
        
        self.rectangleBleuInfGauche = c31.Rectangle(container, c31.Vecteur(85, 350), 30, 60, 0, '#0000ff', '#0000ff', 0)
        
        self.rectangleBleuInfDroit = c31.Rectangle(container, c31.Vecteur(355, 340), 100, 20, 0, '#0000ff', '#0000ff', 0)
        
        self.leftBorder = c31.Rectangle(container, c31.Vecteur(25, self.coteAirDeJeu/2), 50, 450, 0,'black','black',0)

        self.rightBorder = c31.Rectangle(container, c31.Vecteur(425, self.coteAirDeJeu/2), 50, 450, 0,'black','black',0)          
 
        self.topBorder = c31.Rectangle(container, c31.Vecteur(self.coteAirDeJeu/2, 25), 450, 50, 0,'black','black',0)     

        self.bottomBorder = c31.Rectangle(container, c31.Vecteur(self.coteAirDeJeu/2, 425), 450, 50, 0,'black','black',0)

    #methode pour creer le rcare rouge
    def afficher_carreRouge(self):
        self.carreRouge.draw()
        # cette fonctionnalité permet de déplacer carreRouge lorsque le boutton gauche de la souris est appuyé
        # self.carreRouge.bind("<B1-Motion>", move)

    #methode pour creer rectangle bleuGauche
    def afficher_rectangleBleuGauche(self):
        self.rectangleBleuGauche.draw()

    #methode pour creer rectangle bleuSupDroit
    def afficher_rectangleBleuSupDroit(self):
        self.rectangleBleuSupDroit.draw()

    #methode pour creer rectangle bleuInfGauche
    def afficher_rectangleBleuInfGauche(self):
        self.rectangleBleuInfGauche.draw()

    #methode pour creer rectangle bleuInfDroit
    def afficher_rectangleBleuInfDroit(self):
        self.rectangleBleuInfDroit.draw()

    #methode pour afficher leftBorder
    def afficher_leftBorder(self):
        self.leftBorder.draw()

    #methode pour afficher rightBorder
    def afficher_rightBorder(self):
        self.rightBorder.draw()

    #methode pour afficher topBorder
    def afficher_topBorder(self):
        self.topBorder.draw()

    #methode pour afficher bottomBorder
    def afficher_bottomBorder(self):
        self.bottomBorder.draw()


    
    #TODO faut-il deplacer cette methode dans une classe specifique au carreRouge? pareil pour les autres methodes d'initialisation..?

    # cette methode permet au carreRouge de se deplacer vers la gauche a l'écran
    #TODO ajuster la valeur de deplacement (réduire pour que l'on voit plus précisement ou se trouve le carre)
    def left(e):
        x = -20
        y = 0
        airJeu.move(carreRouge, x, y)   # FIXME le format est canvas.move(img, x, y), il faut donc trouver une facon de rendre l'airJeu disponible au scope de toutes ces methodes

    # cette methode permet au carreRouge de se deplacer vers la droite a l'écran
    def right(e):
        x = 20
        y = 0
        airJeu.move(carreRouge, x, y)

    # cette methode permet au carreRouge de se deplacer vers le haut a l'écran
    def up(e):
        x = 0
        y = -20
        airJeu.move(carreRouge, x, y)

    # cette methode permet au carreRouge de se deplacer vers le bas a l'écran
    def down(e):
        x = 0
        y = 20
        airJeu.move(carreRouge, x, y)

        # cette methode permet au carreRouge de se déplacer a l'ecran
    def move(e):
        image = carreRouge
        img = airJeu.create_image(e.x, e.y, image=image)

    