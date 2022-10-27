from cgi import test
from VueJeu import VueJeu
from ModeleJeu import Bordure, CarreRouge, Rectangles
from functools import partial
import tkinter as tk

import c31Geometry2 as c31

class ControleurJeu:
    """
    Cette classe contient les fonctionnalités du jeu
    """
    
    def __init__(self, container):
        """
        parametres container
        """
        self.vueJeu = VueJeu()
        self.carreRouge = CarreRouge(container)
        self.rectangles = Rectangles(container)
        self.bordure = Bordure(container)
        self.vueJeu.afficherCarreRouge(self.carreRouge.carreRouge)
        self.vueJeu.afficherRectanglesBlues(self.rectangles)
        self.vueJeu.afficherBordure(self.bordure)
        self.enMouvement = False
        self.gameOver = False
        self.it = 0
        
        self.carreRouge.carreRouge.canvas.bind("<Button-1>", self.click)
        self.carreRouge.carreRouge.canvas.bind("<Motion>", self.moveCR)
        self.carreRouge.carreRouge.canvas.bind("<ButtonRelease-1>", self.release)
        

    # cette methode commence le jeu
    def click(self, e):
        """
        Cette méthode détecte un click gauche de la souris sur le carré rouge et change la valeur de vérité de la variable enMouvement en conséquence.
        La valeur de vérité de la variable enMouvement est une condition pour permettre le mouvement du carré rouge.
        parametre:
        event
        """

        CRL = self.carreRouge.carreRouge.get_position().x - 20    #position gauche du carré rouge 
        CRR = self.carreRouge.carreRouge.get_position().x + 20    #position droite du carré rouge
        CRT = self.carreRouge.carreRouge.get_position().y - 20    #position haut du carré rouge
        CRB = self.carreRouge.carreRouge.get_position().y + 20    #position bas du carré rouge
        
        if  e.x > CRL and e.x < CRR and e.y > CRT and e.y < CRB:
            self.enMouvement = True
                        
    def release(self, e):
        """
        Cette méthode détecte le release du boutton gauche de la souris.
        parametre:
        event
        """
        self.enMouvement = False
    
    def start(self, container):
        """
        Cette méthode clear? le container.
        parametre: 
        container
        """       
        self.vueJeu.clear(container)
        
    def moveCR(self, e):
        """
        Cette méthode permet de bouger le carré rouge dans le canvas.
        parametre:
        event
        """  
            
        if self.enMouvement == True:
            if self.it % 3 == 0:    
                    
                self.carreRouge.carreRouge.translateTo(c31.Vecteur(e.x, e.y))
                self.carreRouge.carreRouge.set_position(c31.Vecteur(e.x,e.y))
                self.vueJeu.afficherCarreRouge(self.carreRouge.carreRouge)
                
                self.collision()
            self.it += 1
            
    def collision(self):
        
        collision = False
            
        for i in range(4):

            CRY = self.carreRouge.carreRouge.get_position().y    #position Y milieu du carré rouge 
            CRX = self.carreRouge.carreRouge.get_position().x    #position X milieu du carré rouge 
            CRL = CRX - 20    #position gauche du carré rouge 
            CRR = CRX + 20    #position droite du carré rouge
            CRT = CRY - 20    #position haut du carré rouge
            CRB = CRY + 20    #position bas du carré rouge
            PL = self.rectangles.listeRectangles[i].get_position().x - self.rectangles.listeTaillesRectangles[i][0]/2  #position gauche du pion
            PR = self.rectangles.listeRectangles[i].get_position().x + self.rectangles.listeTaillesRectangles[i][0]/2  #position droite du pion
            PT = self.rectangles.listeRectangles[i].get_position().y - self.rectangles.listeTaillesRectangles[i][1]/2  #position haut du pion
            PB = self.rectangles.listeRectangles[i].get_position().y + self.rectangles.listeTaillesRectangles[i][1]/2  #position bas du pion

            # la logique des collisions
            if  CRT <= PB and CRT >= PT or CRY <= PB and CRY >= PT or CRB >= PT and CRB <= PB:
                if  CRR >= PL and CRR <= PR or CRL <= PR and CRL >= PL or CRX <= PR and CRX >= PL:
                    collision = True
                    break
        
        if collision:
            print(True)
        else:
            print(False)
            
    def moveP(self):
        """ Cette méthode permet de bouger les pions (rectangle bleu) dans le canvas.
        parametre:
        event
        """
        pass

