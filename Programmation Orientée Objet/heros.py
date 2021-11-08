from random import randint

class Heros:

    def __init__(self, nom, pv, res, dmax):
        print("Création du héros "+nom)
        self.nom = nom
        self.points_de_vie = pv
        self.resistance = res
        self.degats_max = dmax

    def __repr__(self):
        return self.nom + " [" + str(self.points_de_vie) + "/" + str(self.resistance) + "/" + str(self.degats_max) + "]"

    def est_en_vie(self):
        return self.points_de_vie>0

    def attaque(self, autre):
        if self.est_en_vie():
            if randint(1,10)==1:
                degats = self.degats_max
            else:
                degats = randint(1, self.degats_max)
            autre.subit_attaque(self, degats)

    def subit_attaque(self, autre, degats):
        if degats>self.resistance:
            self.points_de_vie -= degats
            print(self.nom+" perd "+str(degats)+" points de vie")
        else:
            print(autre.nom+" a raté son attaque contre "+self.nom)
        if not self.est_en_vie():
            print(autre.nom+" a tué "+self.nom)

#scénario

troie = []
grece = []

for i in range(1, 101):
    troie.append(Heros("Plouc Troyen n°" + str(i), randint(50, 100), randint(20, 40), randint(20, 40)))
    grece.append(Heros("Gueu Grec n°" + str(i), randint(50, 100), randint(20, 40), randint(20, 40)))

while len(troie)!=0 and len(grece)!=0:
    grece[randint(0, len(grece)-1)].attaque(troie[randint(0, len(troie)-1)])
    troie[randint(0, len(troie)-1)].attaque(grece[randint(0, len(grece)-1)])

if len(grece)==0:
    print("Troie est victorieuse !\n" + troie + grece)

if len(troie)==0:
    print("La Grèce est victorieuse !\n" + grece + troie)
