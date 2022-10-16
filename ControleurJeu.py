from VueJeu import VueJeu
from ModeleJeu import ModeleJeu
import tkinter as tk

class ControleurJeu:
    
    def __init__(self, container):
        self.vueJeu = VueJeu()
        self.modeleJeu = ModeleJeu(container)
        self.modeleJeu.afficher_carreRouge()
        self.modeleJeu.afficher_rectangleBleu1()
        self.modeleJeu.afficher_rectangleBleu2()
        self.modeleJeu.afficher_rectangleBleu3()
        self.modeleJeu.afficher_rectangleBleu4()

    # cette methode commence le jeu
    def start(self, container):
        #affichage air de jeu
        ModeleJeu.creation_airJeu(container)
        #affichage carre rouge
        ModeleJeu.creation_carreRouge(container)
        #affichage rectangle
        ModeleJeu.creation_rectangleBleu1(container)
        ModeleJeu.creation_rectangleBleu2(container)
        ModeleJeu.creation_rectangleBleu3(container)
        ModeleJeu.creation_rectangleBleu4(container)
        self.vueJeu.clear(container)

    