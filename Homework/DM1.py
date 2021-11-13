#1
def vue_sur_la_mer(lst):
    a = 0
    els = []
    for i in reversed(lst):
        if i>a:
            a = i
            els.append(i)
    return els

liste = [5, 12, 8, 9, 5, 2, 3]
print(vue_sur_la_mer(liste))

#2
def recherche(texte, mot):
    lst = []
    for i in range(len(texte)-1):
        if texte.startswith(mot, i):
            lst.append(i)
    return lst

assert recherche("abcab", "ab") == [0, 3]
assert recherche("abc" * 3, "ab") == [0, 3, 6]
assert recherche("ba" * 4, "ab") == [1, 3, 5]
assert recherche("abcd" * 2, "ad") == []
assert recherche("abcd" * 2, "da") == [3]
assert recherche("ab" * 4, "abab") == [0, 2, 4]


#3
f = open("dico.txt", "r", encoding="utf -8")
dico = []
for ligne in f:
    dico.append(ligne [: -1])

g = open("mots.txt", "r", encoding="utf -8")
mots = []
for ligne in g:
    mots.append(ligne[: -1])

print("Nombre de mots de dico.txt (en comptant les trois \"a\" du début) :", len(dico))

liste = []
k = 0
for i in mots:
    a = False
    for j in dico:
        if i == j:
            a = True
            break
    if not a:
        liste.append(i)
    k+=1

print(liste)
