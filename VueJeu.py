from tkinter import Canvas


class VueJeu:
    
    # cette methose suprime la fenetre tout ce qui est dans la fenetre
    def clear(self, container):
        container = container.grid_slaves()
        for widget in container:
            widget.destroy()

    

    