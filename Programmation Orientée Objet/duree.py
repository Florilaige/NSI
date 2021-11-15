class Duree:
    """ Duree ( int , int) -> Duree
        Classe représentant une durée en heures, minutes et secondes. """

    def __init__(self, h, m, s):
        self.heures = h
        self.minutes = m
        self.secondes = s
        while self.secondes >= 60:
            self.minutes += 1
            self.secondes -= 60
        while self.minutes >= 60:
            self.heures += 1
            self.minutes -= 60

    def affiche(self):
        """ affiche() -> None
            Affiche la durée au format hh:mm:ss."""
        hh = str(self.heures ).rjust(2 , "0")
        mm = str(self.minutes).rjust(2 , "0")
        ss = str(self.secondes).rjust(2, "0")

        print ( hh +":"+ mm )

    def allonge(self, duree):
        """ allonge( Duree ) -> Duree
            Allonge la durée de celle passée en argument."""
        h = self.heures + duree.heures
        m = self.minutes + duree.minutes
        s = self.secondes + duree.secondes
        if s >=60 :
           s -= 60
           m += 1
        if m >=60 :
           m -= 60
           h += 1
        self.heures = h
        self.minutes = m
        self.secondes = s

    def en_minutes(self):
        return self.heures*60 + self.minutes + self.secondes/60

d1 = Duree (1, 23)
d2 = Duree (2, 51)
d1.affiche()
d2.affiche()
d1.allonge(d2)
d1.affiche()
d1.allonge(d1)
d1.affiche()
d2.affiche()
