from pile import Pile

#1
p = Pile()
p.empile("n")
p.empile("s")
p.empile("i")

#2
def echange(p):
    if p.taille() >= 2:
        x = p.depile()
        y = p.depile()
        p.empile(x)
        p.empile(y)

#3
def inverse(p):
    if p.taille() >= 2:
        pl1 = Pile()
        pl2 = Pile()
        while not p.est_vide():
            x = p.depile()
            pl1.empile(x)
            pl2.empile(x)
        while not pl2.est_vide():
            p.empile(pl2.depile())
        return pl1

#4
def copie(p):
    return(inverse(inverse(p)))

#5.1
def fond(p):
    if not p.est_vide():
        pl = Pile()
        while not p.est_vide():
            x = p.depile()
            pl.empile(x)
        n = pl.depile()
        while not pl.est_vide():
            p.empile(pl.depile())
        return n

#5.2
def rotation(p):
    if p.taille() >= 2:
        pl = Pile()
        a = p.depile()
        while not p.est_vide():
            pl.empile(p.depile())
        n = pl.depile()
        pl.empile(a)
        while not pl.est_vide():
            p.empile(pl.depile())
        p.empile(n)

#6





''' Jeu de test :
assert test_parenthesage (" (a )( b )((( c )(d )))" )== True
assert test_parenthesage (" ([b ]){(( c ))[d ]} " )== True
assert test_parenthesage (" (" )== False
assert test_parenthesage (" (a )) " )== False
assert test_parenthesage (" ((a ))}" )== False
assert test_parenthesage (" [[a ]" )== False
assert test_parenthesage (" [(a ])" )== False
assert test_parenthesage (" {((a )})" )== False
'''
