from cgi import test
from VueJeu import VueJeu
from ModeleJeu import ModeleJeu
from functools import partial
import tkinter as tk
from datetime import datetime
        

import c31Geometry2 as c31

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
        self.enMvt = False
        self.it = 0
        self.tpsDebutPartie = 0
        self.tpsFinPartie = 0
        self.tpsTotal = 0
        
        self.modeleJeu.carreRouge.canvas.bind("<Button-1>", self.click)
        self.modeleJeu.carreRouge.canvas.bind("<Motion>", self.move)
        self.modeleJeu.carreRouge.canvas.bind("<ButtonRelease-1>", self.release)

    # cette methode commence le jeu
    
    def click(self, e):
        if  e.x > self.modeleJeu.carreRouge.get_position().x - 40/2:
            if e.x < self.modeleJeu.carreRouge.get_position().x + 40/2:
                if  e.y > self.modeleJeu.carreRouge.get_position().y - 40/2:
                    if e.y < self.modeleJeu.carreRouge.get_position().y + 40/2:
                        self.enMvt = True
                        self.tpsDebutPartie = datetime.now();
                        
    def release(self, e):
        self.enMvt = False
        self.tpsFinPartie = datetime.now();
        self.tpsTotal = self.tpsFinPartie - self.tpsDebutPartie
        print(self.tpsTotal, "secondes");
    
    def start(self, container):    
        self.vueJeu.clear(container)
        
    def move(self, e):


        # if coordonneX != self.modeleJeu.carreRouge.get_position().x and coordonneY != self.modeleJeu.carreRouge.get_position().y:
            # self.modeleJeu.carreRouge.set_remplissage("grey90")
            # self.modeleJeu.carreRouge.set_bordure("grey90")
            # self.modeleJeu.afficher_carreRouge()
            # self.modeleJeu.carreRouge = c31.Carre(container, c31.Vecteur(coordonneX,coordonneY),40,0, '#ff0000', '#ff0000', 0)
            # self.modeleJeu.carreRouge.set_position(c31.Vecteur(coordonneX,coordonneY))
            
            # print(str(self.modeleJeu.carreRouge.get_position().x) + " " + str(self.modeleJeu.carreRouge.get_position().y))
            
            
            # self.modeleJeu.carreRouge.set_remplissage("black")
            # self.modeleJeu.carreRouge.translate(self.modeleJeu.carreRouge.get_position())
            # self.modeleJeu.carreRouge.translateTo(c31.Vecteur(coordonneX,coordonneY))
            
            
            # self.modeleJeu.carreRouge.translate(self.modeleJeu.carreRouge.get_position())
            # self.modeleJeu.afficher_carreRouge()
            # time.sleep(0.2)
            
            if self.enMvt == True:
                if self.it % 3 == 0:
                    for i in range(4):
                        if  e.x > self.modeleJeu.carreRouge.get_position().x - 40/2:
                            if e.x < self.modeleJeu.carreRouge.get_position().x + 40/2:
                                if  e.y > self.modeleJeu.carreRouge.get_position().y - 40/2:
                                    if e.y < self.modeleJeu.carreRouge.get_position().y + 40/2:
                                        pass
                        
                        
                    self.modeleJeu.carreRouge.translateTo(c31.Vecteur(e.x, e.y))
                    self.modeleJeu.carreRouge.set_position(c31.Vecteur(e.x,e.y))
                    self.modeleJeu.afficher_carreRouge()
            self.it += 1   

    
class Mouvement:
    pass
    
    # #TODO faut-il deplacer cette methode dans une classe specifique au carreRouge? pareil pour les autres methodes d'initialisation..?

    # # cette methode permet au carreRouge de se deplacer vers la gauche a l'écran
    # #TODO ajuster la valeur de deplacement (réduire pour que l'on voit plus précisement ou se trouve le carre)
    # def left(e):
    #     x = -20
    #     y = 0
    #     airJeu.move(carreRouge, x, y)   # FIXME le format est canvas.move(img, x, y), il faut donc trouver une facon de rendre l'airJeu disponible au scope de toutes ces methodes

    # # cette methode permet au carreRouge de se deplacer vers la droite a l'écran
    # def right(e):
    #     x = 20
    #     y = 0
    #     airJeu.move(carreRouge, x, y)

    # # cette methode permet au carreRouge de se deplacer vers le haut a l'écran
    # def up(e):
    #     x = 0
    #     y = -20
    #     airJeu.move(carreRouge, x, y)

    # # cette methode permet au carreRouge de se deplacer vers le bas a l'écran
    # def down(e):
    #     x = 0
    #     y = 20
    #     airJeu.move(carreRouge, x, y)

    #     # cette methode permet au carreRouge de se déplacer a l'ecran
    # def move(e):
    #     image = carreRouge
    #     img = airJeu.create_image(e.x, e.y, image=image)

    