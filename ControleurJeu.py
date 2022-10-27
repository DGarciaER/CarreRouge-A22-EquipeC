from cgi import test
from itertools import count
from VueJeu import VueJeu
from ModeleJeu import ModeleJeu
from functools import partial
import tkinter as tk
from datetime import datetime
import Main


import c31Geometry2 as c31

class stopwatch():
    '''
    Cette classe s'occupe du générer le score/stopwatch lorsqu'on clique sur le carré rouge
    '''

    def __int__(self):
        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.update_time = stopwatch_label.after(1000, update)

    def start(self):
        if not self.running:
            update()
            running = True

    def pause(self):
        if self.running:
            stopwatch_label.after_cancel(update_time)
            self.running = False;

    def reset(self):
        if self.running:
            stopwatch_label.after_cancel(update_time)
            running = False
        self.minutes, self.seconds = 0

        stopwatch_label.config(text='00:00 ')



    

class ControleurJeu:
    '''
    Classe pour le la partie "Controleur jeu" du modèle MVC (Model-View-Controller)
    
    Attributs:
        container:
        enMouvement:
        gameOver:
        it:
        modeleJeu:
    '''
    def __init__(self, container):
        '''
        Le constructeur de la classe "ControleurJeu"
        
        Paramètres:
            container:
        '''

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
        self.modeleJeu.carreRouge.canvas.bind("<Motion>", self.move)
        self.modeleJeu.carreRouge.canvas.bind("<ButtonRelease-1>", self.release)
        

    # cette methode commence le jeu
    def click(self, e):
        '''
        Cette méthode commence le jeu lorsqu'on clique sur le carré rouge
        
        Paramètre:
            e: L'événement (...)
        '''
        CRL = self.modeleJeu.carreRouge.get_position().x - 20    #position gauche du carré rouge 
        CRR = self.modeleJeu.carreRouge.get_position().x + 20    #position droite du carré rouge
        CRT = self.modeleJeu.carreRouge.get_position().y - 20    #position haut du carré rouge
        CRB = self.modeleJeu.carreRouge.get_position().y + 20    #position bas du carré rouge
        
        if  e.x > CRL and e.x < CRR and e.y > CRT and e.y < CRB:
            self.enMouvement = True
                        
    def release(self, e):
        '''
        (...)
        
        Paramètre:
            e: L'événement (...)
        '''
        self.enMouvement = False
    
    def start(self, container):
        '''
        (...)
        
        Paramètre:
            container: (...)
            
        '''    
        self.vueJeu.clear(container)
        
    def move(self, e):
        
        '''
        Cette méthode sert à bouger le carré rouge dans l'aire de jeu.
        
        Paramètres:
            e: L'événement (...)
        '''        
        
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

               
