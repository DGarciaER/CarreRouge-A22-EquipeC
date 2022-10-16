from tkinter import Canvas
class ModeleJeu:

    tailleCarreRouge = 40

    def __init__(self, container):
        self.carreRouge = Canvas(container, bg="#ff0000", width=self.tailleCarreRouge, height=self.tailleCarreRouge)
        self.rectangleBleu = Canvas(container, bg="#0000ff", width=30, height=30)
        self.rectangleBleu = Canvas(container, bg="#0000ff", width=30, height=30)
        self.rectangleBleu = Canvas(container, bg="#0000ff", width=20, height=50)
        self.rectangleBleu = Canvas(container, bg="#0000ff", width=150, height=20)

    #methode pour creer le carre rouge
    #TODO faut-il deplacer cette methode dans une classe specifique au carreRouge? pareil pour les autres methodes d'initialisation..?
    def afficher_carreRouge(self):
        self.carreRouge.place(x=225 - self.tailleCarreRouge / 2, y= 225 - self.tailleCarreRouge / 2)
        # cette fonctionnalité permet de déplacer carreRouge lorsque le boutton gauche de la souris est appuyé
        self.carreRouge.bind("<B1-Motion>, move")

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

    #methode pour creer rectangle bleu1
    def afficher_rectangleBleu1(self):
        self.rectangleBleu.place(x=5, y=2)

    #methode pour creer rectangle bleu2
    def afficher_rectangleBleu2(self):
        self.rectangleBleu.place(x=150, y=2)

    #methode pour creer rectangle bleu3
    def afficher_rectangleBleu3(self):
        self.rectangleBleu.place(x=20, y=120)

    #methode pour creer rectangle bleu4
    def afficher_rectangleBleu4(self):
        self.rectangleBleu.place(x=100, y=100)