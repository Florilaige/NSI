import pygame
from pygame.locals import *

class Dessin :
    """ Dessin() -> Dessin
        Classe permettant de dessiner des rectangles sur une fenêtre.
        La fenêtre a pour dimensions 600x400.
    """

    def __init__(self):
        self.rectangles = []
        pygame.init()
        pygame.font.init()

        size = (600, 400)
        self.window = pygame.display.set_mode(size)

    def ajoute_rectangle(self, x, y, w, h, c):
        """ ajoute_rectangle(int x, int y, int w, int h, tuple c) -> None
            Ajoute un rectangle.
            x, y : coordonnées du coin supérieur gauche du rectangle
            w, h : largeur et hauteur du rectangle
            c : couleur du rectangle au format (r, v, b)
        """
        self.rectangles.append((x, y, w, h, c))

    def affiche(self):
        """ affiche() -> None
            Affiche la fenêtre.
            Cette méthode doit être appellée après l'ajout des rectangles."""
        lock = True
        while lock:
            self.window.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    lock = False

            for x, y, w, h, c in self.rectangles :
                rect = pygame.Rect(x, y, w, h)
                pygame.draw.rect(self.window, c, rect)


            pygame.display.update()

        pygame.quit()

# Drapeau français
drapeau = Dessin()
drapeau.ajoute_rectangle(0,0,200,400,(0,0,200))
drapeau.ajoute_rectangle(200,0,200,400,(255,255,255))
drapeau.ajoute_rectangle(400,0,200,400,(255,0,0))
drapeau.affiche()

# Carrés
carres = Dessin()
carres.ajoute_rectangle(0,0,600,400,(255,255,255))
carres.ajoute_rectangle(100,0,400,400,(0,0,0))
carres.ajoute_rectangle(150,50,300,300,(0,0,250))
carres.ajoute_rectangle(200,100,200,200,(0,250,0))
carres.ajoute_rectangle(250,150,100,100,(250,0,0))
carres.affiche()

# Dammier
dammier = Dessin()
for i in range(6):
    for j in range(4):
        dammier.ajoute_rectangle(100*i, 100*j, 50, 50, (255,255,255))
        dammier.ajoute_rectangle(100*i+50, 100*j+50, 50, 50, (255,255,255))
dammier.affiche()

#Labyrinthe (A finir)
labyrinthe = Dessin()
labyrinthe.ajoute_rectangle(0,0,600,400,(255,255,255))
for i in range(10):
    labyrinthe.ajoute_rectangle(200+20*i,0+20*i,400-40*i,400-40*i,(0,0,0))
    labyrinthe.ajoute_rectangle(210+20*i,10+20*i,380-40*i,380-40*i,(0,0,0))
labyrinthe.affiche()
