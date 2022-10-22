from cgi import test
from VueJeu import VueJeu
from ModeleJeu import ModeleJeu
from functools import partial
import tkinter as tk
import time

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
        self.gameOver = False
        self.it = 0
        
        self.modeleJeu.carreRouge.canvas.bind("<Button-1>", self.click)
        self.modeleJeu.carreRouge.canvas.bind("<Motion>", self.move)
        self.modeleJeu.carreRouge.canvas.bind("<ButtonRelease-1>", self.release)
        

    # cette methode commence le jeu
    
    def click(self, e):
        if  e.x > self.modeleJeu.carreRouge.get_position().x - 20:
            if e.x < self.modeleJeu.carreRouge.get_position().x + 20:
                if  e.y > self.modeleJeu.carreRouge.get_position().y - 20:
                    if e.y < self.modeleJeu.carreRouge.get_position().y + 20:
                        self.enMvt = True
                        
    def release(self, e):
        self.enMvt = False
    
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
            
            vertical = False
            horizontal = False
            
            if self.enMvt == True:
                if self.it % 3 == 0:
                    if self.modeleJeu.carreRouge.get_position().x - 20 < self.modeleJeu.listeRectangles[0].get_position().x + self.modeleJeu.listT[0][0]/2:
                        horizontal = True
                    if  self.modeleJeu.carreRouge.get_position().y - 20 < self.modeleJeu.listeRectangles[0].get_position().y + self.modeleJeu.listT[0][1]/2:
                        vertical = True
                    if  self.modeleJeu.carreRouge.get_position().x + 20 > self.modeleJeu.listeRectangles[0].get_position().x - self.modeleJeu.listT[0][0]/2:
                        horizontal = True
                    if self.modeleJeu.carreRouge.get_position().y + 20 > self.modeleJeu.listeRectangles[0].get_position().y - self.modeleJeu.listT[0][1]/2:
                        vertical = True
                    
                    if vertical and horizontal:    
                        print('hello')
                    # for i in range(4):
                                        
                    #     if  self.modeleJeu.carreRouge.get_position().x - 20 < self.modeleJeu.listeRectangles[i].get_position().x + self.modeleJeu.listT[i][0]/2:
                            # if  self.modeleJeu.carreRouge.get_position().x + 20 > self.modeleJeu.listeRectangles[i].get_position().x - self.modeleJeu.listT[i][0]/2:
                            # if  self.modeleJeu.carreRouge.get_position().y - 20 < self.modeleJeu.listeRectangles[i].get_position().y + self.modeleJeu.listT[i][1]/2 or self.modeleJeu.carreRouge.get_position().y + 20 > self.modeleJeu.listeRectangles[i].get_position().y - self.modeleJeu.listT[i][1]/2:
                            # print('hello')
                                        
                        # # if  self.modeleJeu.carreRouge.get_position().x - 20 < self.modeleJeu.listeRectangles[i].get_position().x + self.modeleJeu.listT[i][0]/2:
                        # elif  self.modeleJeu.carreRouge.get_position().x + 20 > self.modeleJeu.listeRectangles[i].get_position().x - self.modeleJeu.listT[i][0]/2:
                        #     if  self.modeleJeu.carreRouge.get_position().y - 20 < self.modeleJeu.listeRectangles[i].get_position().y + self.modeleJeu.listT[i][1]/2 or self.modeleJeu.carreRouge.get_position().y + 20 > self.modeleJeu.listeRectangles[i].get_position().y - self.modeleJeu.listT[i][1]/2:
                        #         print('hello')
                        
                        # if  self.modeleJeu.carreRouge.get_position().x - 20 < self.modeleJeu.listeRectangles[i].get_position().x + self.modeleJeu.listT[i][0]/2:
                        #     if  self.modeleJeu.carreRouge.get_position().x + 20 > self.modeleJeu.listeRectangles[i].get_position().x - self.modeleJeu.listT[i][0]/2:
                        #         if  self.modeleJeu.carreRouge.get_position().y - 20 < self.modeleJeu.listeRectangles[i].get_position().y + self.modeleJeu.listT[i][1]/2:
                        #             if  self.modeleJeu.carreRouge.get_position().y + 20 > self.modeleJeu.listeRectangles[i].get_position().y - self.modeleJeu.listT[i][1]/2:
                        #                 # if e.x < self.modeleJeu.carreRouge.get_position().x + 20:
                        #                 #     if  e.y > self.modeleJeu.carreRouge.get_position().y - 20:
                        #                 #         if e.y < self.modeleJeu.carreRouge.get_position().y + 20:
                        #                 print('hello')
                                        
                        #  if  self.modeleJeu.carreRouge.get_position().x - 20 < self.modeleJeu.listeRectangles[i].get_position().x + self.modeleJeu.listT[i][0]/2:
                        #         if  self.modeleJeu.carreRouge.get_position().x + 20 > self.modeleJeu.listeRectangles[i].get_position().x - self.modeleJeu.listT[i][0]/2:
                        #         if  self.modeleJeu.carreRouge.get_position().y - 20 < self.modeleJeu.listeRectangles[i].get_position().y + self.modeleJeu.listT[i][1]/2:
                        #             if  self.modeleJeu.carreRouge.get_position().y + 20 > self.modeleJeu.listeRectangles[i].get_position().y - self.modeleJeu.listT[i][1]/2:
                        #                 # if e.x < self.modeleJeu.carreRouge.get_position().x + 20:
                        #                 #     if  e.y > self.modeleJeu.carreRouge.get_position().y - 20:
                        #                 #         if e.y < self.modeleJeu.carreRouge.get_position().y + 20:
                        #                 print('hello')
                        
                        
                    self.modeleJeu.carreRouge.translateTo(c31.Vecteur(e.x, e.y))
                    self.modeleJeu.carreRouge.set_position(c31.Vecteur(e.x,e.y))
                    self.modeleJeu.afficher_carreRouge()
                    for i in range(4):
                        self.collision(self.modeleJeu.carreRouge, self.modeleJeu.listeRectangles[i])
                        if self.gameOver == False:
                            print("game over")
                            return

            self.it += 1   

    def collision(self, element1, element2):
        vecteur1x = element1.get_position().x
        vecteur1y = element1.get_position().y
        demiLongeur1 = (element1._vertex[1] - element1._vertex[0])/2    #demi longeur element 1
        demiHauteur1 = (element1._vertex[0] - element1._vertex[2])/2   #demi hauteur element 1
        vertex1 = []

        # coin haut gauche
        vertex1[0] = element1.origine + c31.Vecteur((demiLongeur1 * -1), (demiHauteur1 * -1))
        
        # coin haut droit
        vertex1[1] = element1.origine + c31.Vecteur(demiLongeur1, (demiHauteur1 * -1))

        # coin bas gauche
        vertex1[2] = element1.origine + c31.Vecteur((demiLongeur1 * -1), demiHauteur1)

        # coin bas droit
        vertex1[3] = element1.origine + c31.Vecteur(demiLongeur1, demiHauteur1)

        vecteur2x = element2.get_position().x
        vecteur2y = element2.get_position().y
        demiLongeur2 = abs(element2._vertex[1] - element2._vertex[0])/2    #demi longeur element 2
        demiHauteur2 = abs(element2._vertex[0] - element2._vertex[2])/2   #demi hauteur element 2

        vertex2 = []
        
        # coin haut gauche
        vertex2[0] = element2.origine + c31.Vecteur((demiLongeur2 * -1), (demiHauteur2 * -1))
        
        # coin haut droit
        vertex2[1] = element2.origine + c31.Vecteur(demiLongeur2, (demiHauteur2 * -1))

        # coin bas gauche
        vertex2[2] = element2.origine + c31.Vecteur((demiLongeur2 * -1), demiHauteur2)

        # coin bas droit
        vertex2[3] = element2.origine + c31.Vecteur(demiLongeur2, demiHauteur2)

        deltax = abs(vecteur2x - vecteur1x)
        deltay = abs(vecteur2y - vecteur1y)

        
        # cas du carreRouge
        # if demiLongeur1 == demiHauteur1:
        if deltax < (demiLongeur1 + demiLongeur2):
            self.enMvt = False
            self.gameOver = False
        elif  deltay < demiHauteur1 + demiHauteur2:
            self.enMvt = False
            self.gameOver = False
            
        
