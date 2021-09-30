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
    p_temp = Pile()
    np = Pile()

    while not p.est_vide():
        el = p.depile()
        p_temp.empile(el)
        np.empile(el)


    while not p_temp.est_vide():
        el = p_temp.depile()
        p.empile(el)

    return np

#4
def copie(p):
    p_temp = Pile()

    while not p.est_vide():
        el = p.depile()
        p_temp.empile(el)

    np = Pile()
    while not p_temp.est_vide():
        el = p_temp.depile()
        np.empile(el)
        p.empile(el)

    return np

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
def test_parenthesage(x):
    p = Pile()
    ouvrants = ["(", "[", "{"]
    fermants = [")", "]", "}"]

    for i in x:
        if i in ouvrants:
            p.empile(fermants[ouvrants.index(i)])

        if i in fermants:
            if p.est_vide() or p.depile() != i:
                return False

    if not p.est_vide():
        return False
    return True

assert test_parenthesage (" (a )( b )((( c )(d )))" )== True
assert test_parenthesage (" ([b ]){(( c ))[d ]} " )== True
assert test_parenthesage (" (" )== False
assert test_parenthesage (" (a )) " )== False
assert test_parenthesage (" ((a ))}" )== False
assert test_parenthesage (" [[a ]" )== False
assert test_parenthesage (" [(a ])" )== False
assert test_parenthesage (" {((a )})" )== False

#7
def ranger(p):
    blanches = Pile()
    vertes = Pile()
    while not p.est_vide():
        el = p.depile
        if el[0] == "vert":
            vertes.empile(el)
        elif el[0] == "blanc":
            blanches.empile(el)

    while not blanches.est_vide():
        p.empile(blanches.depile())

    while not vertes.est_vide():
        p.empile(vertes.depile())



assiettes = Pile()
assiettes.empile(("vert", 5))
assiettes.empile(("vert", 4))
assiettes.empile(("blanc", 7))
assiettes.empile(("vert", 1))
assiettes.empile(("blanc", 9))
assiettes.empile(("blanc", 7))
assiettes.empile(("vert", 3))
print(assiettes)
ranger(assiettes)
print(assiettes)
