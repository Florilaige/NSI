def hanoi(n, source, dest, inter):
    if n==1:
        return print("Déplacer 1 disque de la tour", source, "à la tour", dest)
    hanoi(n-1, source, inter, dest)
    hanoi(1, source, dest, inter)
    hanoi(n-1, inter, dest, source)

hanoi(5, 1, 3, 2)
