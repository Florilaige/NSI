class File:

    def __init__(self):
        self.content = []

    def enfile(self, el):
        self.content.append(el)

    def defile(self):
        assert not self.est_vide(), "La file est déjà vide."
        return self.content.pop(0)

    def taille(self):
        return len(self.content)

    def est_vide(self):
        return self.taille() == 0

    def __repr__(self):
        if self.est_vide():
            return "|"
        prt = "| "
        for i in f.content:
            prt += str(i) + "| "
        return prt

# ----- Exercice 2 -----

#1
def passe_ton_tour(f):
    f.enfile(f.defile())

#2&3
def nb_occurences(f, val):
    f1 = File()
    cpt = 0
    while not f.est_vide():
        el = f.defile()
        if el == val:
            cpt += 1
        f1.enfile(el)
    while not f1.est_vide():
        f.enfile(f1.defile())
    return cpt

#4
def last_in_first(f):
    for i in range(f.taille()-1):
        passe_ton_tour(f)


# ----- Exercice 3 -----

#1
def permute_prochains(f):
    el1 = f.defile()
    f.enfile(f.defile())
    f.enfile(el1)
    for i in range(f.taille()-2):
        passe_ton_tour(f)

#2
def permute_derniers(f):
    for i in range(f.taille()-2):
        passe_ton_tour(f)
    el1 = f.defile()
    f.enfile(f.defile())
    f.enfile(el1)


# ----- Exercice 4 -----

#1
def est_dans_la_file(f, val):
    return nb_occurences(f, val) >=1

#2
def supprime_doublons(f):
    for i in range(f.taille()):
        el = f.defile()
        if nb_occurences(f, el) == 0:
            f.enfile(el)


# ----- Exercice 5 -----

def vin_first(f):
    vin = File()
    nvin = File()
    while not f.est_vide():
        el = f.defile()
        assert type(el) == int, "La liste ne doit contenir que des entiers."
        if el%12 == 0:
            vin.enfile(el)
        else:
            nvin.enfile(el)
    while not vin.est_vide():
        f.enfile(vin.defile())
    while not nvin.est_vide():
        f.enfile(nvin.defile())


# ----- Exercice 6 -----

class Pile():

    def __init__(self):
        self.main = File()
        self.secondary = File()

    def empile(self, el):
        self.main.enfile(el)

    def depile(self):
        assert not self.est_vide(), "La pile est déjà vide."
        while self.main.taille()>=1:
            self.secondary.enfile(self.main.defile())
        el = self.main.defile()
        while not self.secondary.est_vide():
            self.main.enfile(self.secondary.defile())

    def taille(self):
        return self.main.taille()

    def est_vide(self):
        return self.main.est_vide()

    def __repr__(self):
        if self.est_vide():
            return "| |"
        prt = ""
        for i in range(self.main.taille()):
            el = self.main.defile()
            prt += "|" + str(el) + "|\n"
            self.main.enfile(el)
        return prt
