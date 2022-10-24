from cgi import test
from VueJeu import VueJeu
from ModeleJeu import ModeleJeu
from functools import partial
import tkinter as tk
import random
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
            
        if self.enMvt == True:
            if self.it % 3 == 0:
                                
                    
                self.modeleJeu.carreRouge.translateTo(c31.Vecteur(e.x, e.y))
                self.modeleJeu.carreRouge.set_position(c31.Vecteur(e.x,e.y))
                self.modeleJeu.afficher_carreRouge()

                collision = False
                
                for i in range(4):

                    CRX = self.modeleJeu.carreRouge.get_position().y
                    CRY = self.modeleJeu.carreRouge.get_position().x
                    CRL = CRY - 20
                    CRR = CRY + 20
                    CRT = CRX - 20
                    CRB = CRX + 20
                    PL = self.modeleJeu.listeRectangles[i].get_position().x - self.modeleJeu.listT[i][0]/2
                    PR = self.modeleJeu.listeRectangles[i].get_position().x + self.modeleJeu.listT[i][0]/2
                    PT = self.modeleJeu.listeRectangles[i].get_position().y - self.modeleJeu.listT[i][1]/2
                    PB = self.modeleJeu.listeRectangles[i].get_position().y + self.modeleJeu.listT[i][1]/2

                    if  CRT <= PB and CRT >= PT or CRX <= PB and CRX >= PT:
                        if  CRR >= PL and CRR <= PR:
                            collision = True
                            break
                        elif CRL <= PR and CRL >= PL:
                            collision = True
                            break
                        elif CRY <= PR and CRY >= PL:
                            collision = True
                            break

                    elif  CRB >= PT and CRB <= PB or CRX>= PT and CRX <= PB:
                        if  CRR >= PL and CRR <= PR:
                            collision = True
                            break
                        elif CRL <= PR and CRL >= PL:
                            collision = True
                            break
                        elif CRY <= PR and CRY >= PL:
                            collision = True
                            break                 
                
                if not collision:
                    print('hello')
                else:
                    print('not hello')
                    
            self.it += 1

               
