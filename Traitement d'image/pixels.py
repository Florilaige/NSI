import pygame
from pygame.locals import *


def transform(window):
    lst = []

    for i in range(512):
        lst.append([])
        for j in range(512):
            r, g, b, a = window.get_at((i, j))  # rÃ©cupÃ¨re la valeur d'un pixel
            n = (r+g+b)//3
            lst[i].append(n)

    for i in range(512):
        for j in range(512):
            f = lst[j][511-i]
            color = (f, f, f)
            window.set_at((i, j), color)    # dÃ©finit la valeur d'un pixel

# initialisation de pygame
pygame.init()
window = pygame.display.set_mode((512, 512))

# affichage de l'image
image = pygame.image.load("buffon.png")
window.blit(image, (0, 0))

pygame.display.update()


lock = True
while lock :
    events_list = pygame.event.get()
    for event in events_list :
        if event.type == QUIT :
            lock = False
        if event.type == KEYDOWN :
            if event.key == K_ESCAPE :
                lock = False
            if event.key == K_SPACE :
                transform(window)
                pygame.display.update()


pygame.quit()
