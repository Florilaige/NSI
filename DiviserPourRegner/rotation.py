import pygame
from pygame.locals import *


class Main :

    def __init__(self):
        """ Main()
            Affiche l'image 'buffon.png' dans une fenêtre pygame
            et applique la méthode rotation().
        """

        # initialisation de pygame
        pygame.init()
        self.window = pygame.display.set_mode((512, 512))

        # affichage de l'image
        image = pygame.image.load("buffon.png")
        self.window.blit(image, (0, 0))
        pygame.display.update()

        # rotation de l'image
        self.rotation(0,0,512)

        # maintien de la fenêtre
        self.hold()


    def hold(self):
        """ hold() -> None
            Maintient la fenêtre ouverte jusqu'à sa fermeture
            ou la pression de la touche 'Echap'."""
        lock = True
        while lock :
            events_list = pygame.event.get()
            for event in events_list :
                if event.type == QUIT :
                    lock = False
                if event.type == KEYDOWN :
                    if event.key == K_ESCAPE :
                        lock = False
        pygame.quit()


    def rotation(self, x, y, t):
        """ rotation()->None
            Tourne l'image d'un quart de tour."""

        t //= 2

        if t>1:
            self.rotation(x, y, t)
            self.rotation(x+t, y, t)
            self.rotation(x+t, y+t, t)
            self.rotation(x, y+t, t)



        for j in range(x, x+t):
            for i in range(y, y+t):
                pixel_1 = self.window.get_at((j,i))
                pixel_2 = self.window.get_at((j+t,i))
                pixel_3 = self.window.get_at((j+t,i+t))
                pixel_4 = self.window.get_at((j,i+t))
                self.window.set_at((j,i), pixel_4)
                self.window.set_at((j+t,i), pixel_1)
                self.window.set_at((j+t,i+t), pixel_2)
                self.window.set_at((j,i+t), pixel_3)
        pygame.display.update()

Main()
