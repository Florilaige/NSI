train_images = open("train-images.idx3-ubyte", mode = "br")
train_labels = open("train-labels.idx1-ubyte", mode = "br")
test_images = open("t10k-images.idx3-ubyte", mode = "br")
test_labels = open("t10k-labels.idx1-ubyte", mode = "br")

b = train_images.read(16) # Passe les 16 premiers octets d'entête.
l = train_labels.read(8) # Passe les 8 premiers octets d'entête.
b = test_images.read(16) # Passe les 16 premiers octets d'entête.
l = test_labels.read(8) # Passe les 8 premiers octets d'entête.

# Variables
t_images = []
t_labels = []
t_number = 6000

images = []
labels = []
number = 1000

# Fonctions
def load_images(f):
    '''
    Charge une image du fichier f.
    '''
    lst = []
    for i in range(28):
        line = []
        for j in range(28):
            b = f.read(1)
            c = int.from_bytes(b, byteorder = "big")
            line.append(c)
        lst.append(line)
    return lst

def load_labels(f):
    """
    Charge un label du fichier f.
    """
    b = f.read(1)
    c = int.from_bytes(b, byteorder = "big")
    return c

def distance(im1,im2):
    sum = 0
    for i in range(28):
        for j in range(28):
            sum += abs(im1[i][j]-im2[i][j])
    return sum

def plusProcheVoisin(img):
    nbr = None
    dist = None
    for i in range(t_number):
        s = distance(img,t_images[i])
        if dist == None or s < dist:
            nbr = t_labels[i]
            dist = s
    return (nbr, dist)


# Main
for i in range(t_number):
    t_images.append(load_images(train_images))

for i in range(t_number):
    t_labels.append(load_labels(train_labels))

for i in range(number):
    images.append(load_images(test_images))

for i in range(number):
    labels.append(load_labels(test_labels))

winRate = 0

for i in range(number):
    guess = plusProcheVoisin(images[i])
    print("Image n°", i+1, ":  Guess =", guess[0], "Real number =", labels[i], "Distance :", guess[1])
    if guess[0] == labels[i]:
        winRate += 1

print("Taux de réussite :", (winRate/number)*100, "%")
