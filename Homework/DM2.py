##############
# Exercice 1 #
##############

def explose(s, sep):
    """ Renvoie la liste des mots délimités par sep dans s. """
    lst = []
    temp = ""
    for el in s:
        if el in sep:
            if temp != "":
                lst.append(temp)
            temp = ""
        else:
            temp += el
    if temp != "":
        lst.append(temp)
    return lst
    
s = "Que j'aime à faire apprendre ce nombre utile aux sages"
print(explose(s, " "))

s = "Hey, you - what are you doing here!?"
print(explose(s, " ,-!?"))

##############
# Exercice 2 #
##############

data = []
f = open("accidents-2019.csv", encoding="utf-8")
f.readline() # passe l'entête
for line in f:
    entry = line[:-1].split(";") # la syntaxe line[:-1] permet de supprimer 
    # le dernier caractère de line qui est un saut de ligne (\n)
    data.append(entry)
f.close()

print(data[0])
    
def question_1(data):
    """ Renvoie le nombre accidents recensés en 2019. """
    compt = 0
    for i in data:
        if i[3] == "2019":
            compt += 1
    return compt

def question_2(data):
    """ Renvoie le nombre accidents recensés 
        dans les Bouches-du-Rhône en 2019. """
    compt = 0
    for i in data:
        if i[6] == "13":
            compt += 1
    return compt

def question_3(data):
    """ Renvoie le nombre d'accidents survenus au mois de juillet 2019, 
        en plein jour, hors agglomération, 
        dans des conditions atmosphériques normales. """
    compt = 0
    for i in data:
        if i[2] == "7" and i[3] == "2019" and i[5] == "1" and i[8] == "1" and i[10] == "1":
            compt += 1
    return compt



def question_4(data):
    """ Renvoie le pourcentage des accidents survenus entre vingt heures 
        et six heures du matin, parmi tous les accidents survenus en 2019. """
    compt = 0
    total = 0
    for i in data:
        if i[3] == "2019":
            total += 1
            h = i[4].split(":")
            if int(h[0]) >= 20 or int(h[0]) <= 5:
                compt += 1
    return "En 2019, " + str((compt/total)*100) + "% des accidents ont eu lieu entre 20h et 6h."
    
def question_5(data):
    """ Renvoie le numéro du département qui a enregistré le plus 
        d'accidents corporels en 2019. """
    d = {}
    for i in data:
        dep = i[6]
        if dep in d:
            d[dep] += 1
        else :
            d[dep] = 1
    return max(d, key=d.get)

print(question_1(data))
print(question_2(data))
print(question_3(data))
print(question_4(data))
print(question_5(data))
