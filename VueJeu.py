from tkinter import Canvas

class VueJeu:

    """Cette méthode affiche le carré rouge."""
    def afficherCarreRouge(self, carreRouge):
        carreRouge.draw()
        
    """Cette méthode affiche tous les rectangles blues (pions)."""
    def afficherRectanglesBlues(self, rectangles):
        for i in range(4):
            rectangles.listeRectangles[i].draw()
            
    """Cette méthode affiche la bordure."""        
    def afficherBordure(self, bordure):
        for i in range(4):
            bordure.listeBordures[i].draw()
            
                
    # # cette methose suprime la fenetre tout ce qui est dans la fenetre
    # def clear(self, container):
    #     container = container.grid_slaves()
    #     for widget in container:
    #         widget.destroy()
    