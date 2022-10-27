from cgi import test
from itertools import count
from VueJeu import VueJeu
from ModeleJeu import ModeleJeu
from functools import partial
import tkinter as tk
from datetime import datetime



import c31Geometry2 as c31

class ControleurJeu(tk.Frame):
    '''
    Classe pour le la partie "Controleur jeu" du modèle MVC (Model-View-Controller)
    
    Attributs:
        container:
        enMouvement:
        gameOver:
        it:
        modeleJeu:
    '''
    def __init__(self, container, window=None):
        '''
        Le constructeur de la classe "ControleurJeu"
        
        Paramètres:
            container:
        '''
        super().__init__(window)
        self.window = window
        self.update_time = ''
        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.pack()
        self.create_widgets()
        self.minutes_string = ""
        self.seconds_string = ""
        self.milliseconds_string = ""
        
        
        

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
        self.collision = False
        
        
        self.modeleJeu.carreRouge.canvas.bind("<Button-1>", self.click)
        self.modeleJeu.carreRouge.canvas.bind("<Motion>", self.move)
        self.modeleJeu.carreRouge.canvas.bind("<ButtonRelease-1>", self.release)
        
    def create_widgets(self):
        self.stopwatch_label = tk.Label(self, text='00:00:00', font=('Arial', 80))
        self.stopwatch_label.pack()
        # self.start_button = tk.Button(self, text='start', height=5, width=7, font=('Arial', 20), command=self.start)
        # self.start_button.pack(side=tk.LEFT)
        # self.pause_button = tk.Button(self, text='pause', height=5, width=7, font=('Arial', 20), command=self.pause)
        # self.pause_button.pack(side=tk.LEFT)
        # self.reset_button = tk.Button(self, text='reset', height=5, width=7, font=('Arial', 20), command=self.reset)
        # self.reset_button.pack(side=tk.LEFT)
        # self.quit_button = tk.Button(self, text='quit', height=5, width=7, font=('Arial', 20), command=self.window.quit)
        # self.quit_button.pack(side=tk.LEFT)
        # self.window.title('Stopwatch (Class)')

    def start1(self):
        if not self.running:
                self.stopwatch_label.after(10)
                self.update()
                self.running = True

    def pause(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.update_time)
            self.running = False

    # def reset(self):
    #     if self.running:
    #         self.stopwatch_label.after_cancel(self.update_time)
    #         self.running = False
    #     self.minutes, self.seconds, self.milliseconds = 0, 0, 0
    #     self.stopwatch_label.config(text='00:00:00')

    def update(self):
        self.milliseconds += 1
        if self.milliseconds == 60:
            self.seconds += 1
            self.milliseconds = 0
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        self.minutes_string = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
        self.seconds_string = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
        self.milliseconds_string = f'{self.milliseconds}' if self.milliseconds > 9 else f'0{self.milliseconds}'
        self.stopwatch_label.config(text=self.minutes_string + ':' + self.seconds_string + ':' + self.milliseconds_string)
        self.update_time = self.stopwatch_label.after(10, self.update)
        
        
        
        
  

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
            if self.collision == False:
                self.start1()
                        
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
                    # print(True)
                    self.collision = True
                    #mettre temps dans fichier csv
                    print(self.minutes_string + ":" + self.seconds_string + ":" + self.milliseconds_string)
                    self.pause()
                    
                # else:
                    # print(False)

            self.it += 1
        

  