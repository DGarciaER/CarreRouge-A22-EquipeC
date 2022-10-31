from cgi import test
from operator import truediv
from VueJeu import VueJeu
from ModeleJeu import Bordure, CarreRouge, Rectangles
from functools import partial
import tkinter as tk
import time
from threading import Timer
import csv

import c31Geometry2 as c31

class ControleurJeu(tk.Frame):
    """
    Cette classe contient les fonctionnalités du jeu
    """
    def __init__(self, container, window=None):

        #Variables timer
        super().__init__(window)
        self.window = window
        self.update_time = ''
        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.pack()
        # self.create_widgets()
        self.minutes_string = ""
        self.seconds_string = ""
        self.milliseconds_string = ""

        #variables score
        self.listScore = []
        self.nbrTourBoucle = 0
        self.username = ''

        """
        parametres container
        """
        self.vueJeu = VueJeu()
        self.carreRouge = CarreRouge(container)
        self.rectangles = Rectangles(container)
        self.bordure = Bordure(container)
        
        self.initializeAll()

        self.carreRouge.carreRouge.canvas.bind("<Button-1>", self.click)
        self.carreRouge.carreRouge.canvas.bind("<Motion>", self.moveCR)
        self.carreRouge.carreRouge.canvas.bind("<ButtonRelease-1>", self.release)



        #PARTIE POUR TIMER    
    def create_widgets(self, container):
        self.stopwatch_label = tk.Label(container, text='00:00:00', font=('Arial', 20), background= "#FFE299")
        self.stopwatch_label.grid(column=1, row=2, padx=10)

    def startTimer(self):
        if not self.running:
                self.stopwatch_label.after(10)
                self.updateTimer()
                self.running = True

    def pauseTimer(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.update_time)
            self.running = False

    def resetTimer(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.update_time)
            self.running = False
        self.minutes, self.seconds, self.milliseconds = 0, 0, 0
        self.stopwatch_label.config(text='00:00:00')

    def updateTimer(self):
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
        self.update_time = self.stopwatch_label.after(10, self.updateTimer)
    #FIN PARTIE TIMER    
        
    #PARTIE CSV

    #Ecriture du score et username dans fichier csv
    def openCSV(self, score, username):
        f = open('score.csv', 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([username, score])
        f.close()

    #Window pop up pour le username
    def setUsername(self, x):
        if not x == None:
            self.username = x + "\n"
        else:
            self.username = x
        

    



    def initializeAll(self):
        self.enMouvement = False # boolean qui change selon les evenements click ou release du B1 de la souris, permet de savoir quand deplacer le carre rouge et quand le laisser statique 
        self.gameOver = False # boolean qui nous permet d'arreter le jeu lorsqu'il y a une collision
        self.premierMouv = True
        self.premierClick = True
        self.iteration = 0 # valeur qui permet de ralentir l'affichage du carre rouge pour assurer une belle presentation
        
        self.DirectionActuelle = [c31.Vecteur(0, 0), c31.Vecteur(0, 0), c31.Vecteur(0, 0), c31.Vecteur(0, 0) ]   
        self.boolDroiteHaut = [False, False, False, False]
        self.boolDroiteBas = [False, False, False, False]
        self.boolGaucheHaut = [False, False, False, False]
        self.boolGaucheBas = [False, False, False, False]

        self.carreRouge.carreRouge.translateTo(c31.Vecteur(225,225))
        self.carreRouge.carreRouge.set_position(c31.Vecteur(225,225))
        self.rectangles.listeRectangles[0].translateTo(c31.Vecteur(100, 100))
        self.rectangles.listeRectangles[0].set_position(c31.Vecteur(100, 100))
        self.rectangles.listeRectangles[1].translateTo(c31.Vecteur(300, 85))
        self.rectangles.listeRectangles[1].set_position(c31.Vecteur(300, 85))
        self.rectangles.listeRectangles[2].translateTo(c31.Vecteur(85, 350))
        self.rectangles.listeRectangles[2].set_position(c31.Vecteur(85, 350))
        self.rectangles.listeRectangles[3].translateTo(c31.Vecteur(355, 340))
        self.rectangles.listeRectangles[3].set_position(c31.Vecteur(355, 340))

        self.vueJeu.afficherBordure(self.bordure)
        self.vueJeu.afficherRectanglesBlues(self.rectangles)
        self.vueJeu.afficherCarreRouge(self.carreRouge.carreRouge)


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
            if self.premierClick:
                self.premierClick = False
                self.resetTimer()
                self.startTimer()
                self.moveR()
                        
    def release(self, e):
        """
        Cette méthode détecte le release du boutton gauche de la souris.
        parametre:
        event
        """
        self.enMouvement = False
        
    def moveCR(self, e): # move Carré Rouge
        """
        Cette méthode permet de bouger le carré rouge dans le canvas.
        parametre:
        event
        """  
            
        if self.enMouvement == True and not self.gameOver:
            if self.iteration % 3 == 0: # relentir d'affichage 
                self.iteration = 0
                self.carreRouge.carreRouge.translateTo(c31.Vecteur(e.x, e.y))
                self.carreRouge.carreRouge.set_position(c31.Vecteur(e.x,e.y))
                self.vueJeu.afficherCarreRouge(self.carreRouge.carreRouge)
                
            self.iteration += 1
            
    def collision(self):
        
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
            self.gameOver = True
            print("carre rouge est sorti de l'aire de jeu")  # temp pour debug
            
        for i in range(4):
            
            RL = self.rectangles.listeRectangles[i].get_position().x - self.rectangles.listeTaillesRectangles[i][0]/2  #position gauche du pion
            RR = self.rectangles.listeRectangles[i].get_position().x + self.rectangles.listeTaillesRectangles[i][0]/2  #position droite du pion
            RT = self.rectangles.listeRectangles[i].get_position().y - self.rectangles.listeTaillesRectangles[i][1]/2  #position haut du pion
            RB = self.rectangles.listeRectangles[i].get_position().y + self.rectangles.listeTaillesRectangles[i][1]/2  #position bas du pion

            # la logique des collisions avec RB
            if  CRT <= RB and CRT >= RT or CRY <= RB and CRY >= RT or CRB >= RT and CRB <= RB:
                if  CRR >= RL and CRR <= RR or CRL <= RR and CRL >= RL or CRX <= RR and CRX >= RL:
                    self.gameOver = True
                    break


    """ Cette méthode permet de bouger les pions (rectangle bleu) dans le canvas.
    parametre:
    event
    """       
    def moveR(self):

        for i in range(4):

            # Les 4 positions externes de la bordure qu'on va utiliser pour vérifier si les rectangles les touchent
            BL = self.bordure.listeBordures[0].get_position().x - self.bordure.listeTaillesBordure[0][0]/2  #position bordure gauche externe (border left)
            BR = self.bordure.listeBordures[1].get_position().x + self.bordure.listeTaillesBordure[1][0]/2  #position bordure droite externe (border right)
            BT = self.bordure.listeBordures[2].get_position().y - self.bordure.listeTaillesBordure[2][1]/2  #position bordure haut externe (border top)
            BB = self.bordure.listeBordures[3].get_position().y + self.bordure.listeTaillesBordure[3][1]/2  #position bordure bas externe (border bottom)

            # La position d'origin du rectangle selon l'axe de x et de y (RB pour rectangle blue)
            RBY = self.rectangles.listeRectangles[i].get_position().y    #position Y milieu du rectangle blue 
            RBX = self.rectangles.listeRectangles[i].get_position().x    #position X milieu du rectangle blue

            # La position de chaque côte du rectangle (RB pour rectangle blue)
            RBL = RBX - self.rectangles.listeTaillesRectangles[i][0]/2    #position gauche du rectangle blue 
            RBR = RBX + self.rectangles.listeTaillesRectangles[i][0]/2    #position droite du rectangle blue
            RBT = RBY - self.rectangles.listeTaillesRectangles[i][1]/2    #position haut du rectangle blue
            RBB = RBY + self.rectangles.listeTaillesRectangles[i][1]/2    #position bas du rectangle blue
            
            self.vitesse = 14 # La vitesse de la translation du rectangle
            
            # Les directions horizontales et verticales
            DirectionGauche = RBX - self.vitesse
            DirectionHaut = RBY - self.vitesse
            DirectionDroite = RBX + self.vitesse
            DirectionBas = RBY + self.vitesse

            # Les directions diagonales (celles qu'on va utiliser)
            DirectionDroiteHaut = c31.Vecteur(DirectionDroite, DirectionHaut)
            DirectionDroiteBas = c31.Vecteur(DirectionDroite, DirectionBas)
            DirectionGaucheHaut = c31.Vecteur(DirectionGauche, DirectionHaut)
            DirectionGaucheBas = c31.Vecteur(DirectionGauche, DirectionBas)

            # Si c'est le premier tour de mouvement donne le rectange sa direction actuelle pour commencer la translation
            if self.premierMouv:
                if i == 0:
                    self.DirectionActuelle[i] = DirectionDroiteBas
                    self.boolDroiteBas[i] = True
                elif i == 1:
                    self.DirectionActuelle[i] = DirectionGaucheBas
                    self.boolGaucheBas[i] = True
                elif i == 2:
                    self.DirectionActuelle[i] = DirectionDroiteHaut
                    self.boolDroiteHaut[i] = True
                elif i == 3:
                    self.DirectionActuelle[i] = DirectionGaucheHaut
                    self.boolGaucheHaut[i] = True

            # Sinon laisse le continuer avec sa direction actuelle
            else:
                if self.boolDroiteBas[i]:
                    self.DirectionActuelle[i] = DirectionDroiteBas

                elif self.boolDroiteHaut[i]:
                    self.DirectionActuelle[i] = DirectionDroiteHaut

                elif self.boolGaucheBas[i]:
                    self.DirectionActuelle[i] = DirectionGaucheBas

                elif self.boolGaucheHaut[i]:
                    self.DirectionActuelle[i] = DirectionGaucheHaut


            # Si le côte bas du rectangle touche l'extremité du côté bas de la bordure 
            if RBB >= BB:

                # NOTE: Les seules directions qu'on vérifie ici sont les directions: DroiteBas et GaucheBas, 
                # puisque ce sont les seules directions posibles ou le rectangle est en translation vers le bas

                #Si la direction actuelle est DroiteBas alors on le change pour DroiteHaut (sens contraire)
                if self.boolDroiteBas[i]:  
                    self.DirectionActuelle[i] = DirectionDroiteHaut
                    self.boolDroiteBas[i] = False
                    self.boolDroiteHaut[i] = True

                #Si la direction actuelle est GaucheBas alors on le change pour GaucheHaut (sens contraire)
                else: #self.boolGaucheBas 
                    self.DirectionActuelle[i] = DirectionGaucheHaut
                    self.boolGaucheBas[i] = False
                    self.boolGaucheHaut[i] = True


            # Si le côte droit du rectangle touche l'extremité du côté droit de la bordure 
            if RBR >= BR:

                # NOTE: Les seules directions qu'on vérifie ici sont les directions: DroiteBas et DroiteHaut, 
                # puisque ce sont les seules directions posibles ou le rectangle est en translation vers le droit

                #Si la direction actuelle est DroiteBas alors on le change pour GaucheBas (sens contraire)
                if self.boolDroiteBas[i]:
                    self.DirectionActuelle[i] = DirectionGaucheBas
                    self.boolDroiteBas[i] = False
                    self.boolGaucheBas[i] = True
                
                #Si la direction actuelle est DroiteHaut alors on le change pour GaucheHaut (sens contraire)
                else: #self.boolDroiteHaut
                    self.DirectionActuelle[i] = DirectionGaucheHaut
                    self.boolDroiteHaut[i] = False
                    self.boolGaucheHaut[i] = True


            # Si le côte gauche du rectangle touche l'extremité du côté gauche de la bordure 
            if RBL <= BL:

                # NOTE: Les seules directions qu'on vérifie ici sont les directions: GaucheBas et GaucheHaut, 
                # puisque ce sont les seules directions posibles ou le rectangle est en translation vers le gauche

                #Si la direction actuelle est GaucheBas alors on le change pour DroiteBas (sens contraire)
                if self.boolGaucheBas[i]:
                    self.DirectionActuelle[i] = DirectionDroiteBas
                    self.boolGaucheBas[i] = False
                    self.boolDroiteBas[i] = True

                #Si la direction actuelle est GaucheHaut alors on le change pour DroiteHaut (sens contraire)
                else: #self.boolGaucheHaut
                    self.DirectionActuelle[i] = DirectionDroiteHaut
                    self.boolGaucheHaut[i] = False
                    self.boolDroiteHaut[i] = True


            # Si le côte haut du rectangle touche l'extremité du côté haut de la bordure 
            if  RBT <= BT:

                # NOTE: Les seules directions qu'on vérifie ici sont les directions: DroiteHaut et GaucheHaut, 
                # puisque ce sont les seules directions posibles ou le rectangle est en translation vers le haut

                #Si la direction actuelle est DroiteHaut alors on le change pour DroiteBas (sens contraire)
                if self.boolDroiteHaut[i]:
                    self.DirectionActuelle[i] = DirectionDroiteBas
                    self.boolDroiteHaut[i] = False
                    self.boolDroiteBas[i] = True

                #Si la direction actuelle est GaucheHaut alors on le change pour DroiteHaut (sens contraire)
                else: #self.boolGaucheHaut
                    self.DirectionActuelle[i] = DirectionGaucheBas
                    self.boolGaucheHaut[i] = False
                    self.boolGaucheBas[i] = True

            # Mettre en translation le rectangle et sauvegarder sa nouvelle position
            self.rectangles.listeRectangles[i].translateTo(self.DirectionActuelle[i])
            self.rectangles.listeRectangles[i].set_position(self.DirectionActuelle[i])

        # Afficher les 4 rectangles à la fin de la boucle
        self.collision()
        self.vueJeu.afficherRectanglesBlues(self.rectangles)


        self.premierMouv = False # Terminer le premier mouvement

        # Tant que le jeu n'est pas terminer (pas de collision) rappelle la fonction recursivement à chaque 30 miliseconds
        if not self.gameOver:
            wait = Timer(0.03,self.moveR)
            wait.start()
        
        # Sinon reinisialize tout
        else:
            print("You Lost")
            self.pauseTimer()
            self.listScore.append(self.minutes_string + ':' + self.seconds_string + ':' + self.milliseconds_string)
            time.sleep(0.75)
            self.initializeAll()
            print(self.listScore)
            