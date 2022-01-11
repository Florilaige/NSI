class Maillon :

    def __init__(self, val):
        """ Maillon(obj)
            renvoie un maillon contenant l'élément val """
        self.val = val
        self.suiv = None


class Liste :

    def __init__(self):
        """ Liste()
            renvoie une liste vide """
        self.tete = None

    def __repr__(self):
        """ repr(self) -> str
            renvoie une représentation de la liste """
        if self.est_vide():
            return "liste vide"

        s = "liste : "
        maillon = self.tete
        while maillon != None :
            s += repr(maillon.val)+" -> "
            maillon = maillon.suiv
        return s+" None"

    def est_vide(self):
        """ self.est_vide() -> bool
            renvoie True si la liste est vide, False sinon """
        return self.tete == None

    def taille(self):
        """ self.taille() -> int
            renvoie le nombre de maillons de la liste """
        cpt = 0
        m = self.tete
        while m != None:
            cpt += 1
            m = m.suiv
        return cpt

    def ajoute_debut(self, val):
        """ self.ajoute_debut(obj) -> None
            ajoute un nouveau maillon au début de la liste """
        m = self.tete
        self.tete = Maillon(val)
        self.tete.suiv = m

    def ajoute_fin(self, val):
        """ self.ajoute_fin(obj) -> None
            ajoute un nouveau maillon à la fin de la liste """
        if self.tete == None:
            self.tete = Maillon(val)
        m = self.tete
        while m.suiv != None:
            m = m.suiv
        m.suiv = Maillon(val)

    def ajoute_apres(self, val, n):
        """ self.ajoute_a_la_fin(obj) -> None
            ajoute un nouveau maillon après le n-ième maillon """
        assert n < self.taille(), "Indice n trop grand"

        m = self.tete
        for i in range(n):
            m = m.suiv

        nm = Maillon(val)
        nm.suiv = m.suiv
        m.suiv = nm

    def supprime_premier(self):
        """ self.supprime_premier() -> Maillon
            supprime et renvoie le premier maillon de la liste """
        assert self.tete != None, "La liste est déjà vide"
        m = self.tete
        self.tete = m.suiv
        return m.val

    def supprime_dernier(self):
        """ self.supprime_dernier() -> Maillon
            supprime et renvoie le dernier maillon de la liste """
        assert self.tete != None, "La liste est déjà vide"
        m = self.tete
        if self.tete.suiv == None:
            t = self.tete
            self.tete = None
            return t
        while m.suiv.suiv != None:
            m = m.suiv
        m.suiv = None


    def supprime_apres(self, n):
        """ self.supprime_dernier() -> Maillon
            supprime et renvoie le n-ième maillon de la liste """
        assert self.tete != None, "La liste est déjà vide"
        assert n < self.taille(), "Indice n trop grand"
        m = self.tete
        for i in range(n): # --------------------------------------------------- Optimisation
            m = m.suiv

        m1 = m.suiv
        m.suiv = m1.suiv
        return m1.val

    def concatene(self, lst):
        """ self.concatene(Liste) -> None
            ajoute les éléments de lst à la fin de la liste """
        m = lst.tete
        while m != None:
            self.ajoute_fin(m.val)
            m = m.suiv


    def renverse(self):
        """ self.renverse() -> None
            renverse la liste """
        temp = Liste()
        m = self.tete
        while m != None:
            temp.ajoute_fin(m.val)
            m = m.suiv

        self.tete = None

        m = temp.tete
        while m != None:
            self.ajoute_debut(m.val)
            m = m.suiv

        self.supprime_dernier()

    def contient(self, val):
        """ self.contient(val) -> bool
            renvoie True si la liste contient l'élément val,
            False sinon """
        m = self.tete
        while m != None:
            if m.val == val:
                return True
            m = m.suiv
        return False

    def supprime_doublons(self):
        """ self.supprime_doublons() -> None
            supprime les doublons dans la liste """
        pass
