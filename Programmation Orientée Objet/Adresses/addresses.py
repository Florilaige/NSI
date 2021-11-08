from math import sqrt, sin, cos, asin, pi
import pygame
from pygame.locals import *

class Adresse:

    def __init__(self, valeurs):
        self.id = valeurs[0]
        self.numero = int(valeurs[1])
        self.rep = valeurs[2]
        self.nom_voie = valeurs[3]
        self.code_postal = int(valeurs[4])
        self.nom_commune = valeurs[5]
        self.x = float(valeurs[6])
        self.y = float(valeurs[7])
        self.lon = float(valeurs[8])
        self.lat = float(valeurs[9])


    def affiche(self, window, color):
        x = int(0.05331*self.x - 34236)
        y = int(-0.053697*self.y + 368804)
        r = pygame.Rect(x, y, 1, 1)
        pygame.draw.rect(window, color, r)

def question_1(adresses):
    return [a for a in adresses if "Place" in a.nom_voie]

def question_2(adresses):
    return [a for a in adresses if a.code_postal==75015 and a.numero%2==0]

def question_3(adresses):
    return [a for a in adresses if 2.3<a.lon<2.4 and 48.84<a.lat<48.87]

def question_4(adresses):
    d = {}
    for a in adresses:
        if a.nom_voie in d.keys():
            d[a.nom_voie] +=1
        else:
            d[a.nom_voie] = 1

    voie = max(d, key=d.get)
    return [a for a in adresses if a.nom_voie==voie]

def question_5(adresses):
    for a in adresses:
        if a.id=="75115_7089_00016":
            buffon = a
            break
    return [a for a in adresses if distance(a,buffon)<=1]

def distance(a1, a2):
    f1 = a1.lat * pi/180
    f2 = a2.lat * pi/180
    l1 = a1.lon * pi/180
    l2 = a2.lon * pi/180

    d = sin((f2-f1)/2)**2+cos(f1)*cos(f2)*sin((l2-l1)/2)**2
    d = sqrt(d)
    d = asin(d)
    d *= 12000
    return d


# Extraction des donnÃ©es
adresses = []
f = open("adresses-75.csv", encoding="utf-8")
f.readline() # passe l'entÃªte
for line in f:
    entry = line[:-1].split(";")
    adr = Adresse(entry)
    adresses.append(adr)
f.close()

# Affichage des adresses sÃ©lectionnÃ©es

pygame.init()
window = pygame.display.set_mode((1024, 667))

img = pygame.image.load("paris.png")

liste_adresses = adresses

rafraichir = True
lock = True
while lock:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT :
            lock = False

        if event.type == KEYDOWN :
            if event.key == K_ESCAPE:
                lock = False
            if event.key == K_KP1:
                liste_adresses = question_1(adresses)
            if event.key == K_KP2:
                liste_adresses = question_2(adresses)
            if event.key == K_KP3:
                liste_adresses = question_3(adresses)
            if event.key == K_KP4:
                liste_adresses = question_4(adresses)
            if event.key == K_KP5:
                liste_adresses = question_5(adresses)
            rafraichir = True

    if rafraichir:
        window.blit(img, (0, 0))
        color = (255, 0, 0)
        for adr in liste_adresses:
            adr.affiche(window, color)
        pygame.display.update()

        rafraichir = False

pygame.quit()
