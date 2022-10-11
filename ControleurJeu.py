from VueJeu import VueJeu
import tkinter as tk

class ControleurJeu:
    
    def __init__(self):
        self.vueJeu = VueJeu()

    # cette methode commence le jeu
    def start(self, container):
        self.vueJeu.clear(container)