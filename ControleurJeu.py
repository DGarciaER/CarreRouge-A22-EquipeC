from cgi import test
from VueJeu import VueJeu
from ModeleJeu import ModeleJeu
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
        self.enMouvement = False
        self.gameOver = False
        self.it = 0
        
        self.modeleJeu.carreRouge.canvas.bind("<Button-1>", self.click)
        self.modeleJeu.carreRouge.canvas.bind("<Motion>", self.moveCR)
        self.modeleJeu.carreRouge.canvas.bind("<ButtonRelease-1>", self.release)
        

    def click(self, e):
        """
        Cette méthode détecte un click gauche de la souris sur le carré rouge et change la valeur de vérité de la variable enMouvement en conséquence.
        La valeur de vérité de la variable enMouvement est une condition pour permettre le mouvement du carré rouge.
        parametre:
        event
        """

        CRL = self.modeleJeu.carreRouge.get_position().x - 20    #position gauche du carré rouge 
        CRR = self.modeleJeu.carreRouge.get_position().x + 20    #position droite du carré rouge
        CRT = self.modeleJeu.carreRouge.get_position().y - 20    #position haut du carré rouge
        CRB = self.modeleJeu.carreRouge.get_position().y + 20    #position bas du carré rouge
        
        if  e.x > CRL and e.x < CRR and e.y > CRT and e.y < CRB:
            self.enMouvement = True
            # methode moveP
                        
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
                    
                self.modeleJeu.carreRouge.translateTo(c31.Vecteur(e.x, e.y))
                self.modeleJeu.carreRouge.set_position(c31.Vecteur(e.x,e.y))
                self.modeleJeu.afficher_carreRouge()

                collision = False
                
                for i in range(4):

                    CRY = self.modeleJeu.carreRouge.get_position().y    #position Y milieu du carré rouge 
                    CRX = self.modeleJeu.carreRouge.get_position().x    #position X milieu du carré rouge 
                    CRL = CRX - 20    #position gauche du carré rouge 
                    CRR = CRX + 20    #position droite du carré rouge
                    CRT = CRY - 20    #position haut du carré rouge
                    CRB = CRY + 20    #position bas du carré rouge
                    PL = self.modeleJeu.listeRectangles[i].get_position().x - self.modeleJeu.listT[i][0]/2  #position gauche du pion
                    PR = self.modeleJeu.listeRectangles[i].get_position().x + self.modeleJeu.listT[i][0]/2  #position droite du pion
                    PT = self.modeleJeu.listeRectangles[i].get_position().y - self.modeleJeu.listT[i][1]/2  #position haut du pion
                    PB = self.modeleJeu.listeRectangles[i].get_position().y + self.modeleJeu.listT[i][1]/2  #position bas du pion

                    # la logique des collisions
                    if  CRT <= PB and CRT >= PT or CRY <= PB and CRY >= PT:
                        if  CRR >= PL and CRR <= PR:
                            collision = True
                            break
                        elif CRL <= PR and CRL >= PL:
                            collision = True
                            break
                        elif CRX <= PR and CRX >= PL:
                            collision = True
                            break

                    elif  CRB >= PT and CRB <= PB or CRY>= PT and CRY <= PB:
                        if  CRR >= PL and CRR <= PR:
                            collision = True
                            break
                        elif CRL <= PR and CRL >= PL:
                            collision = True
                            break
                        elif CRX <= PR and CRX >= PL:
                            collision = True
                            break                 
                
                if collision:
                    print(True)
                else:
                    print(False)

            self.it += 1
            
    def moveP(self):
        """ Cette méthode permet de bouger les pions (rectangle bleu) dans le canvas.
        parametre:
        event
        """
        pass

               
