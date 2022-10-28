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
        
        BL = self.bordure.listeBordures[0].get_position().x + self.bordure.listeTaillesBordure[0][0]/2  #position bordure gauche interne
        BR = self.bordure.listeBordures[1].get_position().x - self.bordure.listeTaillesBordure[1][0]/2  #position bordure droite interne
        BT = self.bordure.listeBordures[2].get_position().y + self.bordure.listeTaillesBordure[2][1]/2  #position bordure haut interne
        BB = self.bordure.listeBordures[3].get_position().y - self.bordure.listeTaillesBordure[3][1]/2  #position bordure bas interne
        
        CRY = self.carreRouge.carreRouge.get_position().y    #position Y milieu du carré rouge 
        CRX = self.carreRouge.carreRouge.get_position().x    #position X milieu du carré rouge 
        CRL = CRX - 20    #position gauche du carré rouge 
        CRR = CRX + 20    #position droite du carré rouge
        CRT = CRY - 20    #position haut du carré rouge
        CRB = CRY + 20    #position bas du carré rouge
        
        # detecte les collisions du carre rouge avec la bordure interne
        if  CRT <= BT or CRB >= BB or CRR >= BR or CRL <= BL: 
            collision = True
            print("carre rouge est sorti de l'aire de jeu")  # temp pour debug
            
        for i in range(4):
            
            RL = self.rectangles.listeRectangles[i].get_position().x - self.rectangles.listeTaillesRectangles[i][0]/2  #position gauche du pion
            RR = self.rectangles.listeRectangles[i].get_position().x + self.rectangles.listeTaillesRectangles[i][0]/2  #position droite du pion
            RT = self.rectangles.listeRectangles[i].get_position().y - self.rectangles.listeTaillesRectangles[i][1]/2  #position haut du pion
            RB = self.rectangles.listeRectangles[i].get_position().y + self.rectangles.listeTaillesRectangles[i][1]/2  #position bas du pion

            # la logique des collisions avec RB
            if  CRT <= RB and CRT >= RT or CRY <= RB and CRY >= RT or CRB >= RT and CRB <= RB:
                if  CRR >= RL and CRR <= RR or CRL <= RR and CRL >= RL or CRX <= RR and CRX >= RL:
                    collision = True
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

        BL = self.bordure.listeBordures[0].get_position().x - self.bordure.listeTaillesBordure[0][0]/2  #position bordure gauche externe
        BR = self.bordure.listeBordures[1].get_position().x + self.bordure.listeTaillesBordure[1][0]/2  #position bordure droite externe
        BT = self.bordure.listeBordures[2].get_position().y - self.bordure.listeTaillesBordure[2][1]/2  #position bordure haut externe
        BB = self.bordure.listeBordures[3].get_position().y + self.bordure.listeTaillesBordure[3][1]/2  #position bordure bas externe
        
        self.vitesse = 5

        for i in range(4):

            RBY = self.rectangles.listeRectangles[i].get_position().y    #position Y milieu du pion 
            RBX = self.rectangles.listeRectangles[i].get_position().x    #position X milieu du pion 
            RBL = RBX - self.rectangles.listeTaillesRectangles[i][0]/2    #position gauche du pion 
            RBR = RBX + self.rectangles.listeTaillesRectangles[i][0]/2    #position droite du pion
            RBT = RBY - self.rectangles.listeTaillesRectangles[i][1]/2    #position haut du pion
            RBB = RBY + self.rectangles.listeTaillesRectangles[i][1]/2    #position bas du pion
            
            # detecte les collisions des rectangles avec la bordure externe
            if  RBT <= BT:
                self.touchBorder = True
                # methode pour rebondir
                # changer direction en y pour bas
                print("rectangle est sorti de l'aire de jeu")  # temp pour debug
            if RBB >= BB:
                self.touchBorder = True
                # methode pour rebondir
                # changer direction en y pour haut
                print("rectangle est sorti de l'aire de jeu")  # temp pour debug
            if RBR >= BR:
                self.touchBorder = True
                # methode pour rebondir
                # changer direction en x pour gauche
                print("rectangle est sorti de l'aire de jeu")  # temp pour debug
            if RBL <= BL: 
                self.touchBorder = True
                # methode pour rebondir
                # changer direction en x pour gauche
                print("rectangle est sorti de l'aire de jeu")  # temp pour debug
        
        
        
            # for i in range(4):
                # peut etre utilise pour initialiser dans une methode commencer
            # debut methode
            gauche = self.rectangles.listeRectangles[i].get_position().x - self.vitesse
            haut = self.rectangles.listeRectangles[i].get_position().y - self.vitesse
            droite = self.rectangles.listeRectangles[i].get_position().x + self.vitesse
            bas = self.rectangles.listeRectangles[i].get_position().y + self.vitesse

            if i == 0:
                self.rectangles.listeRectangles[i].translateTo(c31.Vecteur(droite, bas))
                self.rectangles.listeRectangles[i].set_position(c31.Vecteur(droite, bas))
            if i == 1:
                self.rectangles.listeRectangles[i].translateTo(c31.Vecteur(gauche, bas))
                self.rectangles.listeRectangles[i].set_position(c31.Vecteur(gauche, bas))
            if i == 2:
                self.rectangles.listeRectangles[i].translateTo(c31.Vecteur(droite, haut))
                self.rectangles.listeRectangles[i].set_position(c31.Vecteur(droite, haut))
            if i == 3:
                self.rectangles.listeRectangles[i].translateTo(c31.Vecteur(gauche, haut))
                self.rectangles.listeRectangles[i].set_position(c31.Vecteur(gauche, haut))
            # fin

            # initialisation non optimisee

            # gauche = self.rectangles.listeRectangles[0].get_position().x - self.vitesse
            # haut = self.rectangles.listeRectangles[0].get_position().y - self.vitesse
            # droite = self.rectangles.listeRectangles[0].get_position().x + self.vitesse
            # bas = self.rectangles.listeRectangles[0].get_position().y + self.vitesse

            # self.rectangles.listeRectangles[0].translateTo(c31.Vecteur(droite, bas))
            # self.rectangles.listeRectangles[0].set_position(c31.Vecteur(droite, bas))

            # gauche = self.rectangles.listeRectangles[1].get_position().x - self.vitesse
            # haut = self.rectangles.listeRectangles[1].get_position().y - self.vitesse
            # droite = self.rectangles.listeRectangles[1].get_position().x + self.vitesse
            # bas = self.rectangles.listeRectangles[1].get_position().y + self.vitesse

            # self.rectangles.listeRectangles[1].translateTo(c31.Vecteur(gauche, bas))
            # self.rectangles.listeRectangles[1].set_position(c31.Vecteur(gauche, bas))

            # gauche = self.rectangles.listeRectangles[2].get_position().x - self.vitesse`
            # haut = self.rectangles.listeRectangles[2].get_position().y - self.vitesse
            # droite = self.rectangles.listeRectangles[2].get_position().x + self.vitesse
            # bas = self.rectangles.listeRectangles[2].get_position().y + self.vitesse

            # self.rectangles.listeRectangles[2].translateTo(c31.Vecteur(droite, haut))
            # self.rectangles.listeRectangles[2].set_position(c31.Vecteur(droite, haut))

            # gauche = self.rectangles.listeRectangles[3].get_position().x - self.vitesse
            # haut = self.rectangles.listeRectangles[3].get_position().y - self.vitesse
            # droite = self.rectangles.listeRectangles[3].get_position().x + self.vitesse
            # bas = self.rectangles.listeRectangles[3].get_position().y + self.vitesse

            # self.rectangles.listeRectangles[3].translateTo(c31.Vecteur(gauche, haut))
            # self.rectangles.listeRectangles[3].set_position(c31.Vecteur(gauche, haut))

            self.vueJeu.afficherRectanglesBlues(self.rectangles)
            
            self.rectangles.listeRectangles[i].set_position(self.rectangles.listeRectangles[i].get_position()) 

        self.vueJeu.afficherRectanglesBlues(self.rectangles)
