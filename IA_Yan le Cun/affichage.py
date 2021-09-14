import pygame
from pygame.locals import *


train_images = open("train-images.idx3-ubyte", mode = "br")
train_labels = open("train-labels.idx1-ubyte", mode = "br")
test_images = open("t10k-images.idx3-ubyte", mode = "br")
test_labels = open("t10k-labels.idx1-ubyte", mode = "br")

b = train_images.read(16) # Passe les 16 premiers octets d'entête.
l = train_labels.read(8) # Passe les 8 premiers octets d'entête.
b = test_images.read(16) # Passe les 16 premiers octets d'entête.
l = test_labels.read(8) # Passe les 8 premiers octets d'entête.

# Mise en place de la page
pygame.init()
window = pygame.display.set_mode((280,300))

# Mise en place de la font
pygame.font.init()
font = pygame.font.SysFont("Calibri", 25)

# Variables
c = 0

t_images = []
t_labels = []
t_number = 6000

images = []
labels = []
number = 1000

# Fonctions
def load_images(f):
    '''
    Charge une image du fichier f.
    '''
    lst = []
    for i in range(28):
        line = []
        for j in range(28):
            b = f.read(1)
            c = int.from_bytes(b, byteorder = "big")
            line.append(c)
        lst.append(line)
    return lst

def load_labels(f):
    """
    Charge un label du fichier f.
    """
    b = f.read(1)
    c = int.from_bytes(b, byteorder = "big")
    return c

def image():
    window.fill((0,0,0)) # Vide la page
    # Affichage de l'image
    for i in range(28):
        for j in range(28):
            colour = t_images[c][i][j]
            pygame.draw.rect(window, (colour, colour, colour), (10*j, 10*i, 10, 10))

    # Affichage du numéro de l'image
    number = font.render("Image n°" + str(c+1), True, (255,255,255))
    window.blit(number, dest = (5,275))

    # Affichage du label
    label = font.render("Label :" + str(t_labels[c]), True, (255,255,255))
    window.blit(label, dest=(150, 275))
    pygame.display.flip() # Actualise la page.

def distance(im1,im2):
    sum = 0
    for i in range(28):
        for j in range(28):
            sum += abs(im1[i][j]-im2[i][j])
    return sum


# Main
for i in range(t_number):
    t_images.append(load_images(train_images))

for i in range(t_number):
    t_labels.append(load_labels(train_labels))

for i in range(number):
    images.append(load_images(test_images))

for i in range(number):
    labels.append(load_labels(test_labels))

print(distance(t_images[0],t_images[1]))

image()
lock = True
while lock:
    for event in pygame.event.get():
        if event.type == QUIT: # Ferme la fenetre
            lock = False
        if event.type == KEYDOWN and event.key == K_RIGHT: # Passe à l'image suivante
            c+=1
            image()
        if event.type == KEYDOWN and event.key == K_LEFT and c!=0: # Passe à l'image précédente
            c-=1
            image()


pygame.quit()
