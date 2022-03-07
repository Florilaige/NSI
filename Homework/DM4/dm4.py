#from ast import Str
#from typing import Tuple
import pygame
from pygame.locals import *

image = pygame.image.load("image.png")

class Exercice_1:

    def __init__(self) -> None:
        
        # initialisation de pygame
        pygame.init()
        self.window = pygame.display.set_mode((400, 400))

        # affichage de l'image
        image = pygame.image.load("image.png")
        self.window.blit(image, (0, 0))
        pygame.display.update()

        # décryptage de l'image
        self.decryption()
        pygame.display.update()

        # maintien de la fenêtre
        self.hold()
        
    def hold(self) -> None:
        """Maintient la fenêtre ouverte jusqu'à sa fermeture
            ou la pression de la touche 'Echap'."""
        lock = True
        while lock:
            events_list = pygame.event.get()
            for event in events_list:
                if event.type == QUIT:
                    lock = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        lock = False
        pygame.quit()

    def decrypt_pixel(self, p) -> Tuple:
        """Décrypte les valeurs cachées dans les bits de poids
            faible des valeurs du pixel p et retourne le
            nouveau pixel qu'elles forment.""" 
        new = []
        for el in p:
            bin_val = bin(el)[2:].rjust(8, "0")
            new_val = bin_val[4:] + "0000"
            new.append(int(new_val, 2))
        return tuple(new)
    
    def decryption(self) -> None:
        """Affiche l'image cachée."""
        for x in range(400):
            for y in range(400):
                pixel = self.window.get_at((x, y))[:-1]
                self.window.set_at((x, y), self.decrypt_pixel(pixel))

Exercice_1()

class Exercice_2:

    def __init__(self) -> None:
        
        # initialisation de pygame
        pygame.init()
        self.window = pygame.display.set_mode((400, 400))

        # affichage de l'image
        image = pygame.image.load("image2.png")
        self.window.blit(image, (0, 0))
        pygame.display.update()

        # décryptage de l'image
        self.decryption()

        # maintien de la fenêtre
        self.hold()
        
    def hold(self) -> None:
        """Maintient la fenêtre ouverte jusqu'à sa fermeture
            ou la pression de la touche 'Echap'."""
        lock = True
        while lock:
            events_list = pygame.event.get()
            for event in events_list:
                if event.type == QUIT:
                    lock = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        lock = False
        pygame.quit()
    
    def decrypt_pixel(self, p) -> Str:
        """Décrypte les valeurs cachées dans les bits de poids
            faible des valeurs du pixel p et retourne le charactère
            qu'elles cachent.""" 
        val = ""
        for el in p:
            bin_val = bin(el)[2:].rjust(8, "0")
            val += bin_val[4:]
        return chr(int(val, 2))
    
    def decryption(self) -> None:
        """Affiche le message caché."""
        hidden = ""
        for x in range(400):
            for y in range(400):
                pixel = self.window.get_at((x, y))[:-1]
                hidden += self.decrypt_pixel(pixel)
        print(hidden)

Exercice_2()