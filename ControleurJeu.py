from cgi import test
from VueJeu import VueJeu
from ModeleJeu import ModeleJeu
import tkinter as tk

class ControleurJeu:
    
    def __init__(self, container):
        self.vueJeu = VueJeu()
        self.modeleJeu = ModeleJeu(container)
        self.modeleJeu.afficher_carreRouge()
        self.modeleJeu.afficher_rectangleBleuSupDroit()
        self.modeleJeu.afficher_rectangleBleuGauche()
        self.modeleJeu.afficher_rectangleBleuInfDroit()
        self.modeleJeu.afficher_rectangleBleuInfGauche()
        self.modeleJeu.afficher_leftBorder()
        self.modeleJeu.afficher_rightBorder()
        self.modeleJeu.afficher_topBorder()
        self.modeleJeu.afficher_bottomBorder()

    # cette methode commence le jeu
    def start(self, container):    
        self.vueJeu.clear(container)
    
class Mouvement:
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

    