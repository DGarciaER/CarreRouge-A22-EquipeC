from tkinter import Canvas
class ModeleJeu:
    #methode pour creer lair de jeu
    def creation_airJeu (container):
        airJeu = Canvas(container,bg="#808080", width= 450, height=450)
        airJeu.place(x=10,y=0)

    #methode pour creer le carre rouge
    def creation_carreRouge(container):
        carreRouge = Canvas(container, bg="#ff0000", width=20, height=20)
        carreRouge.place(x=100,y=60)

    #methode pour creer rectangle bleu1
    def creation_rectangleBleu1(container):
        rectangleBleu = Canvas(container, bg="#0000ff", width=30, height=30)
        rectangleBleu.place(x=5, y=2)

    #methode pour creer rectangle bleu2
    def creation_rectangleBleu2(container):
        rectangleBleu = Canvas(container, bg="#0000ff", width=30, height=30)
        rectangleBleu.place(x=150, y=2)

    #methode pour creer rectangle bleu3
    def creation_rectangleBleu3(container):
        rectangleBleu = Canvas(container, bg="#0000ff", width=20, height=50)
        rectangleBleu.place(x=20, y=120)

    #methode pour creer rectangle bleu4
    def creation_rectangleBleu4(container):
        rectangleBleu = Canvas(container, bg="#0000ff", width=150, height=20)
        rectangleBleu.place(x=100, y=100)
