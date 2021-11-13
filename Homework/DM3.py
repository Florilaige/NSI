# Classes

class Information:

    def __init__(self, valeurs):
        self.station_id = int(valeurs[0])
        self.name = str(valeurs[1])
        self.capacity = int(valeurs[2])
        self.lat = float(valeurs[3])
        self.lon = float(valeurs[4])

class Status:
    def __init__(self, valeurs):
        self.station_id = int(valeurs[0])
        self.is_installed = int(valeurs[1])%2 == 1
        self.is_renting = int(valeurs[2])%2 == 1
        self.is_returning = int(valeurs[3])%2 == 1
        self.last_reported = int(valeurs[4])
        self.num_bikes_available = int(valeurs[5])
        self.num_bikes_available_ebike = int(valeurs[6])
        self.num_bikes_available_mechanical = int(valeurs[7])
        self.num_docks_available = int(valeurs[8])


# Exercice 1

informations = []
f = open("station_information.csv", encoding="utf-8")
f.readline()
for line in f:
    entry = line[:-1].split(";")
    el = Information(entry)
    informations.append(el)
f.close()

status = []
f = open("station_status.csv", encoding="utf-8")
f.readline()
for line in f:
    entry = line[:-1].split(";")
    el = Status(entry)
    status.append(el)
f.close()

# Exercice 2

def a():
    return str(len([a for a in status if not a.is_installed]) / len(status) * 100) + " %"
print(a())

def b():
    return [a.name for a in informations if "Lecourbe" in a.name]
print(b())

def c():
    d = {}
    for el in informations:
            d[el.name] = el.lat
    return max(d, key=d.get)
print(c())

def d():
    d = {}
    for el in status:
        d[el.station_id] = el.num_bikes_available
    id = max(d, key=d.get)
    return [a.name for a in informations if a.station_id == id]
print(d())

def e():
    d = {}
    for el in status:
        d[el.station_id] = el.num_bikes_available
    l = []
    for id, n in d.items():
        for el in informations:
            if el.station_id == id and n > el.capacity:
                l.append(el.name)
    return ", ".join(l)
print(e())
