from tkinter import Canvas
class ModeleJeu:

    tailleCarreRouge = 40

    def __init__(self, container):
        self.carreRouge = Canvas(container, bg="#ff0000", width=self.tailleCarreRouge, height=self.tailleCarreRouge,highlightthickness=0)
        self.rectangleBleuGauche = Canvas(container, bg="#0000ff", width=60, height=60,highlightthickness=0)
        self.rectangleBleuSupDroit = Canvas(container, bg="#0000ff", width=60, height=50,highlightthickness=0)
        self.rectangleBleuInfGauche = Canvas(container, bg="#0000ff", width=85, height=350,highlightthickness=0)
        self.rectangleBleuInfDroit = Canvas(container, bg="#0000ff", width=355, height=340,highlightthickness=0)
        self.leftBorder = Canvas(container,width=50, height=450,bg="black",highlightthickness=0)
        self.rightBorder = Canvas(container,width=50, height=450,bg="black",highlightthickness=0)
        self.topBorder = Canvas(container,width=450, height=50,bg="black",highlightthickness=0)
        self.bottomBorder = Canvas(container,width=450, height=50,bg="black",highlightthickness=0)

    #methode pour creer le rcare rouge
    def afficher_carreRouge(self):
        self.carreRouge.place(x=225 - self.tailleCarreRouge / 2, y= 225 - self.tailleCarreRouge / 2)
        # cette fonctionnalité permet de déplacer carreRouge lorsque le boutton gauche de la souris est appuyé
        self.carreRouge.bind("<B1-Motion>", move)

    #methode pour creer rectangle bleuGauche
    def afficher_rectangleBleuGauche(self):
        self.rectangleBleuGauche.place(x=100, y=100)

    #methode pour creer rectangle bleuSupDroit
    def afficher_rectangleBleuSupDroit(self):
        self.rectangleBleuSupDroit.place(x=300, y=85)

    #methode pour creer rectangle bleuInfGauche
    def afficher_rectangleBleuInfGauche(self):
        self.rectangleBleuInfGauche.place(x=85, y=350)

    #methode pour creer rectangle bleuInfDroit
    def afficher_rectangleBleuInfDroit(self):
        self.rectangleBleuInfDroit.place(x=355, y=340)

    #methode pour afficher leftBorder
    def afficher_leftBorder(self):
        self.leftBorder.place(x=0,y=0)

    #methode pour afficher rightBorder
    def afficher_rightBorder(self):
        self.rightBorder.place(x=400,y=0)

    #methode pour afficher topBorder
    def afficher_topBorder(self):
        self.topBorder.place(x=0,y=0)

    #methode pour afficher bottomBorder
    def afficher_bottomBorder(self):
        self.bottomBorder.place(x=0, y=400)


    
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

    