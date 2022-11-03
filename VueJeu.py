from tkinter import Canvas

class VueJeu:

    def afficherCarreRouge(self, carreRouge):
        """Cette méthode affiche le carré rouge."""
        carreRouge.draw()
        
    def afficherRectanglesBlues(self, rectangles):
        """Cette méthode affiche tous les rectangles blues (pions)."""
        for i in range(4):
            rectangles.listeRectangles[i].draw()
            
    def afficherBordure(self, bordure):
        """Cette méthode affiche la bordure."""        
        for i in range(4):
            bordure.listeBordures[i].draw()
             
    def clear(self, container):
        """cette methose suprime la fenetre tout ce qui est dans la fenetre"""
        container = container.grid_slaves()
        for widget in container:
            widget.destroy()
    