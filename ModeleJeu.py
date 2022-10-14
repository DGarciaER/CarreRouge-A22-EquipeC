from tkinter import Canvas
class ModeleJeu:
    #methode pour creer lair de jeu
    def creation_airJeu (container):
        airJeu = Canvas(container,bg="#808080", width= 450, height=450)
        airJeu.place(x=10,y=0)

    #methode pour creer le carre rouge
    #TODO faut-il deplacer cette methode dans une classe specifique au carreRouge? pareil pour les autres methodes d'initialisation..?
    def creation_carreRouge(container):
        carreRouge = Canvas(container, bg="#ff0000", width=20, height=20)
        carreRouge.place(x=100,y=60)
        # cette fonctionnalité permet de déplacer carreRouge lorsque le boutton gauche de la souris est appuyé
        carreRouge.bind("<B1-Motion>, move")

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
    def creation_rectangleBleu1(container):
        rectangleBleu = Canvas(container, bg="#0000ff", width=30, height=30)
        rectangleBleu.place(x=5, y=2)

    #methode pour creer rectangle bleu2
    def creation_rectangleBleu2(container):
        rectangleBleu = Canvas(container, bg="#0000ff", width=30, height=30)
        rectangleBleu.place(x=150, y=2)

    #methode pour creer rectangle bleu3
    def creation_rectangleBleu3(container):
        rectangleBleu = Canvas(container, bg="#0000ff", width=20, height=50)
        rectangleBleu.place(x=20, y=120)

    #methode pour creer rectangle bleu4
    def creation_rectangleBleu4(container):
        rectangleBleu = Canvas(container, bg="#0000ff", width=150, height=20)
        rectangleBleu.place(x=100, y=100)