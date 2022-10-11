tab = [[],[],[],[],[],[],[],[],[],[]]


for x in range(0, 10):
    for y in range(0, x+1):
        tab[x].append(y+1)


suma = 0


for x in range(0, 10):
    suma = 0
    for y in range(0, x+1):
        suma += tab[x][y]
    print("suma wiersz" + str(x+1) + "=" + str(suma))


print(tab)