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
        self.iteration = 0
        
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
            if self.iteration % 3 == 0:    
                    
                self.carreRouge.carreRouge.translateTo(c31.Vecteur(e.x, e.y))
                self.carreRouge.carreRouge.set_position(c31.Vecteur(e.x,e.y))
                self.vueJeu.afficherCarreRouge(self.carreRouge.carreRouge)
                
                self.moveR()
                self.collision()
            self.iteration += 1
            
    def collision(self):
        
        collision = False
        
        # BL = self.bordure.listeBordures[0].get_position().x + self.bordure.listeTaillesBordure[0][0]/2  #position gauche de la bordure
        # BR = self.bordure.listeBordures[1].get_position().x - self.bordure.listeTaillesBordure[1][0]/2  #position droite de la bordure
        # BT = self.bordure.listeBordures[2].get_position().y + self.bordure.listeTaillesBordure[2][1]/2  #position haut de la bordure
        # BB = self.bordure.listeBordures[3].get_position().y - self.bordure.listeTaillesBordure[3][1]/2  #position bas de la bordure
        
        CRY = self.carreRouge.carreRouge.get_position().y    #position Y milieu du carré rouge 
        CRX = self.carreRouge.carreRouge.get_position().x    #position X milieu du carré rouge 
        CRL = CRX - 20    #position gauche du carré rouge 
        CRR = CRX + 20    #position droite du carré rouge
        CRT = CRY - 20    #position haut du carré rouge
        CRB = CRY + 20    #position bas du carré rouge
        
        # if  CRT <= BB and CRT >= BT or CRY <= BB and CRY >= BT or CRB >= BT and CRB <= BB:
        #         if  CRR >= BL and CRR <= BR or CRL <= BR and CRL >= BL or CRX <= BR and CRX >= BL:
        #             collision = False
        #             print("BF")  # temp pour debug
        #         else:
        #             collision = True
        #             print("BT")  # temp pour debug
            
        for i in range(4):
            
            RL = self.rectangles.listeRectangles[i].get_position().x - self.rectangles.listeTaillesRectangles[i][0]/2  #position gauche du pion
            RR = self.rectangles.listeRectangles[i].get_position().x + self.rectangles.listeTaillesRectangles[i][0]/2  #position droite du pion
            RT = self.rectangles.listeRectangles[i].get_position().y - self.rectangles.listeTaillesRectangles[i][1]/2  #position haut du pion
            RB = self.rectangles.listeRectangles[i].get_position().y + self.rectangles.listeTaillesRectangles[i][1]/2  #position bas du pion

            # la logique des collisions avec RB
            if  CRT <= RB and CRT >= RT or CRY <= RB and CRY >= RT or CRB >= RT and CRB <= RB:
                if  CRR >= RL and CRR <= RR or CRL <= RR and CRL >= RL or CRX <= RR and CRX >= RL:
                    collision = True
                    print("RB") # temp pour debug
                    break
                
                    
            
        
        if collision:
            print(True)
        else:
            print(False)
            
    def moveR(self):
        """ Cette méthode permet de bouger les pions (rectangle bleu) dans le canvas.
        parametre:
        event
        """
        
        # chaque bordure droite/gauche change seulement direction sur droite ou gauche 
        # chaque bordure haut/bas change seulement direction sur haut ou bas 
        
        self.touchBorder = False
        
        for i in range(4):

            RBY = self.rectangles.listeRectangles[i].get_position().y    #position Y milieu du carré rouge 
            RBX = self.rectangles.listeRectangles[i].get_position().x    #position X milieu du carré rouge 
            RBL = RBX - self.rectangles.listeTaillesRectangles[i][0]/2    #position gauche du carré rouge 
            RBR = RBX + self.rectangles.listeTaillesRectangles[i][0]/2    #position droite du carré rouge
            RBT = RBY - self.rectangles.listeTaillesRectangles[i][1]/2    #position haut du carré rouge
            RBB = RBY + self.rectangles.listeTaillesRectangles[i][1]/2    #position bas du carré rouge
            RL = self.rectangles.listeRectangles[i].get_position().x - self.rectangles.listeTaillesRectangles[i][0]/2  #position gauche du pion
            RR = self.rectangles.listeRectangles[i].get_position().x + self.rectangles.listeTaillesRectangles[i][0]/2  #position droite du pion
            RT = self.rectangles.listeRectangles[i].get_position().y - self.rectangles.listeTaillesRectangles[i][1]/2  #position haut du pion
            RB = self.rectangles.listeRectangles[i].get_position().y + self.rectangles.listeTaillesRectangles[i][1]/2  #position bas du pion

            # la logique des collisions
            if  RBT <= RB and RBT >= RT or RBY <= RB and RBY >= RT or RBB >= RT and RBB <= RB:
                if  RBR >= RL and RBR <= RR or RBL <= RR and RBL >= RL or RBX <= RR and RBX >= RL:
                    self.touchBorder = True
                    break
        
        self.vitesse = 5
        
        # self.rectangles.listeRectangles[0].translate(c31.Vecteur.bas() * self.vitesse)
        # self.rectangles.listeRectangles[0].translate(c31.Vecteur.droite() * self.vitesse)
        
        gauche = self.rectangles.listeRectangles[0].get_position().x - self.vitesse
        haut = self.rectangles.listeRectangles[0].get_position().y - self.vitesse
        droite = self.rectangles.listeRectangles[0].get_position().x + self.vitesse
        bas = self.rectangles.listeRectangles[0].get_position().y + self.vitesse

        self.rectangles.listeRectangles[0].translateTo(c31.Vecteur(droite, bas))
        self.rectangles.listeRectangles[0].set_position(c31.Vecteur(droite, bas))

        self.vueJeu.afficherRectanglesBlues(self.rectangles)
            
        
        # self.rectangles.listeRectangles[1].translate(c31.Vecteur.bas() * self.vitesse)
        # self.rectangles.listeRectangles[1].translate(c31.Vecteur.gauche() * self.vitesse)
        
        # self.rectangles.listeRectangles[2].translate(c31.Vecteur.haut() * self.vitesse)
        # self.rectangles.listeRectangles[2].translate(c31.Vecteur.droite() * self.vitesse)
        
        # self.rectangles.listeRectangles[3].translate(c31.Vecteur.haut() * self.vitesse)
        # self.rectangles.listeRectangles[3].translate(c31.Vecteur.gauche() * self.vitesse)
        
        for i in range(4):
            self.rectangles.listeRectangles[i].set_position(self.rectangles.listeRectangles[i].get_position()) 

        self.vueJeu.afficherRectanglesBlues(self.rectangles)
        
